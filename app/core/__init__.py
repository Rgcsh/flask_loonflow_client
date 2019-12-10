# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) rgc, 2019
# All rights reserved

from flask_caching import Cache
from flask_loguru import Logger
# 3p
from flask_sqlalchemy import SQLAlchemy

__all__ = [
    "db",
    "log",
    "cache",
]

# 数据库扩展
db = SQLAlchemy()

# 日志扩展
log = Logger()

# 缓存库
cache = Cache()
