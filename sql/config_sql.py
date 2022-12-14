import datetime

from aop.handle_sql_result import handle_time_format
from aop.handle_transation import transaction
from variables import local_token
from variables.db_connection import db


class ConfigSql:

    def __init__(self):
        self.db = db

    # 动态配置分页查询  查询条件 form_code form_name
    @handle_time_format
    def get_config_list(self, query_data):
        query_name = "%" + query_data.get("formName") + "%" if query_data.get("formName") is not None else None
        totle, data = self.db.query_page(
            "select * from dynamic_form where (form_name like :1 or :2 is null) and (form_code = :3 or :4 is null)",
            (query_name, query_data.get("formName"), query_data.get("formCode"),
             query_data.get("formCode")))
        return {"totle": totle, "list": data}

    # 动态配置插入数据
    def insert_config_info(self, config_data):
        dt = datetime.datetime.now()
        staffId = local_token.token_info.get("staffId")
        self.db.execute_sql(
            "insert into dynamic_form (form_code, form_name, form_default_content, form_detail_content, version, creator, create_time, update_by, update_time) value (:1,:2,:3,:4,:5,:6,:7,:8,:9);",
            (config_data.get("formCode"), config_data.get("formName"), config_data.get("formDefaultContent"),
             config_data.get("formDetailContent"), config_data.get("version"), staffId, dt,
             staffId, dt))

    # 动态配置更新数据
    def update_config_info(self, config_data):
        staffId = local_token.token_info.get("staffId")
        self.db.execute_sql(
            "update dynamic_form set  form_default_content=:1 , form_name = :2,form_detail_content=:3,update_by=:4 where form_code = :5;",
            (config_data.get("formDefaultContent"), config_data.get("formName"), config_data.get("formDetailContent"),
             staffId, config_data.get("formCode")))

    # 根据主键查找数据
    def find_by_id(self, form_code):
        data = self.db.query_one("select * from dynamic_form where form_code = :1", (form_code,))
        return data

    def delete_by_id(self, form_code):
        self.db.execute_sql("delete from dynamic_form where form_code = :1;", (form_code,))
