# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) rgc, 2019
# All rights reserved
# @Author: rgc
# @Time: '2019-09-17 13:07'
import hashlib
import random
import time
import uuid


def get_seed(string='', length=32):
    """
    获取特定长度的随机字符串
    热点：任意两次的字符串不相同
    """
    string += str(time.time())

    uuid_str = str(uuid.uuid1()).replace("-", "")
    string += uuid_str

    sha512 = hashlib.sha512()
    sha512.update(bytes(string, encoding="utf-8"))
    string = sha512.hexdigest()

    return string[:length]


def get_random_int() -> int:
    """
    获取 2**32 -1= 4294967295 范围内的随机整数
    :return:
    """
    return random.randint(0, 2 ** 32 - 1)
