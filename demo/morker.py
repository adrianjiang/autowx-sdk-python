from autowx_sdk import AutoWxSdk

auto_wx = AutoWxSdk(appid="663c8411cc94cf51fce38736", secret="qP&aflsusrKf", base_url="http://localhost:5309")


pong = auto_wx.ping()
print(pong)

auto_wx.connect_im()
auto_wx.morker_test_im()
