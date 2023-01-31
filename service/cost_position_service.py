from sql import cost_position_sql


class CostPositionService:

    def __init__(self):
        self.sql = cost_position_sql

    def get_cost_position_list(self, query_data):
        return self.sql.get_cost_position_list(query_data)
