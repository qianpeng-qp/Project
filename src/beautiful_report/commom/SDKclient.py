import requests


class SDKclient:
    '''
    对请求方法统一处理
    ：params
    :return r
    '''

    @staticmethod
    def do_requests(url, method, data=None):
        if method == 'get':
            r = requests.get(url, params=data)
        elif method == 'post':
            r = requests.post(url, params=data)
        return r
