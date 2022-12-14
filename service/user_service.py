from aop.handle_transation import transaction
from sql import user_sql


class UserService:
    def __init__(self):
        self.sql = user_sql

    def get_all(self):
        return self.sql.get_users()

    @transaction
    def insert_user(self):
        self.sql.insert_user()
