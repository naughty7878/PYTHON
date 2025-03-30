from app import create_app

# 创建Flask应用对象
app = create_app()

# 启动方式
# 在app.py文件目录控制台，运行命令：python -m flask run
# 主函数
if __name__ == '__main__':
    # 启动服务器
    # debug 是否开启调试模式，开启后修改过python代码会自动重启
    # port 指定服务器端口，默认是5000
    # host 可访问主机，默认是127.0.0.1（只能本机访问），指定为0.0.0.0，所有IP均能访问
    app.run(host='0.0.0.0', port=5000, debug=True)
