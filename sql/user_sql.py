from aop.handle_sql_result import handle_time_format
from aop.handle_transation import transaction
from variables.db_connection import db


class UserSql:
    def __init__(self):
        self.db = db

    # @handle_time_format
    def get_users(self):
        totle, data = self.db.query_page(
            "select d.*,dr.* from dynamic_report_history d left join dynamic_report dr on d.form_code = dr.form_code where d.form_code =:1  and dr.form_name =:2 ",
            [None, "2"], handle_none=True)
        return {"totle": totle, "list": data}

    def insert_user(self):
        self.db.execute_sql("insert into user (user_id, user_name) values (%s,%s)",
                            (2, 'admin@example.com'))
