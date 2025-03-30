# __init__.py：初始化文件，创建Flask应用

# 导入Flask
from flask import Flask, render_template, jsonify
from .views import blue
from .models import *

# 创建Flask应用对象
# __name__ 对应当前文件名：__init__.py
# 即app.py所在的目录就是项目目录
def create_app():
    app = Flask(__name__)

    # 注册蓝图
    app.register_blueprint(blueprint=blue)

    return app
