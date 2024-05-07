import requests
import time
from .sign import sign_request


class AutoWxSdk:
    def __init__(self, appid: str, secret: str, base_url: str):
        self._appid = appid
        self._secret = secret
        self._base_url = base_url

    # 测试密钥是否正确
    def test_secret(self):
        # 请求 /api/sdk/test
        url = "/api/sdk/test"
        method = "GET"
        timestamp = int(time.time())
        sign = self._sign_request(method, url, timestamp)
        headers = {
            "appid": self.appid,
            "timestamp": str(timestamp),
            "sign": sign
        }
        response = requests.get(f"{self._base_url}{url}", headers=headers)
        return response.json()

    def _sign_request(self, method: str, url: str, timestamp: int) -> str:
        return sign_request(self._appid, self._secret, method, url, timestamp)
