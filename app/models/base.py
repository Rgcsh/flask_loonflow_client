# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) rgc, 2019
# All rights reserved
# @Author: rgc
# @Time: '2019-09-16 17:59'
# pylint:disable=no-member,too-many-public-methods,wrong-import-order
import traceback

from flask_loguru import logger
from math import ceil
from sqlalchemy import and_, update, select, func, or_
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql.expression import Insert

from app.core import db


class BaseModel:

    @classmethod
    def get_obj_by_field(cls, search):
        """
        通过查询条件获取符合条件的第一个数据对象
        :param search:
        :return:
        """
        return cls.query.filter(and_(*search)).first()

    @classmethod
    def create(cls, info=dict, auto_commit=True):
        """
        新增一条数据
        :param info:
        :param auto_commit:
        :return:
        """
        order = cls(**info)
        db.session.add(order)
        if auto_commit:
            try:
                db.session.commit()
            except SQLAlchemyError:
                logger.error(traceback.format_exc())
                return False

        return True

    @classmethod
    def insert_many(cls, info_list, auto_commit=True):
        """
        批量插入数据
        :param info_list:
        :param auto_commit:
        :return:
        """
        db.session.bulk_insert_mappings(cls, info_list)  # pylint: disable=no-member
        if auto_commit:
            try:
                db.session.commit()  # pylint: disable=no-member
            except SQLAlchemyError:
                logger.error(traceback.format_exc())
                return False
        return True

    @classmethod
    def insert_many_update(cls, info_list, field, auto_commit=True):
        """
        批量插入更新数据，如果存在就更新，如果不存在就插入
        用法优化:放在最后的数据操作 可以使用auto_commit=True从而提交所有对数据库的操作
                不用在业务层显示使用Model.commit()
        警告点：如果出现集中commit()的情况时，在执行完此 语句后，要判断是否执行成功，因为在执行 session.execute就可能
                触发错误，并且在集中commit()时，此错误不会再次捕捉，从而造成批量插入失败，但是返回成功 的业务逻辑错误
               第一次使用会 报警告 S
               AWarning: Can't validate argument 'append_string'; can't locate any SQLAlchemy dialect named 'append'
        集中commit()的情况下,执行此语句时，避免错误的使用方法：
        >>> if not Model.insert_many([{'key':1,'key2':2},{'key':1,'key2':2}], 'sec_id',False):
        >>>     return json_fail(code_dict['db_error'])

        :param info_list: format:[{},{}]
        :param field: 需要修改的字段
        :param auto_commit:
        :return:
        """

        @compiles(Insert)
        def append_string(insert, compiler, **kw):  # pylint:disable=unused-variable
            """
            插入字符串
            :param insert:
            :param compiler:
            :param kw:
            :return:
            """
            s = compiler.visit_insert(insert, **kw)
            if 'append_string' in insert.kwargs:
                return s + " " + insert.kwargs['append_string']
            return s

        session = db.session
        try:
            # 因为如果info_list 为空数据，同样会插入数据库一条数据，所以要有限制
            if info_list:
                session.execute(
                    cls.__table__.insert(append_string='on DUPLICATE KEY UPDATE `{0}` = VALUES(`{0}`)'.format(field)),
                    info_list)
                if auto_commit:
                    session.commit()
        except SQLAlchemyError:
            print(traceback.format_exc())
            logger.error(traceback.format_exc())
            session.rollback()
            return False
        return True

    def to_dict(self, keys, func_name=None):
        """
        把结果数据对象转为dict
        :param keys:
        :param func_name:
        :return:
        """
        d = {}
        for k in keys:
            if func_name:
                d[k] = func_name(getattr(self, k))
            else:
                d[k] = getattr(self, k)
        return d

    @classmethod
    def info(cls, search, field):
        """
        查询一条数据的全部字段(不利于IO,尽量只查需要的字段)，再取部分值
        :param search_list: 搜索列表
        :param field_list: 返回字段列表
        :return:
        """
        ins = cls.query.filter(and_(*search)).first()
        if ins is None:
            return dict()
        return ins.to_dict(keys=field)

    @classmethod
    def info_order(cls, search, field, order):
        """
        查询一条数据的全部字段(不利于IO,尽量只查需要的字段)，再取部分值
        :param search: 搜索列表
        :param field: 返回字段列表
        :param order: 排序
        :return:
        """
        ins = cls.query.filter(and_(*search)).order_by(order).first()
        if ins is None:
            return dict()
        return ins.to_dict(keys=field)

    @classmethod
    def info_all(cls, search_list, field_list):
        """
        查询所有数据的全部字段(不利于IO,尽量只查需要的字段)，再取部分值
        :param search_list: 搜索列表
        :param field_list: 返回字段列表
        :return:
        """
        ins = cls.query.filter(and_(*search_list)).all()
        if ins is None:
            return None
        return list(
            map(
                lambda x: x.to_dict(field_list), ins
            )
        )

    @classmethod
    def info_all_and_query(cls, search, *field):
        """

        :param search: list 如:[AttMacroStateModel.type == 1, AttMacroStateModel.status == 1]
        :param field: 传变量 如: AttMacroState.type
        :return:
        """
        return db.session.query(*field).filter(and_(*search)).all()

    @classmethod
    def info_all_and_query_order(cls, search, order, *field):
        """查询所有的数据并且按照某一个字段进行排序

        :param search: list 如:[AttMacroStateModel.type == 1, AttMacroStateModel.status == 1]
        :param field: 传变量 如: AttMacroState.type
        :return:
        """
        return db.session.query(*field).filter(and_(*search)).order_by(order).all()

    @classmethod
    def info_all_and_query_group(cls, search, group, *field):
        """查询所有的数据并且分组

        :param search: list 如:[AttMacroStateModel.type == 1, AttMacroStateModel.status == 1]
        :param field: 传变量 如: AttMacroState.type
        :return:
        """
        return db.session.query(*field).filter(and_(*search)).group_by(group).all()

    @classmethod
    def info_all_or_query(cls, search, *field):
        """

        :param search: list 如:[AttMacroStateModel.type == 1, AttMacroStateModel.status == 1]
        :param field: 传变量 如: AttMacroState.type
        :return:
        """
        return db.session.query(*field).filter(or_(*search)).all()

    @classmethod
    def info_first_and_query(cls, search, *field):
        """

        :param search: list 如:[AttMacroStateModel.type == 1, AttMacroStateModel.status == 1]
        :param field: 传变量 如: AttMacroState.type
        :return:
        """
        return db.session.query(*field).filter(and_(*search)).first()

    @classmethod
    def info_first_and_query_order(cls, search, order_field, *field):
        """

        :param search: list 如:[AttMacroStateModel.type == 1, AttMacroStateModel.status == 1]
        :param order_field: 传需要排序的变量 如: AttMacroState.id
        :param field: 传变量 如: AttMacroState.type
        :return:
        """
        return db.session.query(*field).filter(and_(*search)).order_by(order_field.desc()).first()

    @classmethod
    def info_first_or_query(cls, search, *field):
        """

        :param search: list 如:[AttMacroStateModel.type == 1, AttMacroStateModel.status == 1]
        :param field: 变量 如：AttMacroState.id
        :return:
        """
        return db.session.query(*field).filter(or_(*search)).first()

    @classmethod
    def query_limit2(cls, search, orderby, *field):
        """
        查询最后的两个数据
        :param search: list 如:[AttMacroStateModel.type == 1, AttMacroStateModel.status == 1]
        :param field: 传变量 如: AttMacroState.type
        :return:
        """
        return db.session.query(*field).filter(and_(*search)).order_by(orderby).limit(2).all()

    @classmethod
    def update(cls, search, data, auto_commit=True):
        """
        更新数据
        :param search:
        :param data:
        :param auto_commit:
        :return:
        """
        db.session.execute(
            update(cls).where(and_(*search)).values(**data)
        )

        if auto_commit:
            try:
                db.session.commit()
            except SQLAlchemyError:
                logger.error(traceback.format_exc())
                db.session.rollback()
                return False

        return True

    @classmethod
    def exist(cls, search):
        """
        判断是否存在
        :param search: dict 如：{"product_id": product_id, "status": 1}
        :return:
        """
        return db.session.query(cls.query.filter_by(**search).exists()).scalar()

    @classmethod
    def exist_by_obj(cls, search):
        """
        判断是否存在
        :param search:
        :return:
        """
        return db.session.execute(
            select([func.count(cls.id)]).where(
                and_(*search)
            )
        ).fetchone()[0] >= 1

    @classmethod
    def map_dict(cls, sql):
        """
        对结果进行map操作
        :param sql:
        :return:
        """
        return map(dict, db.session.execute(sql))

    @classmethod
    def list_map_dict(cls, sql):
        """
        对结果转为list
        :param sql:
        :return:
        """
        return list(cls.map_dict(sql))

    @classmethod
    def get_sum(cls, sum_field, filter_list):
        """
        sum操作
        :param sum_field:
        :param filter_list:
        :return:
        """
        c = db.session.execute(
            select([func.sum(sum_field)]).where(and_(*filter_list))
        ).fetchone()[0] or 0
        return c

    @classmethod
    def get_count(cls, sum_field, filter_list):
        """
        count操作
        :param sum_field:
        :param filter_list:
        :return:
        """
        c = db.session.execute(
            select([func.count(sum_field)]).where(and_(*filter_list))
        ).fetchone()[0] or 0
        return c

    @classmethod
    def pagination(cls, search, page_index, page_size, field):
        """搜索并分页

        :param search: list [model.name==1]
        :param page_index: int 第几页，从1开始
        :param page_size: int 每页大小
        :param field: list 想要查询的字段
        :return: list
        """

        result = cls.query.filter(and_(*search)).paginate(int(page_index), int(page_size), False)
        result_list = []
        for item in result.items:
            result_list.append(item.to_dict(keys=field))
        return result_list

    @classmethod
    def pagination_order(cls, search, page_index, page_size, field, order):
        """搜索并分页并排序

        :param search: list [model.name==1]
        :param page_index: int 第几页，从1开始
        :param page_size: int 每页大小
        :param field: list 想要查询的字段
        :param order:  想要排序的字段
        :return: list
        """

        result = cls.query.filter(and_(*search)).order_by(order).paginate(int(page_index), int(page_size), False)
        result_list = []
        for item in result.items:
            result_list.append(item.to_dict(keys=field))
        return result_list

    @staticmethod
    def get_total_page(total_count, page_size):
        """
        获取总页数
        :param total_count:
        :param page_size:
        :return:
        """
        total_page = 1
        if page_size > 0:
            total_page = ceil(total_count / page_size)
        return total_page if total_page > 0 else 1

    @staticmethod
    def get_total_count(query, page_size=None, page_result=None):
        """
        获取总条数
        :param query:
        :param page_size:
        :param page_result:
        :return:
        """
        if page_size and page_result:
            result_len = len(page_result)
            if page_size > len(page_result):
                # Reduce unnecessary database access.
                return result_len

        return query.order_by(None).count()

    @staticmethod
    def paginate_query(query, page, page_size):
        """
        分页查询数据
        :param query:
        :param page:
        :param page_size:
        :return:
        """
        if page_size > 0:
            query = query.limit(page_size)

        if page > 1:
            query = query.offset((page - 1) * page_size)

        page_result = query.all()

        return page_result

    @classmethod
    def get_paging_result(cls, query, page, page_size):
        """
        获取分页结果及数据总条数
        :param query:
        :param page:
        :param page_size:
        :return:
        """
        page_result = cls.paginate_query(query, page, page_size)
        total_count = cls.get_total_count(query, page_size, page_result)
        # total_page = cls.get_total_page(total_count, page_size)
        return page_result, total_count

    @classmethod
    def db_commit(cls):
        """
        提交数据库
        :return:
        """
        try:
            db.session.commit()
            return True
        except SQLAlchemyError:
            logger.error(traceback.format_exc())
            db.session.rollback()
            return False
