# coding=gbk         #说明对应的编码格式，不然容易报错
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
    # 在消息列表计数内循环，以防遗漏或过度处理消息，以最后一条消息开始对比，直至和
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



