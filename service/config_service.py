from aop.handle_transation import transaction


class ConfigService:
    def __init__(self, sql):
        self.sql = sql

    def get_config_list(self):
        return self.sql.get_config_list()

    @transaction
    def insert_config_info(self, config_data):
        self.sql.insert_config_info(config_data)

    @transaction
    def update_config_info(self, config_data):
        return self.sql.update_config_info(config_data)
