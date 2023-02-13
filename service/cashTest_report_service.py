import datetime

from sql import cashTest_report_sql

"""
    现金流测试报表Service
"""


class CashTestReportService:

    def __init__(self):
        self.sql = cashTest_report_sql

    """
        现金流测试报表列表查询
    """

    def cashTest_report_list(self, query_data):
        datalist = self.sql.get_cashTest_report_list(query_data)

        data = []
        data1 = {"categoryType": "现金及现金等价物", "description": "不属于现金及现金等价物的现金及流动性管理工具，如央行票据、商业银行票据、货币市场基金、同业存单等。", "rate": "100%", "oneAmount": 2.18,
                 "oneRateAmt": 9.16, "twoAmount": 89.73, "twoRateAmt": 2.18, "threeAmount": 9.16, "threeRateAmt": 89.73, "fourAmount": 2.18, "fourRateAmt": 9.16, "fiveAmount": 89.73, "fiveRateAmt": 2.18}
        data2 = {"categoryType": "现金及现金等价物", "description": "划入可供出售金融资产或交易性金融资产的中央政府债", "rate": "95%", "oneAmount": 2.18,
                 "oneRateAmt": 9.16, "twoAmount": 89.73, "twoRateAmt": 2.18, "threeAmount": 9.16, "threeRateAmt": 89.73, "fourAmount": 2.18, "fourRateAmt": 9.16, "fiveAmount": 89.73, "fiveRateAmt": 2.18}
        data3 = {"categoryType": "现金及现金等价物", "description": "划入可供出售金融资产或交易性金融资产的省级政府债、准政府债、AAA 级的金融企业（公司）债；定期存款、协议存款", "rate": "90%", "oneAmount": 2.18,
                 "oneRateAmt": 9.16, "twoAmount": 89.73, "twoRateAmt": 2.18, "threeAmount": 9.16, "threeRateAmt": 89.73, "fourAmount": 2.18, "fourRateAmt": 9.16, "fiveAmount": 89.73, "fiveRateAmt": 2.18}
        data4 = {"categoryType": "现金及现金等价物", "description": "划入可供出售金融资产或交易性金融资产的AAA级的非金融企业（公司）债；债券型基金", "rate": "85%", "oneAmount": 2.18,
                 "oneRateAmt": 9.16, "twoAmount": 89.73, "twoRateAmt": 2.18, "threeAmount": 9.16, "threeRateAmt": 89.73, "fourAmount": 2.18, "fourRateAmt": 9.16, "fiveAmount": 89.73, "fiveRateAmt": 2.18}
        data5 = {"categoryType": "现金及现金等价物", "description": "上市股票（不含举牌及计入长期股权投资的股票）；证券投资基金（不含货币市场基金、债券型基金）；可转债", "rate": "80%", "oneAmount": 2.18,
                 "oneRateAmt": 9.16, "twoAmount": 89.73, "twoRateAmt": 2.18, "threeAmount": 9.16, "threeRateAmt": 89.73, "fourAmount": 2.18, "fourRateAmt": 9.16, "fiveAmount": 89.73, "fiveRateAmt": 2.18}
        data6 = {"categoryType": "现金及现金等价物", "description": "划入持有至到期投资或贷款和应收款项的国债", "rate": "95%", "oneAmount": 2.18,
                 "oneRateAmt": 9.16, "twoAmount": 89.73, "twoRateAmt": 2.18, "threeAmount": 9.16, "threeRateAmt": 89.73, "fourAmount": 2.18, "fourRateAmt": 9.16, "fiveAmount": 89.73, "fiveRateAmt": 2.18}
        data7 = {"categoryType": "现金及现金等价物", "description": "划入持有至到期投资或贷款和应收款项的省级政府债、准政府债、AAA 级的金融企业（公司）债", "rate": "90%", "oneAmount": 2.18,
                 "oneRateAmt": 9.16, "twoAmount": 89.73, "twoRateAmt": 2.18, "threeAmount": 9.16, "threeRateAmt": 89.73, "fourAmount": 2.18, "fourRateAmt": 9.16, "fiveAmount": 89.73, "fiveRateAmt": 2.18}
        data8 = {"categoryType": "现金及现金等价物", "description": "划入持有至到期投资或贷款和应收款项的AAA 级的非金融企业（公司）债", "rate": "85%", "oneAmount": 2.18,
                 "oneRateAmt": 9.16, "twoAmount": 89.73, "twoRateAmt": 2.18, "threeAmount": 9.16, "threeRateAmt": 89.73, "fourAmount": 2.18, "fourRateAmt": 9.16, "fiveAmount": 89.73, "fiveRateAmt": 2.18}
        data9 = {"categoryType": "现金及现金等价物", "description": "固定收益类保险资产管理产品、权益类保险资产管理产品", "rate": "75%", "oneAmount": 2.18,
                 "oneRateAmt": 9.16, "twoAmount": 89.73, "twoRateAmt": 2.18, "threeAmount": 9.16, "threeRateAmt": 89.73, "fourAmount": 2.18, "fourRateAmt": 9.16, "fiveAmount": 89.73, "fiveRateAmt": 2.18}
        data10 = {"categoryType": "现金及现金等价物", "description": "其他资产", "rate": "60%", "oneAmount": 2.18,
                 "oneRateAmt": 9.16, "twoAmount": 89.73, "twoRateAmt": 2.18, "threeAmount": 9.16, "threeRateAmt": 89.73, "fourAmount": 2.18, "fourRateAmt": 9.16, "fiveAmount": 89.73, "fiveRateAmt": 2.18}
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
