# 导入Flask
from flask import Flask

# 创建Flask应用对象
# __name__ 对应当地文件名：app.py
# 即app.py所在的目录就是项目目录
app = Flask(__name__)


# 路由route + 视图函数hello_world
@app.route('/')
def hello_world():
    # 响应：返回浏览器的数据
    return 'Hello World!'


# 启动方式
# 在app.py文件目录控制台，运行命令：python app.py
# 主函数
if __name__ == '__main__':
    # 启动服务器
    app.run()
