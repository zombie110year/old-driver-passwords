import pkgutil
from pathlib import Path
from typing import List

from . import DICTIONARY, DATABASE


def pkg_dictionary() -> List[str]:
    """获得包内 dictionary 的内容
    """
    raw = pkgutil.get_data(__package__, "resource/dictionary.txt")
    text = raw.decode("utf-8").strip("\n")
    passwords = text.split("\n")
    return passwords

def dictionary() -> List[str]:
    """获取用户数据中 dictionary 的内容
    """
    text = Path(DICTIONARY).read_text("utf-8").strip("\n")
    passwords = text.split("\n")
    return passwords

def database_file() -> str:
    """获取用户数据目录中的 SQLite 数据库路径
    """
    return DATABASE