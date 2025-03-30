# 导入Flask
from flask import Flask, render_template, jsonify

# 创建Flask应用对象
# __name__ 对应当地文件名：app.py
# 即app.py所在的目录就是项目目录
app = Flask(__name__, template_folder='templates')


# 路由route + 视图函数hello_world
@app.route('/')
def hello_world():
    # 响应：返回浏览器的数据
    return 'Hello World!'

@app.route('/index')
def index():
    # 响应：字符串
    return "index 首页"

@app.route('/json')
def json():
    # 模板渲染
    # 响应：json字符串
    return jsonify({'name': '法外狂徒张三', 'age': 18})

@app.route('/html')
def html():
    # 模板渲染
    # 响应：html模板
    return render_template('index.html', name='法外狂徒张三')




# 启动方式
# 在app.py文件目录控制台，运行命令：python -m flask run
# 主函数
if __name__ == '__main__':
    # 启动服务器
    # debug 是否开启调试模式，开启后修改过python代码会自动重启
    # port 指定服务器端口，默认是5000
    # host 可访问主机，默认是127.0.0.1（只能本机访问），指定为0.0.0.0，所有IP均能访问
    app.run(host='0.0.0.0', port=5000, debug=True)
