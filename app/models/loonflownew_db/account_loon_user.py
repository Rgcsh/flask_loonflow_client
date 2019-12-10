# -*- coding: utf-8 -*-
"""
@Author: rgc
All rights reserved
create time '2019/9/18'
"""

from app.core import db
from .entity import AccountLoonUserBase


class AccountLoonUserModel(db.Model, AccountLoonUserBase):
    """
    用户表
    """
    field = {
        'query_list': []
    }

    @staticmethod
    def check_user_exist(username):
        """
        检查登录
        :param username:
        :return:
        """
        return AccountLoonUserModel.exist({'username': username})

    @staticmethod
    def get_user_obj(username):
        return AccountLoonUserModel.get_obj_by_field([AccountLoonUserModel.username == username])

    @staticmethod
    def get_all_user():
        query_result = AccountLoonUserModel.info_all_and_query(
            [AccountLoonUserModel.is_deleted == 0, AccountLoonUserModel.is_active == 1], AccountLoonUserModel.id,
            AccountLoonUserModel.username, AccountLoonUserModel.alias)

        return [{"id": item[0], "username": item[1], "alias": item[2]} for item in query_result]
