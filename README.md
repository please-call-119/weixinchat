<!-- wp:paragraph {"fontSize":"medium"} -->
<p class="has-medium-font-size"><strong>简介：博客地址https://www.liujunwu.cn/wordpress/?p=293</strong></p></strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>自动转发微信的消息，也可以用作微信消息发送来使用，可考虑后续结合<a href="https://www.liujunwu.cn/wordpress/?p=293"><strong>同花顺自动交易模块</strong></a>来实现交易信息及时通知，目前还未结合，待后续有时间更新</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>思路：</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>使用pywinauto模块（其实国内也有类似的库，叫<a href="https://github.com/yinkaisheng/Python-UIAutomation-for-Windows"><strong>uiautomation</strong></a>，我测试下来感觉更高效，但是没有什么资料）操作句柄，<strong><span class="has-inline-color has-luminous-vivid-orange-color">如要转载请标明来源</span></strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>工具：</strong></p>
<!-- /wp:paragraph -->

<!-- wp:preformatted -->
<pre id="block-687cf51d-5fa4-4ae8-ae2e-063b6e16f850" class="wp-block-preformatted">pycharm
anaconda（虽然有些臃肿，但是我们并不是要成为专业开发者，一切以便利和可复用为导向</pre>
<!-- /wp:preformatted -->

<!-- wp:paragraph -->
<p><strong>环境：</strong></p>
<!-- /wp:paragraph -->

<!-- wp:preformatted -->
<pre id="block-0d62f4de-9663-411b-88f1-1d5ef42eb1a7" class="wp-block-preformatted">Python3.9.7
pywin32-300（最新版本应该是302，但是会出现找不到模块的错误，最好更换成300或者之前的版本）
pywinauto0.6.8 </pre>
<!-- /wp:preformatted -->

<!-- wp:paragraph -->
<p><strong>环境安装：</strong>（如果不会使用anaconda控制台，建议先百度教程看看，后续我也会写anaconda一些简单操作）</p>
<!-- /wp:paragraph -->

<!-- wp:preformatted -->
<pre id="block-2146a025-5c8e-4c9a-95bd-0c9800bf99d0" class="wp-block-preformatted">conda环境安装：
pip install --upgrade pywin32==300 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install pywinauto -i https://pypi.tuna.tsinghua.edu.cn/simple</pre>
<!-- /wp:preformatted -->

<!-- wp:paragraph -->
<p><strong>项目地址：</strong><a href="https://github.com/please-call-119/weixinchat">GitHub</a></p>
<!-- /wp:paragraph -->

<!-- wp:syntaxhighlighter/code -->
<pre class="wp-block-syntaxhighlighter-code"># coding=gbk         #说明对应的编码格式，不然容易报错
# 导入模块
import time
from pywinauto import Application

# 微信程序路径
exe_path = r'C:\Program Files (x86)\Tencent\WeChat'

# 定义Weixin_News类
class Weixin_News:
    # 连接微信程序，参数：程序路径
    def __init__(self,exe_path):
        self.app = Application(backend="uia").connect(path=exe_path)

    # 消息获取函数
    def get(self):
        # 连接到群消息窗口
        news_win = self.app['群消息']
        # 定位到消息列表
        news_list=news_win.child_window(title="消息", control_type="List")
        # 把列表控件打包成字典类型并返回
        news=news_list.items()
        return news

    # 消息发送函数，参数：消息（字符串类型）
    def send(self,news):
        # 连接到接收方窗口
        send_win=self.app['接收方']
        # 定位到消息编辑框
        edit_win=send_win.child_window(title="输入", control_type="Edit")
        # 输入要转发的消息
        edit_win.type_keys(news)
        time.sleep(1)
        # 定位发送按钮
        enter_butter=send_win.child_window(title="sendBtn", control_type="Button")
        # 点击发送
        enter_butter.click_input()
        time.sleep(1)

    # 对获取的消息进行预处理，参数：列表消息（字典类型）
    def cut_news(self,news):
        #把字典进行切割，处理掉多余的字符并转为字符串格式，返回消息
        msg = str(news).split('\'')
        mag = msg.pop(0)
        mag = msg.pop(-1)
        msg = str(msg)
        msg = msg.strip('[\'')
        msg = msg.strip('\']')
        return msg

# 实例化Weixin_News类型
a=Weixin_News(exe_path)
# 获得消息列表，以此时的消息列表作为对照组
msg= a.get()
print('对照已获得')
# 获得消息计数
msg_count=len(msg)
time.sleep(10)
# 循环47次
for numb in range(1,48):
    # 在消息列表计数内循环，以防遗漏或过度处理消息，以最后一条消息开始对比，直至对照消息组和实验组消息相同
    for num in range(-1, -msg_count, -1):
        # 调用消息获取函数，得到实验组（也就是最新的消息列表）
        experiment = a.get()
        # 把现在获得的实验组第num条消息（一开始是-1）与之前的对照组最后一条消息进行对比，如果相同则没有新消息，直接跳出此次循环
        if experiment[num] == msg[-1]:
            print('相同')
            break
        # 如果不同则进行消息剪切，进行转发操作
        else:
            n = a.cut_news(experiment[num])
            a.send(n)
    # 把实验组设置成下次对比的对照组
    msg=experiment
    print('第【%s】次循环结束，休眠中，半小时后启动下次刷新' % numb)
    # 停顿半小时，再进行下次循环
    time.sleep(1800)
</pre>
<!-- /wp:syntaxhighlighter/code -->

<!-- wp:paragraph -->
<p></p>
<!-- /wp:paragraph -->
