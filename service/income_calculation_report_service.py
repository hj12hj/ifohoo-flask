
from sql import income_calculation_report_sql

"""
    短期债券报表Service
"""


class IncomeCalculationReportService:

    def __init__(self):
        self.sql = income_calculation_report_sql

    """
        短期债券报表列表查询
    """

    def income_calculation_report_list(self, query_data):
        datalist = self.sql.get_income_calculation_report_list(query_data)
        rowKey = 1
        for data in datalist.get("list"):
            data["rowKey"] = rowKey
            rowKey += 1
        return datalist

