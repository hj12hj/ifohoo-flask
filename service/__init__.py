from service.user_service import UserService
from service.config_service import ConfigService


from sql import user_sql
from sql import config_sql

userService = UserService(user_sql)
configService = ConfigService(config_sql)
