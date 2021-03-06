# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) rgc, 2019
# All rights reserved
# @Author: rgc
# @Time: '2019-09-12 17:30'
# sys
import os
# 3p
import yaml


def expand_env_path(env_path):
    """
    Expands env var path by repeatedly applying
    `expandvars` and `expanduser` until interpolation stops having
    any effect
    使用`expandvars` 和 `expanduser` 函数扩展环境变量路径
    将环境变量中的 `~` 替换成用户路径，将`$NAME` 和 `${NAME}` 替换成具体路径

    :param env_path: environment path
    :return: string
    """
    if not env_path:
        return env_path
    while True:
        interpolated = os.path.expanduser(os.path.expandvars(str(env_path)))
        if interpolated == env_path:
            return interpolated
        env_path = interpolated


def get_config_path(path):
    """
    Get config yaml file path
    获取配置文件路径

    :param path: gaea project home path
    :return: string
    """
    if "LF_CONFIG" not in os.environ:
        return expand_env_path(path)

    return expand_env_path(os.environ["LF_CONFIG"])


def get_conf(path=""):
    """
    Get yaml config object
    获取yaml配置文件对象

    :return: string
    """
    path = get_config_path(path)

    # Raise exception when config file is not exists
    if not os.path.isfile(path):
        raise FileNotFoundError("Config file not found in path: %s" % path)

    return yaml.safe_load(open(path, "r", encoding="utf-8").read())


def path_exists(_path):
    """
    判断文件路径是否存在
    :param _path:
    :return:
    """
    return os.path.exists(_path)
