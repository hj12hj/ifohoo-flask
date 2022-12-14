from controllers.config_controller import config
from controllers.config_history_controller import config_history
from controllers.log_controller import log

# 注册蓝图列表
blueprint_list = [log, config, config_history]
