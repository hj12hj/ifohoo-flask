from sql.bond_report_sql import BondReportSql
from sql.income_calulation_report_sql import IncomeCalculationReportSql
from sql.user_sql import UserSql
from sql.config_sql import ConfigSql
from sql.config_history_sql import ConfigHistorySql
from sql.cost_position_sql import CostPositionSql


user_sql = UserSql()
config_sql = ConfigSql()
config_history_sql = ConfigHistorySql()
cost_position_sql = CostPositionSql()

bond_report_sql = BondReportSql()

income_calculation_report_sql = IncomeCalculationReportSql();
