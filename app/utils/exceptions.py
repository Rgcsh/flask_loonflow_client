# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) rgc, 2019
# All rights reserved
# @Author: rgc
# @Time: '2019-09-12 17:20'


class PPException(Exception):
    """ 项目异常基类
    """

    def __init__(self, code=500, message=None):
        super().__init__()
        self.code = code
        self.message = message


class PPApiException(PPException):
    """peppa项目的API处理时的基础异常"""

    def __init__(self, code=500, message=None):
        super().__init__(code, message)


class PPInvalidMapException(PPException):
    """ 无效的Map类型
    """


def raise_exception(response):
    """
    解析 json_fail() 并 抛出异常
    :param response:
    :return:
    """
    raise PPApiException(response.json['respCode'], response.json['respMsg'])
