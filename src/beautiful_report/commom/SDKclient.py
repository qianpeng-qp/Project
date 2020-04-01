import requests


class SDKclient:
    '''
    :return r
    '''
    @staticmethod
    def do_requests(url, method, data):
        if method == 'ger':
            r = requests.get(url, data=data)
        elif method == 'post':
            r = requests.post(url, data=data)
        return r
