# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) rgc, 2019
# All rights reserved
# @Author: rgc
# @Time: '2019-09-12 17:08'
# project
from app.utils import get_conf


class Config:

    def __init__(self):
        self.conf = get_conf()

    def init_app(self, app):
        """ 初始化APP
        """
        self.init_core(app)
        self.init_db(app)
        self.init_log(app)
        self.init_redis(app)
        self.init_redirect(app)

    def init_core(self, app):
        """ 初始化Core模块参数
        """
        core = self.conf.get("CORE", dict())

        # 设置DEBUG模式
        app.config["DEBUG"] = core["DEBUG"]
        app.config["CACHE_TYPE"] = core["cache_type"]
        app.config["CACHE_KEY_PREFIX"] = core["cache_prefix"]

        # 秘钥
        app.config["SECRET_KEY"] = core["secret_key"]

    def init_log(self, app):
        """ 初始化Log模块参数
        """
        log = self.conf.get("LOG", dict())

        app.config["LOG_PATH"] = log["path"]
        app.config["LOG_NAME"] = log["name"]
        app.config["LOG_ROTATION"] = int(log["rotation"])
        app.config["LOG_FORMAT"] = log["format"]

    def init_db(self, app):
        """ 初始化DB模块参数
        """
        db = self.conf.get("DB", dict())

        sql_binds, base_uri = dict(), "mysql+pymysql://%s:%s@%s/%s?charset=utf8"

        for db_name, conf in db.items():
            uri = base_uri % (conf["user"], conf["pass"], conf["host"], db_name)
            sql_binds[db_name] = uri

        app.config["SQLALCHEMY_BINDS"] = sql_binds
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

    def init_redis(self, app):
        """ 初始化Redis模块参数
        """
        rds = self.conf.get("REDIS", dict())

        app.config["CACHE_REDIS_DB"] = rds["db"]
        app.config["CACHE_REDIS_PASSWORD"] = rds.get("pass")
        app.config["CACHE_REDIS_HOST"] = rds["host"]
        app.config["CACHE_REDIS_PORT"] = rds["port"]

    def init_redirect(self, app):
        """ 初始化Redis模块参数
        """
        redirect = self.conf.get("REDIRECT", dict())

        app.config["WORKFLOW_BACKEND_URL"] = redirect["workflow_backend_url"]
        app.config["WORKFLOW_TOKEN"] = redirect.get("workflow_token")
        app.config["WORKFLOW_APP"] = redirect["workflow_app"]
