from sql import config_history_sql


class ConfigHistoryService:
    def __init__(self):
        self.sql = config_history_sql

    def get_config_history_list(self, query_data):
        return self.sql.get_config_history_list(query_data)

    def find_latest_history(self, query_data):
        return self.sql.find_latest_history(query_data)
