import requests
import time
from .sign import sign_request, create_session_id, sign_im
from .crypto import get_machine_code
from .im import AutoWxIm
from .request import Request
import asyncio


class AutoWxSdk:
    def __init__(self, client_type, appid: str, secret: str, base_url: str):
        self._client_type = client_type
        self._appid = appid
        self._secret = secret
        self._base_url = base_url
        self._machine_code = get_machine_code()

        self.im = AutoWxIm(self._client_type, base_url, appid, secret, '/socket-io')
        self.request = Request(base_url, appid, secret)

    def test_task(self):
        print('--> start-test-task')
        asyncio.run(self._mocker_test_task())
        print('<-- end-test-task')

    async def _mocker_test_task(self):
        url = "/api/wb-mocker/test-task"
        event = asyncio.Event()
        task_key = create_session_id()
        # im是否已经收到了task
        is_im_received_task = False

        def on_test_task(data):
            if data['taskKey'] != task_key:
                print(data['taskKey'], task_key)
                return

            # 修改外部is_im_received_task的值为True
            nonlocal is_im_received_task
            is_im_received_task = True

            event.set()
            self.im.event.off('task', on_test_task)

        self.im.event.on('task', on_test_task)
        res_request = self.request.post(url, {'taskKey': task_key})

        if res_request['code']:
            return [False, res_request['message']]

        # todo request请求完成之前im就已经收到了
        if is_im_received_task:
            return [True, "Success!"]

        # 如果超过10秒还没收到im的回调则直接结束

        await event.wait()
        return [True, "Success!"]

    def ping(self):
        url = "/api/wb-mocker/ping"
        return self.request.post(url)

    def mocker_test_im(self):
        url = "/api/wb-mocker/test-im"
        return self.request.post(url)

    def connect_im(self):
        self.im.connect()

    def on_task(self, callback):
        self.im.on_task(callback)

    def on_task_result(self, callback):
        self.im.on_task_result(callback)
