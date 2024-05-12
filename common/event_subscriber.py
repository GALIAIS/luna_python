from bottle import Bottle, request, run
from gevent import monkey; monkey.patch_all()
import threading
import gevent.pool

class SubscriptionHandler:
    _subscriptions = {}
    _lock = threading.Lock()
    _pool = gevent.pool.Pool(1000)  # 设置一个协程池，大小为1000

    @classmethod
    def subscribe(cls, path, handler, method='GET'):
        with cls._lock:
            if path not in cls._subscriptions:
                cls._subscriptions[path] = {}
            cls._subscriptions[path][method] = handler

    @classmethod
    def notify_subscribers(cls, path, data, method='GET'):
        with cls._lock:
            if path in cls._subscriptions and method in cls._subscriptions[path]:
                subscriber_handler = cls._subscriptions[path][method]
                # 使用协程池处理通知
                cls._pool.spawn(subscriber_handler, data)


app = Bottle()

# 设置最大请求体大小为 10MB
app.max_request_size = 1024 * 1024 * 100  # 10MB

# 设置最大请求头大小为 4KB
app.max_request_header_size = 1024 * 4*100  # 4KB

@app.route('/subscribe/<path:path>', method=['POST', 'GET'])
def subscribe(path):
    def handler(data):
        print(f"Received data for path '{path}': {data}")

    if request.method == 'POST':
        SubscriptionHandler.subscribe(path, handler, 'POST')
        return f"Subscribed to path '{path}' via POST"
    else:  # GET request
        SubscriptionHandler.subscribe(path, handler)
        return f"Subscribed to path '{path}' via GET"


@app.get('/receive/<path:path>')
def receive_data_get(path):
    SubscriptionHandler.notify_subscribers(path, request.query)
    return f"Notified subscribers for path '{path}'"


@app.post('/receive/<path:path>')
def receive_data_post(path):
    SubscriptionHandler.notify_subscribers(path, request.body.read().decode('utf-8'), 'POST')
    return f"Notified subscribers for path '{path}' via POST"


def start_event_server(r_port):
    """
    启动 Bottle 服务器并等待完全启动后执行其他逻辑

    参数：
    - port: 服务器端口号
    """

    # 定义启动 Bottle 服务器的函数
    def run_server():
        run(app, host='127.0.0.1', port=r_port, server='gevent')

    # 创建一个线程来启动 Bottle 服务器
    server_thread = threading.Thread(target=run_server)
    server_thread.start()

