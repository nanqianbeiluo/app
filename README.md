<!--
 * @Author: Mr_Yao 2316718372@qq.com
 * @Date: 2025-04-18 16:03:29
 * @LastEditors: Mr_Yao 2316718372@qq.com
 * @LastEditTime: 2025-04-21 10:08:19
 * @FilePath: /py_device_test_backend/README.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->

# 介绍

🤔 一款适合对接智科特实验室智慧中台的 Python 工程性框架，已经实现了状态、参数、定时任务的管理，简化了技能、操作的声明和基本配置。

---

# 快速开始

## 1️⃣ 下载代码到本地

```bash
git clone https://iqr.coding.net/p/labbrain/d/py_device_test_backend/git/tree/main
cd py_device_test_backend
```

## 2️⃣ （可选）创建虚拟环境（推荐）

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3️⃣ 安装依赖

```bash
pip install -r requirements.txt
```

## 4️⃣ 启动项目

```bash
python app.py
```

---

## ✅ 控制台成功日志

```
2025-04-17 20:58:50 - INFO - 服务已启动,监听地址:0.0.0.0:5059
2025-04-17 20:58:50 - INFO - 浏览器访问:http://localhost:5059
2025-04-17 20:58:50 - WARNING - 退出程序:Control+C
 * Serving Flask app 'app'
 * Debug mode: off
```

---

# 📂 项目结构说明

```text
py_device_test_backend/
├── .env                     # 环境变量配置文件
├── app.py                  # 主程序入口
├── controllers/            # 执行器方法
├── logs/                   # 日志存储
├── public/                 # 静态资源目录
│   ├── assets/             # 前端资源，如图片、样式等
│   └── web/                # 页面接口或可视化模块
├── scheduled/              # 定时任务调度
│   └── task1.py            # 示例定时任务
├── service/                # 主服务模块
│   ├── operate/            # 操作服务
│   └── order/              # 技能服务
├── test/                   # 测试目录
│   └── demo.py             # 示例测试脚本
├── utils/                  # 工具类服务
│   ├── __init__.py
│   ├── equ_logger.py       # 设备日志封装
│   ├── logger.py           # 日志工具类
│   ├── params.py           # 参数管理
│   ├── state.py            # 状态管理
│   └── validate.py         # 参数校验
├── .gitignore              # Git 忽略配置
├── README.md               # 项目说明文档
└── requirements.txt        # Python 依赖列表
```

[详细使用说明文档](https://iqrobot.yuque.com/org-wiki-iqrobot-srfpgh/ap5lnu/gbnoed856kz34bgl)
