# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) rgc, 2019
# All rights reserved
# @Author: rgc
# @Time: '2019-09-25 13:49'
from .auth import AuthMiddleWare
from .log import LogMiddleWare

# 中间件
MIDDLEWARE = [
    AuthMiddleWare,
    LogMiddleWare,
]
