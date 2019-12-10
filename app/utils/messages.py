# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) rgc, 2019
# All rights reserved
# @Author: rgc
# @Time: '2019-09-16 11:41'

error_message = {
    # 系统错误
    200: "请求成功",
    403: "无权限，禁止访问",
    405: "方式不被允许",
    500: "请求处理失败",

    # 用户权限等
    501: "用户信息不存在",
    502: "用户权限列表不存在",
    503: "用户权限不足",

    # 参数
    10001: "参数错误",

    # 沙盘推演模块
    1001: "参数值类型错误",
    1002: "参数值错误",
    1003: "没有查询到历史数据",
    1004: "查询的产品信息不存在",
    1005: "沙盘推演试算返回值长度不对",
    1006: "查询数据返回值长度不对",
    1007: "没有数据",
    1010: "查找数据不在同一个月",
    1011: "提交的吸引子建议参数值不对",
    1012: "提交数据到数据库失败，请检查参数或联系后台人员",

    # message
    1022: "error_message中没有这个code",

    # SAA
    10055: "SAA无法生成 无约束有效前沿",
    10056: "可投资工具填写错误",
    10057: "SAA基准比例参数错误",
    10058: "产品持仓参数检查失败",
    10059: "选中的可投资工具，必须要填写SAA试算比例",
    10060: "所有有效的SAA试算比例的和应该大于等于1， 并且和要小于等于1+组合杠杆限制",
    10061: "查询宏观参数失败",
    10062: "检查配置力度失败",
    10063: "当前产品无净值数据",
    10064: "当前产品无净值规模数据",
    10065: "当前产品无持仓收益率数据",
    10068: "当前产品无持仓比例数据",
    10069: "股权资产选中时，请填写相关收益率",
    10070: "股权预期收益必须大于等于下限，小于等于上限",
    10071: "非标预期收益率必须填写",
    10072: "非标预期坏账率必须填写",
    10073: "非标预期回收率必须填写",
    10074: "当前用户没有该产品的相关权限",
    10075: "当前用户没有该产品的提交权限",
    10076: "缓存失效，请重新试算",
    10077: "选定的范围内，没有符合条件的点",
    10078: "函数计算调用失败",
    10079: "当前没有符合条件的组合",

    # 资产约束
    10080: "资产下限应大于等于0",
    10081: "资产上限应小于等于（1+组合杠杆约束）",
    10082: "资产下限应该小于等于上限",
    10083: "大类资产下限之和小于等于（1+组合杠杆约束）",
    10084: "大类资产上限之和大于等于1",
    10085: "所有小类下限之和小于等于所属大类上限",
    10086: "所有小类上限之和大于等于所属大类下限",
    10087: "所有小类上限小于等于所属大类上限",
    10088: "可投资工具设置至少选择权益类,固收类的一个小类资产",

    10095: "TAA试算比例检查失败",
    10096: "检查TAA资产单位VaR值失败",
    10097: "检查TAA协方差矩阵失败",

    # TAA
    10110: "TAA主试算运行失败",
    10111: "TAA模拟回测运行失败",
    10112: "试算数据提交失败",

    # 业绩评估
    10201: "当前产品还未进行测算",
    10202: "业绩评估运行失败",
    10203: "业绩评估数据存储失败",
    10204: "正在进行业绩评估，请稍后",

    # 产品
    10301: "产品代码已存在",
    10302: "净值日期晚于当前日期",
    10303: "产品的持仓比例总和小于1，持仓比例参数错误",
    10304: "产品不存在",
    10305: "无权限编辑，产品拥有者可编辑",
    10306: "无权限查看该产品详情",
    10307: "产品不能分享给自己",
    10308: "不是自己的产品，无权限分享",
    10309: "分享失败",
    10310: "无权限访问产品",
    10311: "无权限创建产品",
    10312: "无权删除产品",
    10313: "无权限删除该分享",
    10314: "删除分享失败，分享不存在或已被删除",
    10316: "权限检查失败",
    10321: "官方产品同步失败",
    10322: "产品不存在或被删除，无法分享",
    10323: "产品不存在或被删除，无法删除分享",
    10324: "当前测算历史不存在，或已经被删除",
    10325: "删除测算历史失败",
    10326: "删除产品持仓数据失败",
    10327: "当前日期净值已经存在",
    10328: "当前日期净值数据不存在",
    10329: "提交产品净值数据失败",

    # 用户
    10501: "用户不存在或被删除",
    10502: "请输入被分享人的完整账号（手机号或邮箱）",
    10503: "用户信息不存在",

    # mysql
    10401: "上传数据到mysql出错",
    # 风险管理
    10211: "风险管理运行失败",
    10212: "风险管理数据存储失败",
    10213: "正在进行风险测算，请稍后",

    # 模拟回测
    10601: "查询开始时间应该大于结束时间",
    10602: "提交产品模板数据失败",
    10603: "当前模板名称已经存在",
    10604: "模板代码错误",
    10605: "尝试删除模板失败",
    10606: "当前任务名称已经存在",
    10607: "回测任务提交失败",
    10608: "当前任务不存在",
    10609: "尝试删除回测任务失败",
    10610: "模拟回测运行失败",

    # 沙盘推演模块
    11000: "没有查询到历史数据",

    # 产品模块
    12000: "当前测算不存在",
}
