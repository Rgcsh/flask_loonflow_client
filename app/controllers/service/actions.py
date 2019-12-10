# -*- coding: utf-8 -*-
"""
@Author: rgc
All rights reserved
create time '2019/9/19 10:18'
"""
from flask_loguru import logger

from app.controllers.base import BaseController
from app.utils import WorkFlowAPiRequest, get_request_username
from app.utils.response import api_response
from .base import api


@api.resource("/actions/<int:ticket_id>/")
class ServiceActionsController(BaseController):
    """
    获取 某个工单 将要进行的操作
    """

    def get(self, ticket_id):
        logger.info(f'start /service/actions/{ticket_id} request')
        username = get_request_username()
        ins = WorkFlowAPiRequest(username)
        status, resp = ins.getdata(dict(per_page=10, name=''), method='get',
                                   url='/api/v1.0/tickets/{}/transitions?username={}'.format(ticket_id, username))
        if resp['code'] == 0:
            return api_response({'code': resp['code'], 'data': resp['data'], 'msg': resp['msg']}, 200)
        else:
            return api_response({'code': resp['code'], 'data': None, 'msg': resp['msg']}, 400)
