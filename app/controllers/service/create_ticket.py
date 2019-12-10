# -*- coding: utf-8 -*-
"""
@Author: rgc
All rights reserved
create time '2019/9/19 10:18'
"""
import json

from flask import request
from flask_loguru import logger

from app.controllers.base import BaseController
from app.utils import WorkFlowAPiRequest, get_request_username
from app.utils.response import api_response
from .base import api


@api.resource("/create_ticket/")
class ServiceCreateTicketController(BaseController):
    """
    """

    def post(self):
        logger.info('start /service/create_ticket/ request')
        username = get_request_username()
        ins = WorkFlowAPiRequest(username)
        request_data = json.loads(request.data)
        request_data['username'] = username
        status, resp = ins.getdata(dict(per_page=10, name=''), method='post', url='/api/v1.0/tickets', data=request_data)
        if resp['code'] == 0:
            return api_response({'code': resp['code'], 'data': resp['data'], 'msg': resp['msg']}, 200)
        else:
            return api_response({'code': resp['code'], 'data': None, 'msg': resp['msg']}, 400)
