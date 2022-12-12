from aop.handle_transation import transaction


class UserService:
    def __init__(self, sql):
        self.sql = sql

    def get_all(self):
        return self.sql.get_users()

    @transaction
    def insert_user(self):
        self.sql.insert_user()
