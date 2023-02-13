from service.config_history_service import ConfigHistoryService
from service.bond_report_service import BondReportService
from service.user_service import UserService
from service.config_service import ConfigService
from service.cost_position_service import CostPositionService
from service.flowRate_report_service import FlowRateReportService
from service.cashTest_report_service import CashTestReportService
from service.incomeCount_report_service import IncomeCountReportService

userService = UserService()
configService = ConfigService()
historyService = ConfigHistoryService()
costPositionService = CostPositionService()

bondReportService = BondReportService()

flowRateReportService = FlowRateReportService()
cashTestReportService = CashTestReportService()
incomeCountReportService = IncomeCountReportService()