from aop.handle_transation import transaction
from sql import config_sql
from sql import config_history_sql


class ConfigService:
    def __init__(self):
        self.sql = config_sql

    def get_config_list(self, query_data):
        return self.sql.get_config_list(query_data)

    @transaction
    def insert_config_info(self, config_data):
        self.sql.insert_config_info(config_data)

    # 配置更新数据
    @transaction
    def update_config_info(self, config_data):
        return self.sql.update_config_info(config_data)

    # 配置部署
    @transaction
    def deploy_config(self, form_code):
        # 1.根据主键去配置表查找信息
        data = config_sql.find_by_id(form_code)
        # 2.将相同form_code版本变更
        config_history_sql.update_config_last_flag(form_code=form_code)
        # 3.获取最新版本号
        version = config_history_sql.get_last_form_version_by_form_code(form_code=form_code).get("lastversion")
        version = 1 if version is None else version + 1
        # 3.将配置信息插入到历史表中
        data["formVersion"] = version
        config_history_sql.insert_config_history(data)

    @transaction
    def delete_by_id(self, form_code):
        return self.sql.delete_by_id(form_code)

    def find_by_id(self, form_code):
        return self.sql.find_by_id(form_code)

