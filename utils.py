import os
import sys
from typing import Optional


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

    # 检查图片文件是否存在
    if not os.path.exists(image_path):
        # 如果图片文件不存在，则返回一个空图片的路径
        empty_image_path = os.path.join(base_path, 'tsl_images/general/icon_load_fail.png')
        return empty_image_path

    return image_path