"""
关于一些常用的辅助函数
"""

import os
import time
import requests
from requests.adapters import HTTPAdapter
module_path = os.path.dirname(__file__)  # needed because sample data files are located in the same folder

import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    # filename='/home/URL/client/test_log.log',
                    # filemode='a',
                    )

def remove_nan_string(li):
    """移去列表中的 ''

    :param li:
    :return:

    Examples
    --------
    demo = ['元器件', '', '', '电感', 'l4', '', '4*4mm']
    print(remove_nan_string(demo))
    >>>  ['元器件', '电感', 'l4', '4*4mm']
    """
    return [x for x in li if x!='']


def datapath(fname):
    """
    方便加载路径
    :param fname:
    :return:
    """
    return os.path.join(module_path, fname)


def cal_time(func):
    """
    计时装饰器

    :param func:
    :return:
    """

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print(f'{func.__name__} running time：{t2 - t1}secs')
        return result
    return wrapper


def requests_get(url, headers=None, timeout=10, times=3):
    """
    参考：https://www.cnblogs.com/suguangti/p/11950185.html
    对传进来的url 进行 requests get 请求
    :param times:
    :param url:
    :param timeout: 超时重试时间
    :return: 
    """
    s = requests.Session()
    s.mount('http://', HTTPAdapter(max_retries=times))
    s.mount('https://', HTTPAdapter(max_retries=times))

    print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} 请求：{url}...")
    r = ''
    try:
        r = s.get(url, headers=headers, timeout=timeout)
        # print(r.text)
    except requests.exceptions.RequestException as e:
        print(e)
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} 请求完毕...")
    return r

