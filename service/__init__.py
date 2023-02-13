from service.assetDetail_report_service import AssetDetailReportService
from service.config_history_service import ConfigHistoryService
from service.bond_report_service import BondReportService
from service.income_calculation_report_service import IncomeCalculationReportService
from service.user_service import UserService
from service.config_service import ConfigService
from service.cost_position_service import CostPositionService

userService = UserService()
configService = ConfigService()
historyService = ConfigHistoryService()
costPositionService = CostPositionService()
bondReportService = BondReportService()
assetDetailReportService = AssetDetailReportService()
incomeCalculationReportService = IncomeCalculationReportService()
