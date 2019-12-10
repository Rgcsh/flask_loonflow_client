# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) rgc, 2019
# All rights reserved
# @Author: rgc
# @Time: '2019-09-12 17:00'
from flask_script import Manager

from app import create_app

app = create_app()
manager = Manager(app)


@manager.option('-p', '--port', help='Server run port', default=5000)
@manager.option('-h', '--host', help='Server run host', default='0.0.0.0')
def start(host, port):
    """ 开启实例

    :param host: 监听的主机
    :param port: 监听的端口
    """
    app.run(host=host, port=int(port))


if __name__ == '__main__':
    manager.run()
