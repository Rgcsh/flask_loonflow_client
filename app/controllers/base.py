# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) rgc, 2019
# All rights reserved
# @Author: rgc
# @Time: '2019-09-12 18:06'
# sys
import traceback

# 3p
from flask_loguru import logger
from flask_restful import Api, Resource

# project
from app.utils import json_fail
from app.utils.exceptions import PPException


class BaseApi(Api):

    def handle_error(self, e):
        """ 处理异常
        """
        if isinstance(e, PPException):
            return json_fail(e.code, e.message)
        # 打印错误到控制台 和 日志
        logger.error(traceback.format_exc())

        return json_fail(500)


class BaseController(Resource):

    def get(self, *args, **kwargs):  # pylint: disable=unused-argument,no-self-use
        """ GET 方法基类
        """
        return json_fail(405)

    def post(self, *args, **kwargs):  # pylint: disable=unused-argument,no-self-use
        """ POST 方法基类
        """
        return json_fail(405)
