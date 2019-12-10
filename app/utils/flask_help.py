# -*- coding: utf-8 -*-
"""
@Author: rgc
All rights reserved
create time '2019/9/18'
"""
import urllib.parse
from functools import wraps

from flask import request, g

from .response import json_fail


def get_user_id():
    """
    获取请求上下文 g 中 的user_id
    :return:
    """
    return g.account["user_id"]


def cache_key():
    """
    获取请求路径及参数，并转化为字符串返回；主要用在 函数根据不同参数设置缓存时使用
    :return:
    """
    args = request.args
    li = [(k, v) for k in sorted(args) for v in sorted(args.getlist(k))]
    key = request.path + '?' + urllib.parse.urlencode(li)
    return key


def get_request_username():
    """
    获取用户名
    :return:
    """
    auth = request.headers.environ['HTTP_AUTHORIZATION']
    auth_list = auth.split('.')
    if len(auth_list) >= 2:
        return auth_list[1]
    return None


def check_access_id(access_id):
    """
    检查权限
    :param role_id:
    {'access_token': 'c8e4444ec5c4aecd0e83d20b8c722c30',
         'salt': 'c0b6b50258',
         'user_id': 1,
         'role_id': 1,
         'nickname': '吴东',
         'real_name': '吴东',
         'gender': 1,
         'avatar': 'http://image.bvrft.cn/image/2019/07/24/cadfd5d71d903caa5f1d40e73424b4f5.jpeg', 'profile': '阿斯顿发11',
         'access_list': [10002, 10004, 10005, 10006, 10014, 10008, 10007, 10013, 10010, 10015, 10016, 10026, 10027, 10029,
                         10042, 10028, 10022, 10023, 10024, 10025, 10017, 10018, 10021, 10020, 10019, 10030, 10037, 10039,
                         10038, 10041, 10040, 10031, 10032, 10036, 10033, 10034, 10035, 10001],
         'mobile': '13718416506',
         'email': 'wd@bvrft.com', 'banned': 0, 'state': 1}

    :return:
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not g.account or not g.account.get("user_id"):
                return json_fail(501)

            access_list = g.account.get('access_list')
            if not access_list:
                return json_fail(502)
            if access_id not in access_list:
                return json_fail(503)
            return func(*args, **kwargs)

        return wrapper

    return decorator
