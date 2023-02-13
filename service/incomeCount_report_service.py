import datetime

from sql import incomeCount_report_sql

"""
    收益率计算报表Service
"""


class IncomeCountReportService:

    def __init__(self):
        self.sql = incomeCount_report_sql

    """
        收益率计算报表列表查询
    """

    def incomeCount_report_list(self, query_data):
        datalist = self.sql.get_incomeCount_report_list(query_data)

        data = []
        data1 = {"positionNo": "1", "productName": "1、现金及流动性管理工具", "incomeRate": 11, "incomeAmt": 89.73, "avgScale": 2.18,
                 "realScale": 9.16, "yearRate": 89.73}
        data2 = {"positionNo": "2", "productName": "2、固定收益类投资资产", "incomeRate": 11, "incomeAmt": 89.73, "avgScale": 2.18,
                 "realScale": 9.16, "yearRate": 89.73}
        data3 = {"positionNo": "3", "productName": "2.1境内固定收益类投资资产", "incomeRate": 11, "incomeAmt": 89.73, "avgScale": 2.18,
                 "realScale": 9.16, "yearRate": 89.73}
        data4 = {"positionNo": "4", "productName": " 2.2境外固定收益类投资资产", "incomeRate": 11, "incomeAmt": 89.73, "avgScale": 2.18,
                 "realScale": 9.16, "yearRate": 89.73}
        data5 = {"positionNo": "5", "productName": "3、权益类投资资产", "incomeRate": 11, "incomeAmt": 89.73, "avgScale": 2.18,
                 "realScale": 9.16, "yearRate": 89.73}
        data6 = {"positionNo": "6", "productName": "3.1境内长期股权投资", "incomeRate": 11, "incomeAmt": 89.73, "avgScale": 2.18,
                 "realScale": 9.16, "yearRate": 89.73}
        data7 = {"positionNo": "7", "productName": "3.2境内不含长期股权投资的上市股票和基金", "incomeRate": 11, "incomeAmt": 89.73, "avgScale": 2.18,
                 "realScale": 9.16, "yearRate": 89.73}
        data8 = {"positionNo": "8", "productName": "3.3境内不含长期股权投资的其他权益投资资产", "incomeRate": 11, "incomeAmt": 89.73, "avgScale": 2.18,
                 "realScale": 9.16, "yearRate": 89.73}
        data9 = {"positionNo": "9", "productName": "3.4境外权益类投资", "incomeRate": 11, "incomeAmt": 89.73, "avgScale": 2.18,
                 "realScale": 9.16, "yearRate": 89.73}
        data10 = {"positionNo": "10", "productName": "4、投资性房地产", "incomeRate": 11, "incomeAmt": 89.73, "avgScale": 2.18,
                 "realScale": 9.16, "yearRate": 89.73}
        data11 = {"positionNo": "11`", "productName": "另：卖出回购证券", "incomeRate": 11, "incomeAmt": 89.73, "avgScale": 2.18,
                 "realScale": 9.16, "yearRate": 89.73}
        data12 = {"positionNo": "12", "productName": "贷款", "incomeRate": 11, "incomeAmt": 89.73, "avgScale": 2.18,
                 "realScale": 9.16, "yearRate": 89.73}
        data13 = {"positionNo": "13", "productName": "金融衍生工具", "incomeRate": 11, "incomeAmt": 89.73, "avgScale": 2.18,
                  "realScale": 9.16, "yearRate": 89.73}
        data14 = {"positionNo": "14", "productName": "资金运用净额", "incomeRate": 11, "incomeAmt": 89.73, "avgScale": 2.18,
                  "realScale": 9.16, "yearRate": 89.73}

        data.append(data1)
        data.append(data2)
        data.append(data3)
        data.append(data4)
        data.append(data5)
        data.append(data6)
        data.append(data7)
        data.append(data8)
        data.append(data9)
        data.append(data10)
        data.append(data11)
        data.append(data12)
        data.append(data13)
        data.append(data14)
        # for data in datalist.get("list"):
        #     data["term"] = self.__dealDate()
        #     data["weight"] = (abs(data["matchSettleAmt"]) * data["term"]) / 365
        #     data["yield"] = data["weight"] * data["matchMaturityYield"]
        return {"total": len(data), "list": data}

    '''
    处理日期，当前日期和上月月底日期相差天数
    '''

    def __dealDate(self):
        today = datetime.date.today()
        first = today.replace(day=1)
        last_month = first - datetime.timedelta(days=1)
        num = (today - last_month).days
        return num
