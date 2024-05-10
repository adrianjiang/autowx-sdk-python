from autowx_sdk import AutoWxSdk
import time

auto_wx = AutoWxSdk(client_type="mocker", appid="663c8411cc94cf51fce38736", secret="qP&aflsusrKf",
                    base_url="http://localhost:5309")

# pong = auto_wx.ping()
# print(pong)

auto_wx.connect_im()
# auto_wx.on_task(lambda data: print('on-task', data))
# 定时3秒
time.sleep(3)
# auto_wx.morker_test_im()

auto_wx.test_task()
