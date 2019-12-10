# -*- coding: utf-8 -*-
"""
@Author: rgc
All rights reserved
create time '2019/9/19 10:18'
"""
from flask_loguru import logger

from app.controllers.base import BaseController
from app.models.loonflownew_db import AccountLoonUserModel
from app.utils.response import api_response
from .base import api


@api.resource("/users/fetch-users/")
class AccountFetchUsersController(BaseController):
    """
    """

    def get(self):
        logger.info('start /account/fetch-users/ request')

        user_list = AccountLoonUserModel.get_all_user()
        if user_list is None:
            return api_response('', 400)
        return api_response({"msg": "", "code": 0, "data": user_list}, 200)
