# flask_loonflow_client
loonflow项目客户端 工作流审核 后端代码部分

# 声明
此项目为 [loonflow(工作流)](https://github.com/blackholll/loonflow) 的客户端项目([shutongFlow](https://github.com/youshutong2080/shutongFlow)) 的后端代码部分;
感谢 前人的辛苦开源，让我们拥有美好的明天!

### 源项目 获取时的最后上传时间为 2019.11.17

# 修改原因
由于shutongFlow项目后端使用Django编写,及在测试 请假申请 时,发现 shutongFlow项目数据库和 loonFlow项目数据库 账号体系不对应，导致审核出现各种问题；

# 修改内容
* 由Django框架迁移为Flask框架；并且弱化了相关 验证机制;
* 弱化了 登录验证密码功能(随便输入即可)

# 配合的前端项目为
loonflow_client_web

# 启动项目方法(python3.6)
* cd xxx/flask_loonflow_client/requirements
* pip install flask_loguru-2.0.0-py3-none-any.whl 
* pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/  (注意，此安装包为win平台,其他请自行处理)
* 添加 环境变量 LF_CONFIG=xxx\flask_loonflow_client\config\local.yml
* 数据库配置 在本人 loonflow_custom项目中(先安装此项目)
* python manage.py runserver -p 6062

### 其他相关readme内容,请查看 [shutongFlow](https://github.com/youshutong2080/shutongFlow)

# 项目依赖关系架构图
 ![项目依赖关系架构图](./requirements/loonflow.png)
