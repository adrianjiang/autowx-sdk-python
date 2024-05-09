import requests
import time
from .sign import sign_request
from .crypto import get_machine_code
from .im import sio


class AutoWxSdk:
    def __init__(self, appid: str, secret: str, base_url: str):
        self._appid = appid
        self._secret = secret
        self._base_url = base_url
        self._machine_code = get_machine_code()

    def test_task(self):
        url = "/api/wb-sdk/test-task"
        method = "POST"
        timestamp = int(time.time())
        sign = self._sign_request(method, url, timestamp)
        headers = {
            "appid": self.appid,
            "timestamp": str(timestamp),
            "sign": sign
        }
        response = requests.get(f"{self._base_url}{url}", headers=headers)
        return response.json()

    def ping(self):
        url = "/api/wb-morker/ping"
        method = "POST"
        timestamp = int(time.time() * 1000)
        sign = self._sign_request(method, url, timestamp)
        headers = {
            "appid": self._appid,
            "timestamp": str(timestamp),
            "machine_code": self._machine_code,
            "sign": sign,
        }
        response = requests.post(f"{self._base_url}{url}", headers=headers)
        print(response)
        return response.json()

    def _sign_request(self, method: str, url: str, timestamp: int) -> str:
        return sign_request(self._appid, self._secret, method, url, timestamp)

    def morker_test_im(self):
        url = "/api/wb-morker/test-im"
        method = "POST"
        timestamp = int(time.time() * 1000)
        sign = self._sign_request(method, url, timestamp)
        headers = {
            "appid": self._appid,
            "timestamp": str(timestamp),
            "machine_code": self._machine_code,
            "sign": sign,
        }
        response = requests.post(f"{self._base_url}{url}", headers=headers)
        return response.json()

    def connect_im(self):
        # 连接到 Socket.IO 服务器
        sio.connect(f"{self._base_url}/socket-io/socket.io/")

        # 在需要的时候发送消息
        # sio.emit('message', {'foo': 'bar'})
