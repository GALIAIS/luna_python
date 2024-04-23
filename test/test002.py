# from bottle import Bottle, request, response
# import threading
#
#
# class SubscriptionHandler:
#     _subscriptions = {}
#     _lock = threading.Lock()
#
#     @classmethod
#     def subscribe(cls, path, handler, method='GET'):
#         with cls._lock:
#             if path not in cls._subscriptions:
#                 cls._subscriptions[path] = {}
#             cls._subscriptions[path][method] = handler
#
#     @classmethod
#     def notify_subscribers(cls, path, data, method='GET'):
#         with cls._lock:
#             if path in cls._subscriptions and method in cls._subscriptions[path]:
#                 cls._subscriptions[path][method](data)
#
#
# app = Bottle()
#
#
# @app.route('/subscribe/<path:path>', method=['POST', 'GET'])
# def subscribe(path):
#     def handler(data):
#         print(f"Received data for path '{path}': {data}")
#
#     if request.method == 'POST':
#         SubscriptionHandler.subscribe(path, handler, 'POST')
#         return f"Subscribed to path '{path}' via POST"
#     else:  # GET request
#         SubscriptionHandler.subscribe(path, handler)
#         return f"Subscribed to path '{path}' via GET"
#
#
# @app.get('/test/<path:path>')
# def test(path):
#     SubscriptionHandler.notify_subscribers(path, request.query)
#     return f"Notified subscribers for path '{path}'"
#
#
# @app.post('/test/<path:path>')
# def post_test(path):
#     SubscriptionHandler.notify_subscribers(path, request.body.read().decode('utf-8'), 'POST')
#     return f"Notified subscribers for path '{path}' via POST"
#
#
# def run_server():
#     app.run(host='localhost', port=8080, debug=True)
#
#
# if __name__ == "__main__":
#     server_thread = threading.Thread(target=run_server)
#     server_thread.start()
#
#
#     def custom_handler_get(data):
#         print(f"Custom handler received data get : {data}")
#
#     def custom_handler_post(data):
#         print(f"Custom handler received data post : {data}")
#
#
#     SubscriptionHandler.subscribe("test_path", custom_handler_get, 'GET')
#     SubscriptionHandler.subscribe("test_path", custom_handler_post, 'POST')
