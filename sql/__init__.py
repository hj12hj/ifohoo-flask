from sql.bond_report_sql import BondReportSql
from sql.user_sql import UserSql
from sql.config_sql import ConfigSql
from sql.config_history_sql import ConfigHistorySql
from sql.cost_position_sql import CostPositionSql
from sql.flowRate_report_sql import FlowRateReportSql
from sql.cashTest_report_sql import CashTestReportSql
from sql.incomeCount_report_sql import IncomeCountReportSql

user_sql = UserSql()
config_sql = ConfigSql()
config_history_sql = ConfigHistorySql()
cost_position_sql = CostPositionSql()

bond_report_sql = BondReportSql()

flowRate_report_sql = FlowRateReportSql()
cashTest_report_sql = CashTestReportSql()
incomeCount_report_sql = IncomeCountReportSql()