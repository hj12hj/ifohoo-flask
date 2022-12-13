import datetime

from aop.handle_sql_result import handle_time_format
from aop.handle_transation import transaction
from variables.db_connection import db


class ConfigSql:

    def __init__(self):
        self.db = db

    # 动态配置分页查询
    @handle_time_format
    def get_config_list(self):
        totle, data = self.db.query_page("select * from dynamic_config")
        return {"totle": totle, "list": data}

    # 动态配置插入数据
    def insert_config_info(self, config_data):
        dt = datetime.datetime.now()
        self.db.execute_sql(
            "insert into dynamic_config (form_code, form_name, form_default_content, form_detail_content, version, creator, create_time, update_by, update_time) value (:1,:2,:3,:4,:5,:6,:7,:8,:9);",
            (config_data.get("formCode"), config_data.get("formName"), config_data.get("formDefaultContent"),
             config_data.get("formDetailContent"), config_data.get("version"), config_data.get("creator"), dt,
             config_data.get("updateBy"), dt))

    # 动态配置更新数据
    def update_config_info(self, config_data):
        self.db.execute_sql("update dynamic_config set  form_default_content=:1 where form_code = :2;",
                            (config_data.get("formDefaultContent"), config_data.get("formCode")))
