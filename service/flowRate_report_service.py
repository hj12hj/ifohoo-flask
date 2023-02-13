import datetime

from sql import flowRate_report_sql

"""
    综合流动比率报表Service
"""


class FlowRateReportService:

    def __init__(self):
        self.sql = flowRate_report_sql

    """
        综合流动比率报表列表查询
    """

    def flowRate_report_list(self, query_data):
        datalist = self.sql.get_flowRate_report_list(query_data)

        data = []
        data1 = {"flowRateNo": 1, "productName": "现金及现金等价物", "marketValueAmt": 11, "dealCashFlow": 89.73, "undueCashFlow": 2.18,
                 "threadMon": 9.16, "oneYear": 89.73, "moreOneYear": 2.18}
        data2 = {"flowRateNo": 2, "productName": "投资资产：", "marketValueAmt": 4109.59, "dealCashFlow": 89.73, "undueCashFlow": 2.18,
                 "threadMon": 9.16, "oneYear": 89.73, "moreOneYear": 2.18}
        data3 = {"productName": "定期存款和协议存款", "marketValueAmt": 4109.59, "dealCashFlow": 89.73, "undueCashFlow": 2.18,
                 "threadMon": 9.16, "oneYear": 89.73, "moreOneYear": 2.18}
        data4 = {"productName": "政府债券", "marketValueAmt": 4109.59, "dealCashFlow": 89.73, "undueCashFlow": 2.18,
                 "threadMon": 9.16, "oneYear": 89.73, "moreOneYear": 2.18}
        data5 = {"productName": "金融债", "marketValueAmt": 4109.59, "dealCashFlow": 89.73, "undueCashFlow": 2.18,
                 "threadMon": 9.16, "oneYear": 89.73, "moreOneYear": 2.18}
        data6 = {"productName": "企业债券", "marketValueAmt": 4109.59, "dealCashFlow": 89.73, "undueCashFlow": 2.18,
                 "threadMon": 9.16, "oneYear": 89.73, "moreOneYear": 2.18}
        data7 = {"productName": "资产证券化产品", "marketValueAmt": 4109.59, "dealCashFlow": 89.73, "undueCashFlow": 2.18,
                 "threadMon": 9.16, "oneYear": 89.73, "moreOneYear": 2.18}
        data8 = {"productName": "信托资产", "marketValueAmt": 4109.59, "dealCashFlow": 89.73, "undueCashFlow": 2.18,
                 "threadMon": 9.16, "oneYear": 89.73, "moreOneYear": 2.18}
        data9 = {"productName": "基础设施投资", "marketValueAmt": 4109.59, "dealCashFlow": 89.73, "undueCashFlow": 2.18,
                 "threadMon": 9.16, "oneYear": 89.73, "moreOneYear": 2.18}
        data10 = {"productName": "保险资产管理产品", "marketValueAmt": 4109.59, "dealCashFlow": 89.73, "undueCashFlow": 2.18,
                  "threadMon": 9.16, "oneYear": 89.73, "moreOneYear": 2.18}
        data11 = {"productName": "权益投资", "marketValueAmt": 4109.59, "dealCashFlow": 89.73, "undueCashFlow": 2.18,
                  "threadMon": 9.16, "oneYear": 89.73, "moreOneYear": 2.18}
        data12 = {"productName": "贷款", "marketValueAmt": 4109.59, "dealCashFlow": 89.73, "undueCashFlow": 2.18,
                  "threadMon": 9.16, "oneYear": 89.73, "moreOneYear": 2.18}
        data13 = {"productName": "投资性不动产", "marketValueAmt": 4109.59, "dealCashFlow": 89.73, "undueCashFlow": 2.18,
                  "threadMon": 9.16, "oneYear": 89.73, "moreOneYear": 2.18}
        data14 = {"productName": "衍生金融工具", "marketValueAmt": 4109.59, "dealCashFlow": 89.73, "undueCashFlow": 2.18,
                  "threadMon": 9.16, "oneYear": 89.73, "moreOneYear": 2.18}
        data15 = {"productName": "其他投资资产", "marketValueAmt": 4109.59, "dealCashFlow": 89.73, "undueCashFlow": 2.18,
                  "threadMon": 9.16, "oneYear": 89.73, "moreOneYear": 2.18}
        data16 = {"productName": "应收款项", "marketValueAmt": 4109.59, "dealCashFlow": 89.73, "undueCashFlow": 2.18,
                  "threadMon": 9.16, "oneYear": 89.73, "moreOneYear": 2.18}
        data17 = {"productName": "其他资产", "marketValueAmt": 4109.59, "dealCashFlow": 89.73, "undueCashFlow": 2.18,
                  "threadMon": 9.16, "oneYear": 89.73, "moreOneYear": 2.18}
        data18 = {"productName": "独立账户资产", "marketValueAmt": 4109.59, "dealCashFlow": 89.73, "undueCashFlow": 2.18,
                  "threadMon": 9.16, "oneYear": 89.73, "moreOneYear": 2.18}
        data19 = {"productName": "合计", "marketValueAmt": 4109.59, "dealCashFlow": 89.73, "undueCashFlow": 2.18,
                  "threadMon": 9.16, "oneYear": 89.73, "moreOneYear": 2.18}
        data20 = {"productName": "未到期责任准备金", "marketValueAmt": 4109.59, "dealCashFlow": 89.73, "undueCashFlow": 2.18,
                  "threadMon": 9.16, "oneYear": 89.73, "moreOneYear": 2.18}
        data21 = {"productName": "寿险责任准备金", "marketValueAmt": 4109.59, "dealCashFlow": 89.73, "undueCashFlow": 2.18,
                  "threadMon": 9.16, "oneYear": 89.73, "moreOneYear": 2.18}
        data22 = {"productName": "长期健康险责任准备金", "marketValueAmt": 4109.59, "dealCashFlow": 89.73, "undueCashFlow": 2.18,
                  "threadMon": 9.16, "oneYear": 89.73, "moreOneYear": 2.18}
        data23 = {"productName": "未决赔款责任准备金", "marketValueAmt": 4109.59, "dealCashFlow": 89.73, "undueCashFlow": 2.18,
                  "threadMon": 9.16, "oneYear": 89.73, "moreOneYear": 2.18}
        data24 = {"productName": "保户储金及投资款", "marketValueAmt": 4109.59, "dealCashFlow": 89.73, "undueCashFlow": 2.18,
                  "threadMon": 9.16, "oneYear": 89.73, "moreOneYear": 2.18}
        data25 = {"productName": "应付保户红利", "marketValueAmt": 4109.59, "dealCashFlow": 89.73, "undueCashFlow": 2.18,
                  "threadMon": 9.16, "oneYear": 89.73, "moreOneYear": 2.18}
        data26 = {"productName": "应付佣金及手续费", "marketValueAmt": 4109.59, "dealCashFlow": 89.73, "undueCashFlow": 2.18,
                  "threadMon": 9.16, "oneYear": 89.73, "moreOneYear": 2.18}
        data27 = {"productName": "应付款项", "marketValueAmt": 4109.59, "dealCashFlow": 89.73, "undueCashFlow": 2.18,
                  "threadMon": 9.16, "oneYear": 89.73, "moreOneYear": 2.18}
        data28 = {"productName": "卖出回购证券", "marketValueAmt": 4109.59, "dealCashFlow": 89.73, "undueCashFlow": 2.18,
                  "threadMon": 9.16, "oneYear": 89.73, "moreOneYear": 2.18}
        data29 = {"productName": "应付返售证券", "marketValueAmt": 4109.59, "dealCashFlow": 89.73, "undueCashFlow": 2.18,
                  "threadMon": 9.16, "oneYear": 89.73, "moreOneYear": 2.18}
        data30 = {"productName": "应付债券", "marketValueAmt": 4109.59, "dealCashFlow": 89.73, "undueCashFlow": 2.18,
                  "threadMon": 9.16, "oneYear": 89.73, "moreOneYear": 2.18}
        data31 = {"productName": "预计负债", "marketValueAmt": 4109.59, "dealCashFlow": 89.73, "undueCashFlow": 2.18,
                  "threadMon": 9.16, "oneYear": 89.73, "moreOneYear": 2.18}
        data32 = {"productName": "其他负债", "marketValueAmt": 4109.59, "dealCashFlow": 89.73, "undueCashFlow": 2.18,
                  "threadMon": 9.16, "oneYear": 89.73, "moreOneYear": 2.18}
        data33 = {"productName": "独立账户负债", "marketValueAmt": 4109.59, "dealCashFlow": 89.73, "undueCashFlow": 2.18,
                  "threadMon": 9.16, "oneYear": 89.73, "moreOneYear": 2.18}
        data34 = {"productName": "合计", "marketValueAmt": 4109.59, "dealCashFlow": 89.73, "undueCashFlow": 2.18,
                  "threadMon": 9.16, "oneYear": 89.73, "moreOneYear": 2.18}
        data35 = {"productName": "净现金流入", "marketValueAmt": 4109.59, "dealCashFlow": 89.73, "undueCashFlow": 2.18,
                  "threadMon": 9.16, "oneYear": 89.73, "moreOneYear": 2.18}
        data36 = {"productName": "综合流动比率", "marketValueAmt": 4109.59, "dealCashFlow": 89.73, "undueCashFlow": 2.18,
                  "threadMon": 9.16, "oneYear": 89.73, "moreOneYear": 2.18}
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
        data.append(data15)
        data.append(data16)
        data.append(data17)
        data.append(data18)
        data.append(data19)
        data.append(data20)
        data.append(data21)
        data.append(data22)
        data.append(data23)
        data.append(data24)
        data.append(data25)
        data.append(data26)
        data.append(data27)
        data.append(data28)
        data.append(data29)
        data.append(data30)
        data.append(data31)
        data.append(data32)
        data.append(data33)
        data.append(data34)
        data.append(data35)
        data.append(data36)
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
