
import logging
import requests
from solaredge_interface import __http_request_user_agent__ as USER_AGENT
from solaredge_interface import __http_request_timeout__ as REQUESTS_TIMEOUT


logger = logging.getLogger(__name__)


class Response(object):
    url = request = headers = cookies = status_code = elapsed = text = None

    def __init__(self, **attrs):
        for k in attrs:
            setattr(self, k, attrs[k])

    def __str__(self):
        if not hasattr(self, 'text'):
            return None
        return str(self.text)

    def __set__(self, name, value):
        setattr(self, name, value)


def http_request(url, params=None, headers=None, timeout=REQUESTS_TIMEOUT):

    if type(params) is dict:
        for key in params:
            if type(params[key]) is list:
                params[key] = ','.join(str(params[key]).strip(' '))
            params[key] = str(params[key]).strip(' ')

    if type(headers) is dict:
        headers['user-agent'] = USER_AGENT
    else:
        headers = {'user-agent': USER_AGENT}

    r = requests.get(url, params=params, headers=headers, timeout=timeout)

    response = Response(
        url=r.url,
        request=r.request,
        headers=r.headers,
        cookies=r.cookies,
        status_code=r.status_code,
        text=r.text,
        elapsed=r.elapsed,
    )
    logger.debug('http-response; url={}'.format(r.url))
    logger.debug('http-response; http-status={}'.format(r.status_code))
    return response
