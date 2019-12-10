# -*- coding: utf-8 -*-
"""
@Author: rgc
All rights reserved
create time '2019/12/6 10:27'

Module usage:

"""

import hashlib
import time
import traceback

import requests

try:
    import simplejson as json
except ImportError:
    import json


class WorkFlowAPiRequest(object):
    workflow_backend_url = "http://127.0.0.1:6060"
    workflow_token = "8cd585da-3cc6-11e8-9946-784f437daad6"
    workflow_app = "ops"

    def __init__(self, token=workflow_token, appname=workflow_app, username='admin',
                 workflowbackendurl=workflow_backend_url):
        self.token = token
        self.appname = appname
        self.username = username
        self.workflowbackendurl = workflowbackendurl

    def getrequestheader(self):
        timestamp = str(time.time())[:10]
        ori_str = timestamp + self.token
        signature = hashlib.md5(ori_str.encode(encoding='utf-8')).hexdigest()
        headers = dict(signature=signature, timestamp=timestamp, appname=self.appname, username=self.username)
        return headers

    def getdata(self, parameters=None, method='get', url='/api/v1.0/workflows/', timeout=300, data=None):
        if method not in ['get', 'post', 'put', 'delete', 'patch']:
            return False, 'method must be one of get post put delete or patch'
        if not data:
            data = dict()
        if not parameters:
            parameters = dict()

        if not isinstance(parameters, dict):
            return False, 'Parameters must be dict'
        headers = self.getrequestheader()

        try:
            r = getattr(requests, method)('{0}{1}'.format(self.workflowbackendurl, url), headers=headers, params=parameters,
                                          timeout=timeout, data=json.dumps(data))
            result = r.json()
            return True, result
        except:
            return False, traceback.format_exc()
