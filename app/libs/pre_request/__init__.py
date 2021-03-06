# -*- coding: utf-8 -*-
# Copyright (c) 2017, rgc
# All rights reserved.
"""
Pre-request Library
~~~~~~~~~~~~~~~~~~~

Pre-request is a library, which help us deal with request params before handler.

Usage:
    >>> import pre_request
    >>> @filter_params()
    >>> def handler_info(**kwargs):
    >>>     print(kwargs)


:copyright: (c) 2018 by rgc
:license: Apache 2.0, see LICENSE for more details.
"""
from .flask import filter_params, all_params, get_request_params
from .utils import check_params_rules
from .filter_rules import Rule
from .filter_rules import Length
from .filter_rules import Range
