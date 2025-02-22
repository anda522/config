import logging
import datetime
import sys
import os
from pathlib import Path
from typing import Optional, Union

# 获取当前文件父目录
FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

# 既能输出到终端，又能输出到文件
def logger_init(logging_path: Optional[Union[str, Path]]=None):
    logging_file_name = f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}.log'
    if logging_path is None:
        logging_path = Path(logging_file_name)
    else:
        logging_path = Path(logging_path) / logging_file_name
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(logging_path)
    file_handler.setLevel(logging.DEBUG)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        fmt="[%(asctime)s] [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger