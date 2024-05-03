# luna_python Luna - 基于视觉的抗指纹爬虫第三方库



golang版本地址:https://github.com/musiclover789/luna




本版本是基于golang的版本封装的python版本;

缺点是相对于golang版本更加年轻,优点是方便比较熟悉python的开发者、如果您发现任何bug或者

本框架不太完善的地方,欢迎提出任何意见，酌情优化。但是目前python并未封装 视觉部分。






作者QQ: 80258153

技术交流群:524592021







Luna 是一款强大的第三方库，专为抗指纹自动化爬虫而设计。通过利用视觉特征和先进的算法，Luna 提供了一种有效的方法来对抗现代爬虫检测技术，保护您的网络资源免受恶意爬取和滥用。

如果您有兴趣封装其他语言的框架，您可以参考 https://github.com/musiclover789/luna_http 用http请求的方式来控制luna-抗指纹浏览器



**所有最新功能、请先参考golang版本；参数都是通用的，只是字符串而已。**

## 功能亮点



- **强大的抗指纹技术：** Luna 提供了先进的抗指纹技术，使您的爬虫程序难以被识别。

- **视觉特征解析：** 基于视觉特征的页面解析和操作，使爬虫更智能。

- **简单易用的接口：** Luna 提供简单易用的接口，轻松集成和使用它的功能。

- **智能化行为模拟：** 模拟用户行为，有效应对现代爬虫检测技术。

- **绕过检测技术：** 具备绕过常见爬虫检测技术的能力，确保您的爬虫不容易被拦截。

   [![效果展示-g](https://camo.githubusercontent.com/a926b02080b6da19138811d2b7c9cd7e9a8e527455396a7ec5aebdd71780ad26/68747470733a2f2f692e6962622e636f2f79506b5a4c64302f6d6e676769666c61622d636f6d707265737365642d32303233313032362d3231353235332d6d696e2e676966)](https://camo.githubusercontent.com/a926b02080b6da19138811d2b7c9cd7e9a8e527455396a7ec5aebdd71780ad26/68747470733a2f2f692e6962622e636f2f79506b5a4c64302f6d6e676769666c61622d636f6d707265737365642d32303233313032362d3231353235332d6d696e2e676966)

## 为什么选择 Luna

![效果展示-加载可能有些慢](https://i.ibb.co/nftHyHW/511714127971-pic.jpg)

经过大量测试，目前基本可以过掉主流抗指纹识别;

```
测试网址:
https://www.browserscan.net/
https://uutool.cn/browser/
https://abrahamjuliot.github.io/creepjs/
```



## 开始使用 Luna



详细的使用说明和示例代码，请查看本项目的[文档](https://musiclover789.github.io/lunadocs/)。

示例代码部分也可以查看源码的case包下内容。

## 抗指纹特性

- ### 目前支持指纹项:

- 所有抗指纹部分设置请直接参考golang https://github.com/musiclover789/luna 版本的设置

- golang版本的更新较快，python有些陈旧，所以不在单独写文档列举了。

- **无论您使用哪个版本、请务必用luna对应框架，否则指纹及其容易被识别，几乎作用减少30%**

  |      | 指纹项                      | 技术方案                            |      | win  | mac  |
  | ---- | --------------------------- | ----------------------------------- | ---- | ---- | ---- |
  |      | user_agent指纹              | headless模式下、也会生效            |      |      |      |
  |      | canvas指纹                  | 真实指纹库、难以识别                |      |      |      |
  |      | webgl指纹                   |                                     |      |      |      |
  |      | platform平台                |                                     |      |      |      |
  |      | timezone时区                |                                     |      |      |      |
  |      | timezone_offset时区偏移量   |                                     |      |      |      |
  |      | languages语言               | 无论是国际API、还是navigator 均生效 |      |      |      |
  |      | userAgentData               |                                     |      |      |      |
  |      | header 修改                 | 可以修改http请求协议层header        |      |      |      |
  |      | deviceMemory                |                                     |      |      |      |
  |      | hardwareConcurrency         |                                     |      |      |      |
  |      | UNMASKED_VENDOR_WEBGL       | 显卡                                |      |      |      |
  |      | UNMASKED_RENDERER_WEBGL     | 显卡                                |      |      |      |
  |      | GL_VERSION                  | 显卡                                |      |      |      |
  |      | GL_SupportedExtensions      | 显卡                                |      |      |      |
  |      | GL_VENDOR                   | 显卡                                |      |      |      |
  |      | GL_RENDERER                 | 显卡                                |      |      |      |
  |      | GL_SHADING_LANGUAGE_VERSION | 显卡                                |      |      |      |
  |      | 是否webdriver               | 已处理                              |      |      |      |
  |      | 是否brave                   | 已处理                              |      |      |      |
  |      | 是否selenium                | 已处理                              |      |      |      |
  |      | 是否来自于真实键盘          | 已处理                              |      |      |      |
  |      | 是否来自于真实鼠标          | 已处理                              |      |      |      |
  |      | 鼠标移动轨迹                | 已处理                              |      |      |      |
  |      | 其他机器人检测              | 已处理                              |      |      |      |
  |      | webRTC                      | 可以自行设置出口ip                  |      |      |      |
  |      | screen                      | 已处理                              |      |      |      |
  |      | 声卡指纹                    | 0-1000任意整数                      |      |      |      |
  |      | 屏幕触点数量                | 手机端需要，其他并不需要            |      |      |      |
  |      | 语音合成器                  | 支持自定义                          |      |      |      |

理论上，Luna 可以成功对抗这些指纹技术，使您的爬虫在操作时不容易被识别。更多详细信息请查看我们的[文档](https://musiclover789.github.io/lunadocs/)。

## Luna浏览器部分



目前，我们已经将浏览器文件上传到 百度 网盘，并提供了下载链接：

老版本-win-[2GB]链接: https://pan.baidu.com/s/14EZw9DvCtO998LOwo_epvA 提取码: mm6s

新版本-win-[670MB]连接:链接：https://pan.baidu.com/s/1S3ZdbFHTtaZgW2dInc6JDA 提取码：3pmd

Mac-arm版[114MB]:链接: https://pan.baidu.com/s/1au226sENM5XcoB7SPhEYZA 提取码: lbfs

<Mac版本仅供开发测试使用，部分抗指纹功能不可用，方便Mac开发人员进行开发-完全免费-无限制>

<win版本-没有授权文件的用户,仅可以测试useragent指纹部分,其他指纹不会生效>

如果不是历史原因、请不要使用老版本；

如何获取授权文件联系作者获取;



## 快速入门



```
import time

import devtools.browser as luna
import devtools.page as page
import common.server_management as init

"""
这是一个简单的案例
测试目的:希望你可以正常打开指纹浏览器、并且打开一个网址
"""


def main():
    """
            因为python版本、其实是我的golang版本的http协议方式封装
            也就是封装了可执行程序
            所以这个会自动找寻对应的 可执行程序、也就是一个web服务器;
            所以这个是必须要的;至于是否传入端口的区别是，一个你指定，你不写他就选随机未占用端口。
        """
    if not init.start(9876):
        print("启动服务-失败")

    """
        chromium_path 是必须要传入的参数、就是你抗指纹浏览器所在的路径 如c:\\Default\\chrome.exe        
    """
    chromium_path = "c:\\Default\\chrome.exe"
    """
        new_browser 打开浏览器
    """
    chrome_id = luna.new_browser(chromium_path)
    time.sleep(1)
    """
          new_browser 打开网址;chrome_id 代表的是你准备在哪个浏览器打开网址;
      """
    page_id = page.open_page(chrome_id, "http://www.baidu.com")
    time.sleep(5)
    html = page.get_html(page_id)
    print("网页内容大小是:", len(html))
    page.close_page(page_id)
    # 关闭浏览器
    print("关闭浏览器", luna.close_browser(chrome_id))


if __name__ == "__main__":
    main()
```



## 特点





## 基于视觉的操作



Luna 基于视觉的页面操作方法让您可以使用截图的方式来控制浏览器，也支持传统的 CSS 和 XPath 选择器等方式。这意味着您可以立即看到页面上的内容并执行操作，而不必等待特定事件触发。

这一特性的最大优势在于速度，因为您可以像人一样看到什么就可以操作什么。这样的交互方式使得 Luna 极为高效。

## 代理 IP 多样性



Luna 支持市面上所有类型的代理 IP，包括 HTTP、HTTPS 和 SOCKS5，无论代理 IP 是否需要密码，Luna 都完全兼容。理论上，使用 Luna 进行爬取的请求将无法被追踪。

## 多进程和多线程



Luna 考虑到了多进程和多线程的应用场景，使得您可以并发执行多个任务，提高了爬虫的效率。

## 网络数据包过滤



Luna 考虑到了、可能会协议和浏览器混编的方式、和可能的协议采集需求,所以继承了比较完备的cookie方案，和数据包过滤方案、方便采集数据使用、已经封装了比较完善的 一对一 请求过滤。

- 另外、鼠标移动轨迹、键盘输入、鼠标滚轮、如果没有luna浏览器配合、那么依然会被轻易识别。

如果您有技术方便问题、或者bug反馈、欢迎反馈!

------

代码调用抗指纹部分示例，最好您参考文档里面的详细内容，这里仅黏贴一部分代码，提供参考。

## 

```
import time

import devtools.browser as luna
import devtools.page as page
import common.server_management as init

"""
测试目的:希望你可以正常使用指纹
"""


def main():
    """
    start函数是启动 服务、你可以选择传入参数;就是端口号、你也可以不传入、如果你不传入 程序会自动选择一个未被占用的端口。
    如果你不清楚他有什么用、可以不予理睬
    """
    if not init.start(9876):
        print("启动服务-失败")

    """
        chromium_path 是必须要传入的参数、就是你抗指纹浏览器所在的路径 如 c:\\luna\\Default\\chrome.exe
    """
    chromium_path = "/Users/hongyuji/Documents/workspace/golang/Chromium.app/Contents/MacOS/Chromium"

    args = [
        "--luna_user_agent=Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
        "--luna_platform=win64",
        "--luna_languages=en-GB",
        "--luna_deviceMemory=8",
        "--luna_UNMASKED_VENDOR_WEBGL=Intel Corporation",
        "--luna_UNMASKED_RENDERER_WEBGL=Intel(R) UHD Graphics 620",
        "--luna_GL_VERSION=WebGL 1.0 (OpenGL ES 3.0 Intel(R) UHD Graphics 620)",
        # 仅是示例、更多指纹设置参考luna golang版本文档-都是一样的
    ]  # 示例指纹列表,

    chrome_id = luna.new_browser(chromium_path, fingerprint=args)

    time.sleep(1)

    page_id = page.open_page(chrome_id, "http://www.baidu.com")

    print("便于您查看指纹、暂停1分钟")
    time.sleep(60)

    page.close_page(page_id)
    # 关闭浏览器
    print("关闭浏览器", luna.close_browser(chrome_id))


if __name__ == "__main__":
    main()
```



#### 常见问题回复



1、可以自己随便修改指纹吗？

答：是的

2、目前支持Linux 系统 or 苹果m1,m2芯片吗？

答:暂时不支持、

3、有http协议版本吗？

答：有

4、有体积更小的浏览器么？

答：无、本身就是抗指纹的，如果精简版 不利于抗指纹。

5、为什么我测试基于视觉时候发现，出现bug

答：下载代码后不要修我的项目名字

6、第三封库可以用的么，如Selenium Pyppeteer Playwright 。

答：不再支持任何第三方框架，经过大量测试，发现第三方框架 极度容易被识别。

7、我没有找到如何类似xpath cssselecter选择器。

答：参考如下代码

```
import time

import devtools.browser as luna
import devtools.page as page
import devtools.script as js
import common.server_management as init


def main():
    # 我建议他自己随便选用一个未被占用的端口
    if not init.start():
        print("启动服务-失败")
    # 设置要传递给 make_http_request 函数的参数
    chromiumPath = "/Chromium.app/Contents/MacOS/Chromium"
    CachePath = "/golang/cache/"
    ImgPath = ""
    Headless = False
    ProxyStr = ""
    Fingerprint = ["--luna_cavans_random_str=B3B4", "--luna_hardwareConcurrency=16"]  # 示例指纹列表
    windowSize = luna.WindowSize(width=1024, height=768)  # 示例窗口大小

    # 调用 make_http_request 函数
    chrome_id = luna.new_browser(chromiumPath, CachePath, ImgPath, Headless, ProxyStr, Fingerprint, windowSize)
    # 检查返回结果
    if chrome_id:
        print("Chrome ID:", chrome_id)
    else:
        print("Failed to create new browser.")
    print("chrome_id:", chrome_id)
    page_id = page.open_page(chrome_id, "http://www.baidu.com")
    page.set_cookie(page_id, "abk", "1jsk", ".baidu.com")
    print(page.get_cookie(page_id, "http://www.baidu.com"))
    # print(page.get_html(page_id))
    time.sleep(3)
    page.run_js(page_id, js.show_mouse_position())
    print(page.get_currentURL(page_id))
    for node in page.get_all_child_element_by_css(page_id, "#form > span.bg.s_ipt_wr.new-pmd.quickdelete-wrap"):
        print("Node Type:", node.NodeType)
        print("Node Name:", node.NodeName)
        print("Node Value:", node.NodeValue)
        print("Text Content:", node.TextContent)
        print("HTML Content:", node.HTMLContent)
        print("CSS Selector:", node.CSSSelector)
        print("XPath Selector:", node.XPathSelector)
        print("-----------------------------------")
    ka = page.get_element_by_css(page_id, "#form > span.bg.s_ipt_wr.new-pmd.quickdelete-wrap")
    print(ka.CSSSelector, ka.XPathSelector)
    position = page.simulate_mouse_move_to_element(page_id, "#kw")
    print(position, ">>>>")
    if position is not None:
        x, y = position
        # page.simulate_mouse_move_to_target(page_id, x, y)
        page.simulate_mouse_click(page_id, x, y)
        time.sleep(1)
        page.simulate_keyboard(page_id, "123123")
        page.simulate_mouse_move_on_page(page_id, x, y, 100, 100)
        time.sleep(5)
        ##page > div > strong > span
        page.simulate_scroll_to_element(page_id, "#page > div > strong > span")
        page.simulate_drag(page_id, 100, 100, 500, 500)
        page.upload_files(page_id, "#page > div > strong > span")
    else:
        print("获取元素位置失败。")
    time.sleep(5)
    page.close_page(page_id)
    # 关闭浏览器
    print(">>>>>", luna.close_browser(chrome_id))


if __name__ == "__main__":
    main()
```



8、如何操作cookie、文档中我并没有找到

答：参考如下代码

```
import time

import devtools.browser as luna
import devtools.page as page
import devtools.script as js
import common.server_management as init


def main():
    if not init.start():
        print("启动服务-失败")

    chromiumPath = "/Users/hongyuji/Documents/workspace/golang/Chromium.app/Contents/MacOS/Chromium"

    windowSize = luna.WindowSize(width=1024, height=768)  # 示例窗口大小
    # 调用 make_http_request 函数
    chrome_id = luna.new_browser(chromiumPath, window_size=windowSize)
    # 检查返回结果
    time.sleep(1)

    page_id = page.open_page(chrome_id, "http://www.baidu.com")

    page.set_cookie(page_id, "abk", "1jsk", ".baidu.com")

    cookies = page.get_cookie(page_id, "http://www.baidu.com")

    print("获取到到cookies:", cookies)
    time.sleep(3)
    page.run_js(page_id, js.show_mouse_position())
    print("当前的url是", page.get_currentURL(page_id))
    time.sleep(10)
    page.close_page(page_id)
    luna.close_browser(chrome_id)


if __name__ == "__main__":
    main()
```



更多案例：直接参考源码的case包里面案例;<非付费用户，只能测试useragent 部分效果> 如需授权 联系作者QQ: 80258153
