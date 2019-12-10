# -*- coding: utf-8 -*-
"""
@Author: rgc
All rights reserved
create time '2019/9/19 10:18'
"""
from flask_loguru import logger

from app.controllers.base import BaseController
from app.libs.pre_request import Rule
from app.utils import WorkFlowAPiRequest, get_request_username
from app.utils.response import api_response
from .base import api

request_rules = {
    "category": Rule(direct_type=str, allow_empty=True),
    "page": Rule(direct_type=int, allow_empty=True),
}


@api.resource("/logs/<int:ticket_id>/")
class ServiceLogsController(BaseController):
    """
    获取工单 操作日志
    """

    def get(self, ticket_id):
        logger.info(f'start /service/logs/{ticket_id} request')

        username = get_request_username()
        if not ticket_id:
            return api_response("请输入工单id", 400)

        ins = WorkFlowAPiRequest(username)
        status, resp = ins.getdata(dict(per_page=10, name=''), method='get',
                                   url='/api/v1.0/tickets/{}/flowlogs?username={}'.format(ticket_id, username))
        if resp['code'] == 0:
            return api_response({'code': resp['code'], 'data': resp['data'], 'msg': resp['msg']}, 200)
        else:
            return api_response({'code': resp['code'], 'data': None, 'msg': resp['msg']}, 400)
