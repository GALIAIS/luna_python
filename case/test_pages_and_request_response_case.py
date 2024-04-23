from common.event_subscriber import start_event_server, SubscriptionHandler
import devtools.browser as luna
import devtools.page as page
from common.kill_process import kill_process
import time
import common.server_management as init

"""
测试
"""


def main():
    """
        # 启动订阅服务器;
        #只有需要监听网络请求数据包时才需要使用、实现逻辑是;本地启动一个订阅服务器,
        #当有请求数据包的时候，会发送到这个订阅服务器，通过自定义custom_handler_post函数来接收-数据;
    """
    event_port = 9888
    start_event_server(event_port)

    print("-------?------")
    # 测试时 为了防止干扰、关闭其他chromium进程。
    kill_process()
    time.sleep(5)

    if not init.start(9876):
        print("启动服务-失败")

    """
        chromium_path 是必须要传入的参数、就是你抗指纹浏览器所在的路径 如 c:\\luna\\Default\\chrome.exe
    """
    chromium_path = "/Users/hongyuji/Documents/workspace/golang/Chromium.app/Contents/MacOS/Chromium"
    """
        new_browser 打开浏览器
    """
    chrome_id = luna.new_browser(chromium_path)

    """
          new_browser 打开网址;chrome_id 代表的是你准备在哪个浏览器打开网址;
    """
    ##aaa只是个事件名称，叫什么无所谓，用于区别其他订阅事件的
    event_name = "aaa"
    page.open_page(chrome_id, "http://www.baidu.com")
    page.open_page(chrome_id, "http://www.baidu.com")
    # 调用get_pages函数获取page_id数组
    time.sleep(3)
    page_ids = page.get_pages(chrome_id)

    # 判断page_ids是否为None
    if page_ids is not None:
        # 循环打印数组中的每个元素
        for page_id in page_ids:
            # 监听哪个无所谓、但是同一时间，只能监听一个；
            # 原理、他会短暂关闭网络监听、并且刷新你给定的页面、然后开启网络监听、然后开始发数据包给python、然后在推送给你注册的函数里面
            page.listen_network(chrome_id, page_id, event_port, event_name)
            break

    else:
        print("获取page_id数组失败")
    """
    订阅# 这个是一个自定义的函数custom_handler_post;函数data就是返回的response request responsebody数据
    """

    def custom_handler_post(data):
        print(f"Custom handler received data post : {data}")

    SubscriptionHandler.subscribe(event_name, custom_handler_post, 'POST')
    """
       订阅-end
       """
    time.sleep(60)
    # 关闭浏览器
    print("关闭浏览器", luna.close_browser(chrome_id))


if __name__ == "__main__":
    main()
