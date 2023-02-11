from sql.assetDetail_report_sql import AssetDetailReportSql
from sql.bond_report_sql import BondReportSql
from sql.user_sql import UserSql
from sql.config_sql import ConfigSql
from sql.config_history_sql import ConfigHistorySql
from sql.cost_position_sql import CostPositionSql


user_sql = UserSql()
config_sql = ConfigSql()
config_history_sql = ConfigHistorySql()
cost_position_sql = CostPositionSql()

bond_report_sql = BondReportSql()
assetDetail_report_sql = AssetDetailReportSql()
