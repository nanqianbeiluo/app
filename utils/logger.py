import logging
import os
from logging.handlers import TimedRotatingFileHandler
from colorama import init, Fore, Style # type: ignore
from datetime import datetime

# 初始化 colorama
init(autoreset=True)

# 日志颜色映射
LOG_COLORS = {
    logging.DEBUG: Fore.BLUE,
    logging.INFO: Fore.GREEN,
    logging.WARNING: Fore.YELLOW,
    logging.ERROR: Fore.RED,
    logging.CRITICAL: Fore.MAGENTA
}

# 彩色日志格式器（用于终端）
class ColorFormatter(logging.Formatter):
    def format(self, record):
        log_color = LOG_COLORS.get(record.levelno, Fore.WHITE)
        log_format = f"{log_color}%(asctime)s - %(levelname)s - %(message)s{Style.RESET_ALL}"
        formatter = logging.Formatter(log_format, datefmt="%Y-%m-%d %H:%M:%S")
        return formatter.format(record)

# 普通日志格式（用于文件）
FILE_FORMAT = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s", "%Y-%m-%d %H:%M:%S"
)

# 初始化 logger（仅初始化一次）
def configure_logger(name="my_app", log_dir="logs"):
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger  # 已初始化，直接返回

    # 日志目录不存在则创建
    os.makedirs(log_dir, exist_ok=True)

    # 日志文件名（每天一个）
    log_file = os.path.join(log_dir, f"{datetime.now().strftime('%Y-%m-%d')}.log")

    # 1. 终端输出（带颜色）
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(ColorFormatter())
    logger.addHandler(console_handler)

    # 2. 文件输出（自动按天切分，保留 30 天）
    file_handler = TimedRotatingFileHandler(
        filename=log_file,
        when="midnight",     # 每天0点切换
        backupCount=30,      # 最多保留30天
        encoding="utf-8",
        utc=False
    )
    file_handler.setFormatter(FILE_FORMAT)
    logger.addHandler(file_handler)

    # 基本设置
    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    return logger

# 全局 logger 单例
logger = configure_logger()
