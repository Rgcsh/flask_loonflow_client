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
from app.libs.pre_request import Rule, filter_params
from app.utils import WorkFlowAPiRequest, get_request_username
from app.utils.response import api_response
from .base import api

request_rules = {
    "category": Rule(direct_type=str, allow_empty=True), # duty(我的待办),all(所有工单),relation(我相关的)
    "page": Rule(direct_type=int, allow_empty=True),
}


@api.resource("/tickets/")
class ServiceTicketsController(BaseController):
    """
    获取用户拥有的工单列表
    """

    @filter_params(get=request_rules)
    def get(self, params):
        logger.info('start /service/tickets/ request')

        username = get_request_username()
        category = params['category']
        page = params['page'] or 1
        url = '/api/v1.0/tickets?username={}'.format(username)
        if category:
            url += '&category={}'.format(category)

        ins = WorkFlowAPiRequest(username)
        status, resp = ins.getdata(dict(per_page=10, name='', page=page), method='get', url=url)
        if resp['code'] == 0:
            return api_response({'code': resp['code'], 'data': resp['data'], 'msg': resp['msg']}, 200)
        else:
            return api_response({'code': resp['code'], 'data': None, 'msg': resp['msg']}, 400)


@api.resource("/tickets/<int:ticket_id>/")
class ServiceTicketsInfoController(BaseController):
    """
    获取工单详情
    """

    def get(self, ticket_id):
        logger.info(f'start get /service/tickets/{ticket_id} request')

        username = get_request_username()
        if not ticket_id:
            return api_response("请输入工单id", 400)

        ins = WorkFlowAPiRequest(username)
        status, resp = ins.getdata(dict(per_page=10, name=''), method='get',
                                   url='/api/v1.0/tickets/{}?username={}'.format(ticket_id, username))
        if resp['code'] == 0:
            return api_response({'code': resp['code'], 'data': resp['data'], 'msg': resp['msg']}, 200)
        else:
            return api_response({'code': resp['code'], 'data': None, 'msg': resp['msg']}, 400)

    def patch(self, ticket_id):
        logger.info(f'start patch /service/tickets/{ticket_id} request')

        username = get_request_username()
        if not ticket_id:
            return api_response("请输入工单id", 400)

        ins = WorkFlowAPiRequest(username)
        request_data = json.loads(request.data)
        request_data['username'] = username
        status, resp = ins.getdata(parameters={}, method='patch', url='/api/v1.0/tickets/{}'.format(ticket_id),
                                   data=request_data)
        if resp['code'] == 0:
            return api_response({'code': resp['code'], 'data': resp['data'], 'msg': resp['msg']}, 200)
        else:
            return api_response({'code': resp['code'], 'data': None, 'msg': resp['msg']}, 400)
