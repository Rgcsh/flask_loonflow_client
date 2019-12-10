# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) rgc, 2019
# All rights reserved
# @Author: rgc
# @Time: '2019-09-12 17:00'
# sys
import importlib

# 3p
from flask import Flask  # pylint: disable=import-error

# project
from app.middleware import MIDDLEWARE
from config import Config


def _config_app(app):
    """ 将配置文件读取Flask对象
    """
    conf = Config()
    app.config.from_object(conf)
    conf.init_app(app)


def _config_extensions(flask_app):
    """ 配置扩展
    """
    from app import core
    for ext in core.__all__:
        getattr(core, ext).init_app(flask_app)


def _config_blueprints(flask_app):
    """ 配置蓝图
    """
    from app import controllers
    for controller in controllers.__all__:
        obj = importlib.import_module("app.controllers.%s" % controller)
        flask_app.register_blueprint(getattr(obj, controller), url_prefix=("/api/v1/%s" % controller))


def _config_middleware(flask_app):
    """ 配置中间件
    """
    for middle in MIDDLEWARE:
        flask_app.before_request(middle.before_request)
        flask_app.after_request(middle.after_request)


def create_app():
    """
    Create an app with config file
    :return: Flask App
    """
    # 创建APP
    app = Flask(__name__)

    # 初始化APP
    _config_app(app)

    # 配置扩展
    _config_extensions(app)

    # 配置蓝图
    _config_blueprints(app)

    # 配置中间件
    _config_middleware(app)

    return app
