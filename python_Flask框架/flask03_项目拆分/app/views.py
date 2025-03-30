
# views.py: 路由 + 视图函数

from flask import Blueprint, jsonify, render_template

# 蓝图
blue = Blueprint('user', __name__)

# 路由route + 视图函数hello_world
@blue.route('/')
def hello_world():
    # 响应：返回浏览器的数据
    return 'Hello World!'

@blue.route('/index')
def index():
    # 响应：字符串
    return "index 首页1"

@blue.route('/json')
def json():
    # 模板渲染
    # 响应：json字符串
    return jsonify({'name': '法外狂徒张三', 'age': 18})

@blue.route('/html')
def html():
    # 模板渲染
    # 响应：html模板
    return render_template('index.html', name='法外狂徒张三')


