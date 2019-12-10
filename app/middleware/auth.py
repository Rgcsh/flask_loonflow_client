# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) rgc, 2019
# All rights reserved
# @Author: rgc
# @Time: '2019-09-25 13:50'
# 3p

# project
from .base import BaseMiddleWare


class AuthMiddleWare(BaseMiddleWare):

    @staticmethod
    def before_request():  # pylint: disable=inconsistent-return-statements
        """ 检查用户权限
        """
        # white_list = current_app.config.get("AUTH_WHITE_LIST", [''])
        #
        # # 不在白名单中的接口，用户又没有登录，则禁止访问
        # if not hasattr(g, "account") and request.path not in white_list:
        #     logger.info("用户没有登录，不具备访问权限")
        #     return json_fail(403)
        #
        # if request.path not in white_list and not request.path.startswith("/sso") and\
        #         10044 not in g.account["access_list"]:
        #     logger.info("用户没有10044权限，禁止访问")
        #     return json_fail(403)
        pass
