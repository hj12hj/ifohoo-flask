import datetime
from aop.handle_sql_result import handle_time_format
from aop.handle_transation import transaction
from variables import local_token
from variables.db_connection import db
import uuid


class ConfigHistorySql:

    def __init__(self):
        self.db = db

    def __handle_time_format(self, item):
        history_start_time = datetime.datetime.strptime(item.get("historyStartTime") + " 00:00:00",
                                                        "%Y-%m-%d %H:%M:%S") if item.get(
            "historyStartTime") is not None else None
        history_end_time = datetime.datetime.strptime(item.get("historyEndTime") + " 00:00:00",
                                                      "%Y-%m-%d %H:%M:%S") if item.get(
            "historyEndTime") is not None else None
        return history_start_time, history_end_time

    # 动态配置历史分页查询
    @handle_time_format
    def get_config_history_list(self, query_data=None):
        history_start_time, history_end_time = self.__handle_time_format(query_data)
        organCode = local_token.token_info.get("organCode")
        total, data = self.db.query_page(
            "select * from dynamic_report_history where form_code =:1  and new_flag_code =:2 and history_time >:3 and history_time <:4 and organ_code =:5 order by history_time desc",
            (
                query_data.get("formCode"), query_data.get("newFlagCode"), history_start_time, history_end_time,
                organCode),
            handle_none=True)

        return {"total": total, "list": data}

    # 动态配置历史插入数据 2.0
    # def insert_config_history(self, config_data):
    #     dt = datetime.datetime.now()
    #     staffId = local_token.token_info.get("staffNo")
    #     templateId = str(uuid.uuid1())
    #     self.db.execute_sql(
    #         "insert into dynamic_report_history (template_id, form_code, form_default_content, form_detail_content, history_time,form_version, last_flag, version, creator, create_time, update_by, update_time) values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12)",
    #         (
    #             templateId.__str__(), config_data.get("formCode"), config_data.get("formDefaultContent"),
    #             config_data.get("formDetailContent"), dt, config_data.get("formVersion"), 'Y',
    #             config_data.get("version"),
    #             staffId, dt, staffId, dt))

    # 动态配置历史插入数据 2.5
    def insert_config_history(self, config_data):
        dt = datetime.datetime.now()
        staffNo = local_token.token_info.get("staffNo")
        templateNo = str(uuid.uuid1())
        self.db.execute_sql(
            "insert into dynamic_report_history (form_template_no, organ_code, form_code, form_name,form_default_data, form_detail_data, form_version_no, new_flag_code, row_version_no, last_operate_staff_code, last_operate_datetime,history_time) values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12)",
            (templateNo.__str__(), config_data.get("organCode"), config_data.get("formCode"),
             config_data.get("formName"),
             config_data.get("formDefaultData"), config_data.get("formDetailData"), config_data.get("formVersionNo"),
             'Y', 1, staffNo, dt, dt))

    # 动态配置更新数据
    def update_config_last_flag(self, form_code, last_flag='N'):
        self.db.execute_sql("update dynamic_report_history set  new_flag_code =:1 where form_code =:2",
                            ('N', form_code))

    def get_last_config_by_form_code(self, form_code):
        data = self.db.query_all("select * from dynamic_report_history where form_code =:1 and new_flag_code =:2",
                                 (form_code, 1))
        return data

    def get_last_form_version_by_form_code(self, form_code):
        data = self.db.query_one(
            "select max(form_version_no) as lastVersion from dynamic_report_history where form_code = :1",
            (form_code,))
        return data

    @handle_time_format
    def find_latest_history(self, query_data):
        return self.db.query_one(
            "select * from dynamic_report_history where form_code = :1 and new_flag_code = 'Y'", data=
            (query_data.get("formCode"),))
