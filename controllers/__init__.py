from controllers.config_controller import config
from controllers.config_history_controller import config_history
from controllers.cost_position_controller import cost_position
from controllers.log_controller import log

# 注册蓝图列表
from controllers.bond_report_controller import bond_report
from controllers.income_calculation_report_controller import income_calculation_report

blueprint_list = [log, config, config_history, cost_position, bond_report, income_calculation_report]
