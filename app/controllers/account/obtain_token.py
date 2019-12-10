# -*- coding: utf-8 -*-
"""
@Author: rgc
All rights reserved
create time '2019/9/19 10:18'
"""
from flask_loguru import logger

from app.controllers.base import BaseController
from app.libs.pre_request import filter_params, Rule
from app.models.loonflownew_db import AccountLoonUserModel
from app.utils.response import api_response
from .base import api

request_rules = {
    "username": Rule(direct_type=str, allow_empty=False),
    "password": Rule(direct_type=str, allow_empty=False),
}


@api.resource("/obtain_token/")
class AccountObtainTokenController(BaseController):
    """
    """

    @filter_params(post=request_rules)
    def post(self, params):
        logger.info('start /account/obtain_token/ request')
        # todo:注意用户名只能是英文，否则前端报错，在导入用户数据时 注意校验
        username = params['username']

        user = AccountLoonUserModel.get_user_obj(username)
        if user is None:
            return api_response('', 400)

        return api_response({'token': f'{user.id}.{user.username}'}, 200)
