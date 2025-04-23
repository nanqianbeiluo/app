import time
from utils.logger import logger

class EquManager:
    def __init__(self):
        self.equ = {
            "status": "idle",
            "message": "",  # 新增 message 字段
            "fault_code": "",  # 新增 fault_code 字段
            "task": {
                "task_id": None,
                "order": None,
                "status": None,
                "detail": "",
                "result": None,
                "start_time": None,
                "over_time": None,
                "run_time": 0
            },
        }

    def get(self):
        self.calculate_run_time()
        return self.equ

    def set(self, modify_function):
        if not callable(modify_function):
            raise ValueError("modify_function must be a callable function")
        try:
            modified_data = modify_function(self.equ)
            self.validate_state(modified_data)
            self.equ = modified_data
            logger.info(f"State updated: {self.equ}")
            return modified_data
        except Exception as e:
            logger.error(f"Error updating state: {e}")
            raise e

    def validate_state(self, state):
        valid_status = ["idle", "busy", "failed"]
        valid_task_status = ["success", "running", "pass", "failed", "default"]

        if state["status"] not in valid_status:
            raise ValueError(f"Invalid status: {state['status']}")
        if state["task"]["status"] not in valid_task_status:
            raise ValueError(f"Invalid task status: {state['task']['status']}")

    def calculate_run_time(self):
        if self.equ["task"]["start_time"] is not None:
            if self.equ["task"]["over_time"] is not None:
                self.equ["task"]["run_time"] = self.equ["task"]["over_time"] - self.equ["task"]["start_time"]
            else:
                self.equ["task"]["run_time"] = time.time() - self.equ["task"]["start_time"]
        else:
            self.equ["task"]["run_time"] = 0

    def add_detail(self, detail=None, level="info"):
        """添加 detail，并记录对应等级日志"""
        if not detail:
            detail = "运行中..."
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        log_line = f"{timestamp} - {level.upper()} - {detail}\n"
        self.equ["task"]["detail"] += log_line
        log_func = getattr(logger, level, logger.info)
        log_func(f"{self.equ['task']['task_id']}-{self.equ['task']['order']}: {detail}")

    def set_equ_status(self, status, message="", fault_code=""):
        """设置 equ 的状态，并更新 message 和 fault_code"""
        self.equ["status"] = status or self.equ["status"]
        self.equ["message"] = message or self.equ["message"]
        self.equ["fault_code"] = fault_code or self.equ["fault_code"]
        logger.info(f"Status updated: {status}, Message: {message}, Fault Code: {fault_code}")

    def running(self, data):
        if data:
            self.equ["task"]["task_id"] = data.get("task_id")
            self.equ["task"]["order"] = data.get("order")
            self.equ["task"]["status"] = "running"
            self.equ["task"]["result"] = None
            self.equ["task"]["detail"] = ""
            self.equ["task"]["start_time"] = time.time()
            self.equ["task"]["over_time"] = None
            self.add_detail("任务开始运行", level="info")
        self.set_equ_status("busy")

    def success(self, detail=None, result=True):
        self.set_equ_status("idle")
        self.equ["task"]["status"] = "success"
        self.equ["task"]["result"] = result
        self.equ["task"]["over_time"] = time.time()
        self.calculate_run_time()
        self.add_detail(detail or "运行成功", level="info")

    def default(self, detail=None, result=True):
        self.set_equ_status("idle")
        self.equ["task"]["status"] = "default"
        self.equ["task"]["result"] = result
        self.equ["task"]["over_time"] = time.time()
        self.calculate_run_time()
        self.add_detail(detail or "默认处理完成", level="info")

    def pass_(self, detail=None, result=True):
        self.set_equ_status("idle")
        self.equ["task"]["status"] = "pass"
        self.equ["task"]["result"] = result
        self.equ["task"]["over_time"] = time.time()
        self.calculate_run_time()
        self.add_detail(detail or "跳过本次执行", level="warning")

    def failed(self, detail=None, result=False,code="1101"):
        self.set_equ_status("failed", message=detail or "运行错误", fault_code=code)
        self.equ["task"]["status"] = "failed"
        self.equ["task"]["result"] = result
        self.equ["task"]["over_time"] = time.time()
        self.calculate_run_time()
        self.add_detail(detail or "运行错误", level="error")

    def reset(self):
        self.equ = {
            "status": "idle",
            "message": "",
            "fault_code": "",
            "task": {
                "task_id": None,
                "order": None,
                "status": None,
                "detail": "",
                "result": None,
                "start_time": None,
                "over_time": None,
                "run_time": 0
            },
        }
        logger.info("State reset to initial value")

# 创建全局实例
equ_manager = EquManager()