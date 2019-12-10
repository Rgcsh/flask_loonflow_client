# -*- coding: utf-8 -*-
"""
@Author: rgc
All rights reserved
create time '2019/9/19 10:18'
"""
from flask_loguru import logger

from .base import api
from app.controllers.base import BaseController
from app.libs.pre_request import filter_params, Rule
from app.utils import UEDITER_SETTING
from app.utils.response import api_response

request_rules = {
    "action": Rule(direct_type=str, allow_empty=False),
}

@api.resource("/ueditor/")
class ServiceUeditorController(BaseController):
    """
    """

    @filter_params(get=request_rules)
    def get(self, params):
        logger.info('start /service/ueditor/ request')
        action = params['action']

        if action == 'config':
            return api_response(UEDITER_SETTING, 200)
        return api_response("禁用其他参数相关功能", 400)
