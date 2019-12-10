# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) rgc, 2019
# All rights reserved
# @Author: rgc
# @Time: '2019-09-16 11:39'
import datetime
import decimal
import json


class JsonEncoder(json.JSONEncoder):

    def default(self, o):  # pylint: disable=method-hidden

        # 处理datetime
        if isinstance(o, datetime.datetime):
            return o.strftime("%Y-%m-%d %H:%M:%S")

        # 处理日期
        if isinstance(o, datetime.date):
            return o.strftime("%Y-%m-%d")

        # 处理decimal
        if isinstance(o, decimal.Decimal):
            return float(o)

        # 其它默认处理
        return json.JSONEncoder.default(self, o)
