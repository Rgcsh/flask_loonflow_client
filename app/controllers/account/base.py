# -*- coding: utf-8 -*-
"""
@Author: rgc
All rights reserved
create time '2019/9/19 10:18'
"""
from flask import Blueprint

from app.controllers.base import BaseApi

account = Blueprint("account", __name__)
api = BaseApi(account)
