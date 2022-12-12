from aop.handle_sql_result import handle_time_format
from aop.handle_transation import transaction
from variables.db_connection import db


class UserSql:
    def __init__(self):
        self.db = db

    # @handle_time_format
    def get_users(self):
        data = self.db.query_all("select * from test  where user_id = :1 and user_name =:2", [1, 'hh'])
        return data

    def insert_user(self):
        self.db.execute_sql("insert into user (user_id, user_name) values (%s,%s)",
                            (2, 'admin@example.com'))
