# -*- coding: utf-8 -*-
"""
@Author: rgc
All rights reserved
create time '2019/9/18'
"""

from sqlalchemy import Column, func, BigInteger, Integer, DATETIME, VARCHAR

from app.models.base import BaseModel

BIND_KEY = "loonflownew"


class AccountAppTokenBase(BaseModel):
    """记录第三方系统接入 looflow 后台系统的 app token"""

    __bind_key__ = BIND_KEY
    __tablename__ = 'account_apptoken'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True, comment="物理主键")
    app_name = Column(VARCHAR(50), nullable=False, comment="应用名称")
    token = Column(VARCHAR(50), nullable=False, comment="签名令牌,后端自动生成")
    workflow_ids = Column(VARCHAR(2000), nullable=False, comment="工作流权限id,有权限的工作流ids,逗号隔开,如1,2,3")
    ticket_sn_prefix = Column(VARCHAR(20), nullable=False, comment="工单流水号前缀,如设置为loonflow,则创建的工单的流水号为loonflow_201805130013")

    creator = Column(VARCHAR(50), nullable=False, comment="创建人")
    gmt_created = Column(DATETIME, nullable=False, server_default=func.now(), comment="创建时间")
    gmt_modified = Column(DATETIME, nullable=False, server_default=func.now(), onupdate=func.now(), comment="更新时间")
    is_deleted = Column(Integer, nullable=False, server_default="0", comment="状态 0:未删除 1:已删除")


class AccountLoonDeptBase(BaseModel):
    """部门表"""

    __bind_key__ = BIND_KEY
    __tablename__ = 'account_loondept'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True, comment="物理主键")
    name = Column(VARCHAR(50), nullable=False, comment="部门名称")
    parent_dept_id = Column(Integer, nullable=False, server_default="0", comment="上级部门id")
    leader = Column(VARCHAR(50), nullable=False, server_default="", comment="部门的leader, loonuser表中的用户名")
    approver = Column(VARCHAR(100), nullable=False, server_default="",
                      comment="loonuser表中的用户名, 逗号隔开多个user。当工作流设置为leader审批时， 优先以审批人为准，如果审批人为空，则取leader")
    label = Column(VARCHAR(50), nullable=False, server_default="",
                   comment="标签,因为部门信息一般是从别处同步过来， 为保证对应关系，同步时可以在此字段设置其他系统中相应的唯一标识")

    creator = Column(VARCHAR(50), nullable=False, comment="创建人,loonuser表中的用户名")
    gmt_created = Column(DATETIME, nullable=False, server_default=func.now(), comment="创建时间")
    gmt_modified = Column(DATETIME, nullable=False, server_default=func.now(), onupdate=func.now(), comment="更新时间")
    is_deleted = Column(Integer, nullable=False, server_default="0", comment="状态 0:未删除 1:已删除")


class AccountLoonRoleBase(BaseModel):
    """角色表"""

    __bind_key__ = BIND_KEY
    __tablename__ = 'account_loonrole'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True, comment="物理主键")
    name = Column(VARCHAR(50), nullable=False, comment="名称")
    description = Column(VARCHAR(50), nullable=False, comment="描述")
    label = Column(VARCHAR(50), nullable=False, server_default="{}",
                   comment="标签,因为角色信息也可能是从别处同步过来， 为保证对应关系，同步时可以在此字段设置其他系统中相应的唯一标识,字典的json格式")

    creator = Column(VARCHAR(50), nullable=False, comment="创建人")
    gmt_created = Column(DATETIME, nullable=False, server_default=func.now(), comment="创建时间")
    gmt_modified = Column(DATETIME, nullable=False, server_default=func.now(), onupdate=func.now(), comment="更新时间")
    is_deleted = Column(Integer, nullable=False, server_default="0", comment="状态 0:未删除 1:已删除")


class AccountLoonUserBase(BaseModel):
    """用户表"""

    __bind_key__ = BIND_KEY
    __tablename__ = 'account_loonuser'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True, comment="物理主键")
    password = Column(VARCHAR(128), nullable=False, comment="密码")
    last_login = Column(DATETIME, comment="最近登录时间")
    username = Column(VARCHAR(50), nullable=False, unique=True, comment="用户名")
    alias = Column(VARCHAR(50), nullable=False, server_default="", comment="姓名")
    email = Column(VARCHAR(255), nullable=False, comment="邮箱")
    phone = Column(VARCHAR(13), nullable=False, server_default="", comment="电话")
    dept_id = Column(Integer, nullable=False, server_default="0", comment="部门id")
    is_active = Column(Integer, nullable=False, server_default="1", comment="已激活 1:是")
    is_admin = Column(Integer, nullable=False, server_default="1", comment="超级管理员 1:是")

    creator = Column(VARCHAR(50), nullable=False, comment="创建人")
    gmt_created = Column(DATETIME, nullable=False, server_default=func.now(), comment="创建时间")
    gmt_modified = Column(DATETIME, nullable=False, server_default=func.now(), onupdate=func.now(), comment="更新时间")
    is_deleted = Column(Integer, nullable=False, server_default="0", comment="状态 0:未删除 1:已删除")


class AccountLoonUserRoleBase(BaseModel):
    """用户角色关系表"""

    __bind_key__ = BIND_KEY
    __tablename__ = 'account_loonuserrole'

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True, comment="物理主键")
    user_id = Column(Integer, nullable=False, comment="用户id")
    role_id = Column(Integer, nullable=False, comment="角色id")

    creator = Column(VARCHAR(50), nullable=False, comment="创建人")
    gmt_created = Column(DATETIME, nullable=False, server_default=func.now(), comment="创建时间")
    gmt_modified = Column(DATETIME, nullable=False, server_default=func.now(), onupdate=func.now(), comment="更新时间")
    is_deleted = Column(Integer, nullable=False, server_default="0", comment="状态 0:未删除 1:已删除")
