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
        formName = query_data.get("formName")
        if formName is None or formName == "":
            query_name = None
        else:
            query_name = "%" + formName + "%"

        organCode = local_token.token_info.get("organCode")
        total, data = self.db.query_page(
            "select * from dynamic_report where form_name like:1 and form_code =:2 and organ_code =:3",
            (query_name, query_data.get("formCode"), organCode), handle_none=True)

        return {"total": total, "list": data}

    # 动态配置插入数据  2.0
    # def insert_config_info(self, config_data):
    #     dt = datetime.datetime.now()
    #     staffId = local_token.token_info.get("staffNo")
    #     self.db.execute_sql(
    #         "insert into dynamic_report (form_code, form_name, form_default_content, form_detail_content, version, creator, create_time, update_by, update_time) values (:1,:2,:3,:4,:5,:6,:7,:8,:9)",
    #         (config_data.get("formCode"), config_data.get("formName"), config_data.get("formDefaultContent"),
    #          config_data.get("formDetailContent"), 1, staffId, dt,
    #          staffId, dt))

    # 动态配置插入数据  2.5 增加机构
    def insert_config_info(self, config_data):
        dt = datetime.datetime.now()
        staffId = local_token.token_info.get("staffNo")
        organCode = local_token.token_info.get("organCode")
        self.db.execute_sql(
            "insert into dynamic_report (organ_code, form_code,form_name ,form_default_data, form_detail_data, row_version_no, last_operate_staff_code, last_operate_datetime) values (:1,:2,:3,:4,:5,:6,:7,:8)",
            (organCode, config_data.get("formCode"), config_data.get("formName"), config_data.get("formDefaultData"),
             config_data.get("formDetailData"), 1, staffId, dt))

    # 动态配置更新数据
    def update_config_info(self, config_data):
        staffNo = local_token.token_info.get("staffNo")
        self.db.execute_sql(
            "update dynamic_report set  form_default_data=:1 ,form_detail_data=:2,last_operate_staff_code=:3,form_name=:4 ,row_version_no = row_version_no +1 where form_code = :5",
            (config_data.get("formDefaultData"), config_data.get("formDetailData"),
             staffNo, config_data.get("formName"), config_data.get("formCode")))

    # 根据主键查找数据
    def find_by_id(self, form_code):
        data = self.db.query_one("select * from dynamic_report where form_code = :1", (form_code,))
        return data

    def delete_by_id(self, form_code):
        self.db.execute_sql("delete from dynamic_report where form_code = :1", (form_code,))

    def find_name_map(self):
        return self.db.query_all("select form_code,form_name from dynamic_report")
