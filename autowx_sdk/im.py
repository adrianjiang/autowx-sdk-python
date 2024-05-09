import socketio

# 创建一个 Socket.IO 客户端实例
sio = socketio.Client(logger=True, engineio_logger=True)


# 连接事件处理
@sio.on('connect')
def connect():
    print("Connected to the server")


# 断开连接事件处理
@sio.on('disconnect')
def disconnect():
    print("Disconnected from the server")


# 监听自定义事件 'my_message'

@sio.on('test-im')
def task(data):
    print(f"Received task: {data}")


@sio.on('test-im')
def test_im(data):
    print(f"Received testIm: {data}")


# 监听内置的 'message' 事件
