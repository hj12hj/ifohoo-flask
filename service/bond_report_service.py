import datetime

from sql import bond_report_sql

"""
    短期债券报表Service
"""


class BondReportService:

    def __init__(self):
        self.sql = bond_report_sql

    """
        短期债券报表列表查询
    """

    def bond_report_list(self, query_data):
        datalist = self.sql.get_bond_report_list(query_data)
        for data in datalist.get("list"):
            data["term"] = self.__dealDate()
            data["weight"] = (abs(data["matchSettleAmt"]) * data["term"]) / 365
            data["yield"] = data["weight"] * data["matchMaturityYield"]
        return datalist

    '''
    处理日期，当前日期和上月月底日期相差天数
    '''

    def __dealDate(self):
        today = datetime.date.today()
        first = today.replace(day=1)
        last_month = first - datetime.timedelta(days=1)
        num = (today - last_month).days
        return num
