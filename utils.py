import os
import sys
from typing import Optional
from PIL import Image


def get_image_path(filename):
    """
    根据程序是否打包获取图片的路径
    :param filename:
    :return:
    """
    if getattr(sys, 'frozen', False):  # 检查程序是否已被打包
        # 如果程序已被打包，获取打包后的可执行文件所在目录
        # base_path = sys._MEIPASS
        base_path: Optional[str] = getattr(sys, '_MEIPASS', None)
    else:
        # 如果程序未被打包，获取当前脚本所在目录
        base_path = os.path.abspath(os.path.dirname(__file__))

        while not os.path.exists(os.path.join(base_path, 'main.py')):
            base_path = os.path.dirname(base_path)

    # 构建图片文件的绝对路径
    image_path = os.path.join(base_path, filename)

    # 检查路径是否为有效图片
    if not is_valid_image(image_path):
        return 'path is invalid'

    return image_path

def is_valid_image(image_path: str) -> bool:
    """
    检查路径是否为有效图片。
    - 路径必须存在。
    - 文件扩展名必须是图片格式。
    - 文件内容必须可被加载为图片。
    """
    # 检查文件扩展名
    valid_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff"}
    _, ext = os.path.splitext(image_path)
    if ext.lower() not in valid_extensions:
        return False

    # 检查文件是否存在
    if not os.path.isfile(image_path):
        return False

    # 尝试加载图片
    try:
        with Image.open(image_path) as img:
            img.verify()  # 验证图片内容
        return True
    except Exception:
        return False