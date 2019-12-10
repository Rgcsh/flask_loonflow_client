# -*- coding: utf-8 -*-
# (C) rgc, 2018
# All rights reserved
__author__ = 'rgc'
__time__ = '2018/11/27 17:08'
from .filter_config import FILTER_LIST
from .filter_error import ParamsValueError


def format_str_value(ori_str=None):
    """
    Format string value

    Warning:
        if item in array can not trans to str value, it will be ignore

    if input type is string
        separate input string with ','
    elif input type is list
        use str func to format all item
    else
        invalid input type

    usage:

        >>> format_str_value('0001.SH,0002.SZ')
        ['0001.SH', '0002.SZ']
        >>> format_str_value([1, 2])
        ['1', '2']
        >>> format_str_value(['1', '2'])
        ['1', '2']
        >>> format_str_value()
        []

    :param ori_str: str or list
    :return: array
    :rtype list
    """
    # if input value is none, return empty list
    if not ori_str:
        return list()

    if isinstance(ori_str, int):
        return [ori_str]

    # split string value
    elif isinstance(ori_str, str):
        str_list = ori_str.split(',')
        return list(map(str.strip, str_list))

    # format array value,
    if isinstance(ori_str, (list, tuple, set)):
        result = list()
        for item in ori_str:
            if isinstance(item, str):
                try:
                    item = str(item).strip()
                except Exception:
                    continue
            result.append(item)
        return result

    # unrecognized input type
    return list()


def check_params_rules(params, rules):
    """检查参数是否符合规则

    :param params: 需要检查的参数
    :param rules: 参数的规则
    """
    for key, value in rules.items():
        # 处理多个key共用一个Rule的情况
        key_list = format_str_value(key)
        try:
            for key_item in key_list:
                param = params.get(key_item, None)
                for filter_class in FILTER_LIST:
                    param = filter_class(key_item, param, value)()

                # 如果Key有映射，则重置key
                if value.key_map:
                    params[value.key_map] = param
                    # 删除原始key
                    if key_item in params:
                        del params[key_item]
                else:
                    params[key_item] = param

        except ParamsValueError as error:
            return False, error

    return True, params
