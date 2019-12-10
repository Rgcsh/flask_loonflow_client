# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) rgc, 2019
# All rights reserved
# @Author: rgc
# @Time: '2019-09-25 13:50'


class BaseMiddleWare:

    @staticmethod
    def before_request():
        """
        请求之前的处理函数
        """

    @staticmethod
    def after_request(response):
        """
        请求处理完成之后的处理函数
        :param response: 原始响应
        :return: 响应
        """
        return response

    @staticmethod
    def teardown_request(exception):
        """
        项目崩溃的处理函数
        :param exception: 抛出的异常
        """
