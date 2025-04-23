from flask import Flask, request, jsonify, redirect, url_for  # , send_from_directory
from flask_cors import CORS  # type: ignore
from apscheduler.schedulers.background import BackgroundScheduler # type: ignore
from utils.state import equ_manager
from utils.params import equ_params
from utils.logger import logger
import importlib
import threading
import logging
import os

app = Flask(__name__, static_folder="public")  # 设置静态资源目录为 public
CORS(app)  # 允许跨域请求


# 初始化 APScheduler
scheduler = BackgroundScheduler()

# 加载任务模块
def load_tasks():
    tasks_dir = "scheduled"
    for file in os.listdir(tasks_dir):
        if file.endswith(".py") and file != "__init__.py":
            module_name = file[:-3]  # 去掉 .py 后缀
            module_path = f"{tasks_dir}.{module_name}"
            try: 
                module = importlib.import_module(module_path)
                if hasattr(module, "run") and hasattr(module, "SCHEDULE_CONFIG"):
                    schedule_config = module.SCHEDULE_CONFIG
                    trigger = schedule_config.pop("trigger")
                    scheduler.add_job(module.run, trigger, **schedule_config)
                    # print(f"Loaded task: {module_name}")
            except Exception as e:
                print(f"Failed to load task {module_name}: {e}")


# 禁用 Flask 的默认日志记录器
# 配置日志记录器
logging.basicConfig(level=logging.WARNING)
log = logging.getLogger('werkzeug')
log.setLevel(logging.WARNING)

# 禁用 Flask 的默认日志记录器
app.logger.disabled = True
log.disabled = True

# 状态查询接口
@app.route('/api/status', methods=['GET'])
def get_status():
    status = equ_manager.get()
    return jsonify(status)

# 参数查询接口
@app.route('/api/params', methods=['GET'])
def get_params():
    params = equ_params.get()
    return jsonify(params)

# 参数修改接口
@app.route('/api/params', methods=['PUT'])
def modify_params():
    data = request.json
    key_name = data.get('key_name')
    value = data.get('value')
    if key_name:
        try:
            equ_params.update_path(key_name, value)
            return jsonify({"success": True, "detail": "修改成功"})
        except Exception as e:
            return jsonify({"success": False, "detail": str(e)})
    else:
        return jsonify({"success": False, "detail": "缺少必要的参数"})

# 操作按钮接口
@app.route('/api/operate', methods=['POST'])
def operate():
    data = request.json
    key_name = data.get('key_name')
    params = data.get('params')
    if key_name:
        try:
            # 动态加载模块
            module_name = f"service.operate.{key_name}"
            module = importlib.import_module(module_name)
            # 在后台线程中调用模块的 main 方法
            thread = threading.Thread(target=module.main, args=(params,))
            equ_manager.set_equ_status(status="busy")
            thread.start()
            return jsonify({"success": True, "detail": "下发成功"})
        except ModuleNotFoundError:
            return jsonify({"success": False, "detail": f"未找到操作 {key_name}","code":-1})
        except AttributeError:
            return jsonify({"success": False, "detail": f"操作 {key_name} 中没有 main 方法","code":-1})
        except Exception as e:
            return jsonify({"success": False, "detail": str(e),"code":-1})
    else:
        return jsonify({"success": False, "detail": "缺少必要的参数","code":-1})

# 技能执行接口
@app.route('/api/order', methods=['POST'])
def order():
    data = request.json
    key_name = data.get('key_name')
    params = data.get('params')
    task_id = data.get('task_id')
    if key_name and task_id:
        if equ_manager.equ['status'] == "busy":
            logger.warning(f"技能{key_name}未执行,设备繁忙！")
            return jsonify({"success": False, "detail": "设备繁忙！","code":0})
        
        # 处理锁的逻辑
        lock_key = params.get('lock_key', None)  # 安全地获取 lock_key
        lock = params.get('lock', None)  # 安全地获取 lock_key
        # print(lock,lock_key)
        if not equ_params.unlock(lock_key):
            return jsonify({"success": False, "detail": "设备已锁定！","code":1})
        try:
            # 上锁
            equ_params.lock(lock)
            # 动态加载模块
            module_name = f"service.order.{key_name}"
            module = importlib.import_module(module_name)
            # 在后台线程中调用模块的 main 方法
            thread = threading.Thread(target=module.main, args=(params,))
            equ_manager.running({"task_id": task_id, "order": key_name})
            thread.start()
            return jsonify({"success": True, "detail": "下发成功"})
        except ModuleNotFoundError:
            return jsonify({"success": False, "detail": f"未找到技能 {key_name}","code":-1})
        except AttributeError:
            return jsonify({"success": False, "detail": f"技能 {key_name} 中没有 main 方法","code":-1})
        except Exception as e:
            return jsonify({"success": False, "detail": str(e),"code":-1})
    else:
        return jsonify({"success": False, "detail": "缺少必要的参数","code":-1})

# 配置详情接口
@app.route('/api/config-detail', methods=['GET'])
def get_py_files():
    # 获取环境变量 APP_NAME 的值
    app_name = os.getenv('APP_NAME', 'DefaultAppName')  # 如果环境变量不存在，使用默认值

    # 定义要查找的目录
    order_dir = './service/order'
    operate_dir = './service/operate'

    # 初始化返回体
    response = {
        "app_name": app_name,
        "orders": [],
        "operates": []
    }

    # 序列化函数（只用于 jsonify）
    def serialize_params_definition(params_def):
        result = {}
        for key, value in params_def.items():
            result[key] = value.copy()
            if isinstance(result[key].get("type"), type):
                result[key]["type"] = result[key]["type"].__name__
        return result

    # 辅助函数：从文件中提取 PARAMS_DEFINITION
    # noinspection PyShadowingNames
    def extract_params_definition(file_path):
        spec = importlib.util.spec_from_file_location("module.name", file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return getattr(module, 'PARAMS_DEFINITION', {})
    
    # 辅助函数：从文件中提取 REMARK
    # noinspection PyShadowingNames
    def extract_remark_definition(file_path):
        spec = importlib.util.spec_from_file_location("module.name", file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return getattr(module, 'REMARK', '')

    # 遍历 /service/order 目录下的 .py 文件
    if os.path.exists(order_dir):
        for file in os.listdir(order_dir):
            if file.endswith('.py'):
                file_name = file[:-3]  # 去掉 .py 后缀
                file_path = os.path.join(order_dir, file)
                params_definition = extract_params_definition(file_path)
                params_definition = serialize_params_definition(params_definition)
                remark=extract_remark_definition(file_path)
                response["orders"].append({
                    "name": file_name,
                    "params": params_definition,
                    "remark":remark
                })

    # 遍历 /service/operate 目录下的 .py 文件
    if os.path.exists(operate_dir):
        for file in os.listdir(operate_dir):
            if file.endswith('.py'):
                file_name = file[:-3]  # 去掉 .py 后缀
                file_path = os.path.join(operate_dir, file)
                params_definition = extract_params_definition(file_path)
                params_definition = serialize_params_definition(params_definition)
                remark=extract_remark_definition(file_path)
                response["operates"].append({
                    "name": file_name,
                    "params": params_definition,
                    "remark":remark
                })

    return jsonify(response)

# 从环境变量中获取用户名和密码
APP_USER = os.getenv('APP_USER', 'admin')  # 默认值为 admin
APP_PASSWORD = os.getenv('APP_PASSWORD', 'iqr123456')  # 默认值为 iqr123456


@app.route('/api/login', methods=['POST'])
def login():
    # 获取请求中的用户名和密码
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # 检查是否缺少必要的参数
    if not username or not password:
        return jsonify({"success": False, "detail": "缺少必要的参数"}), 400

    # 验证用户名和密码
    if username == APP_USER and password == APP_PASSWORD:
        return jsonify({"success": True, "detail": "登录成功"}), 200
    else:
        return jsonify({"success": False, "detail": "用户名或密码错误"}), 401

# 重定向根路径到 /public/web/index.html
@app.route('/')
def index():
    # 当访问根路径时，重定向到 /web/index.html
    return redirect(url_for('static', filename='/web/index.html'))

if __name__ == '__main__':
    # 获取环境变量 PORT 的值
    PORT = os.getenv('PORT', 5059)  # 如果环境变量不存在，使用默认值
    # 使用彩色打印
    if os.environ.get('WERKZEUG_RUN_MAIN') != 'true':
        logger.info(f"服务已启动,监听地址:0.0.0.0:{PORT}")
        logger.info(f"浏览器访问:http://localhost:{PORT}")
        logger.warning("退出程序:Control+C")
        # 启动调度器 （如不需要定时任务关闭此项）
        # logger.info(f"启动定时任务...")
        # scheduler.start()
        # load_tasks()

    app.run(debug=True, host='0.0.0.0', port=PORT)
