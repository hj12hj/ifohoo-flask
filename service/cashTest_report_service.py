import datetime

from dateutil.relativedelta import relativedelta

from sql import cashTest_report_sql

"""
    现金流测试报表Service
"""
secuCategoryList = {"1": ["DBA", "EUM", "DBN"],
                    "2": ["DBF", "DDT"],
                    "3": ["DB", ],
                    "4": ["DDA", "DDT", "DB"],
                    "5": ["DBV", "DBVM", "ES", "EU"],
                    "6": [],
                    "7": [],
                    "8": ["EUF", "DBV", ],
                    "9": ["EUE"],
                    "10": ["DP"]

                    }

class CashTestReportService:

    def __init__(self):
        self.sql = cashTest_report_sql

    """
        现金流测试报表列表查询
    """

    def cashTest_report_list(self, query_data):
        datalist = self.sql.get_cashTest_report_list(query_data)
        settleDate = query_data.get("settleDate")
        now_quarter_date = self.__dealDate(settleDate).strftime('%Y-%m-%d')
        one_quarter_date = self.__get_three_month_Date(now_quarter_date).strftime('%Y-%m-%d')
        two_quarter_date = self.__get_three_month_Date(one_quarter_date).strftime('%Y-%m-%d')
        three_quarter_date = self.__get_three_month_Date(two_quarter_date).strftime('%Y-%m-%d')
        four_quarter_date = self.__get_three_month_Date(three_quarter_date).strftime('%Y-%m-%d')
        data_1 = self.__getAmount(self.__getData_by_type_no_list(datalist, "1"))
        data_1_1 = data_1-146377547.63

        data_3 = self.__getAmount(self.__getData_by_type_list(datalist, "3"))
        data_3_1 = self.__dealAmount(data_3, "3")
        data_3_2 = self.__getAmount(self.__getData_by_dueData_list(data_3, one_quarter_date))
        data_3_2_1 = self.__dealAmount(data_3_2, "3")
        data_3_3 = self.__getAmount(self.__getData_by_dueData_list(data_3, two_quarter_date))
        data_3_3_1 = self.__dealAmount(data_3_3, "3")
        data_3_4 = self.__getAmount(self.__getData_by_dueData_list(data_3, three_quarter_date))
        data_3_4_1 = self.__dealAmount(data_3_4, "3")
        data_3_5 = self.__getAmount(self.__getData_by_dueData_list(data_3, four_quarter_date))
        data_3_5_1 = self.__dealAmount(data_3_5, "3")

        data_4 = self.__getAmount(self.__getData_by_type_list(datalist, "4"))
        data_4_1 = self.__dealAmount(data_4, "4")
        data_4_2 = self.__getAmount(self.__getData_by_dueData_list(data_4, one_quarter_date))
        data_4_2_1 = self.__dealAmount(data_4_2, "4")
        data_4_3 = self.__getAmount(self.__getData_by_dueData_list(data_4, two_quarter_date))
        data_4_3_1 = self.__dealAmount(data_4_3, "4")
        data_4_4 = self.__getAmount(self.__getData_by_dueData_list(data_4, three_quarter_date))
        data_4_4_1 = self.__dealAmount(data_4_4, "4")
        data_4_5 = self.__getAmount(self.__getData_by_dueData_list(data_4, four_quarter_date))
        data_4_5_1 = self.__dealAmount(data_4_5, "4")


        data_5 = self.__getAmount(self.__getData_by_type_list(datalist, "5"))
        data_5_1 = self.__dealAmount(data_5, "5")
        data_5_2 = self.__getAmount(self.__getData_by_dueData_list(data_5, one_quarter_date))
        data_5_2_1 = self.__dealAmount(data_5_2, "5")
        data_5_3 = self.__getAmount(self.__getData_by_dueData_list(data_5, two_quarter_date))
        data_5_3_1 = self.__dealAmount(data_5_3, "5")
        data_5_4 = self.__getAmount(self.__getData_by_dueData_list(data_5, three_quarter_date))
        data_5_4_1 = self.__dealAmount(data_5_4, "5")
        data_5_5 = self.__getAmount(self.__getData_by_dueData_list(data_5, four_quarter_date))
        data_5_5_1 = self.__dealAmount(data_5_5, "5")

        data_9 = self.__getAmount(self.__getData_by_type_list(datalist, "9"))
        data_9_1 = self.__dealAmount(data_9, "9")
        data_9_2 = self.__getAmount(self.__getData_by_dueData_list(data_9, one_quarter_date))
        data_9_2_1 = self.__dealAmount(data_9_2, "9")
        data_9_3 = self.__getAmount(self.__getData_by_dueData_list(data_9, two_quarter_date))
        data_9_3_1 = self.__dealAmount(data_9_3, "9")
        data_9_4 = self.__getAmount(self.__getData_by_dueData_list(data_9, three_quarter_date))
        data_9_4_1 = self.__dealAmount(data_9_4, "9")
        data_9_5 = self.__getAmount(self.__getData_by_dueData_list(data_9, four_quarter_date))
        data_9_5_1 = self.__dealAmount(data_9_5, "9")

        data_10 = self.__getAmount(self.__getData_by_type_list(datalist, "10"))
        data_10_1 = self.__dealAmount(data_10, "10")
        data_10_2 = self.__getAmount(self.__getData_by_dueData_list(data_10, one_quarter_date))
        data_10_2_1 = self.__dealAmount(data_10_2, "10")
        data_10_3 = self.__getAmount(self.__getData_by_dueData_list(data_10, two_quarter_date))
        data_10_3_1 = self.__dealAmount(data_10_3, "10")
        data_10_4 = self.__getAmount(self.__getData_by_dueData_list(data_10, three_quarter_date))
        data_10_4_1 = self.__dealAmount(data_10_4, "10")
        data_10_5 = self.__getAmount(self.__getData_by_dueData_list(data_10, four_quarter_date))
        data_10_5_1 = self.__dealAmount(data_10_5, "10")


        data = []
        data1 = {"categoryType": "其他现金及流动性管理工具", "description": "不属于现金及现金等价物的现金及流动性管理工具，如央行票据、商业银行票据、货币市场基金、同业存单等。", "rate": "100%", "oneAmount": data_1,
                 "oneRateAmt": data_1, "twoAmount": data_1_1, "twoRateAmt": data_1_1, "threeAmount": data_1_1, "threeRateAmt": data_1_1, "fourAmount": data_1_1, "fourRateAmt": data_1_1, "fiveAmount": data_1_1, "fiveRateAmt": data_1_1}
        data2 = {"categoryType": "", "description": "划入可供出售金融资产或交易性金融资产的中央政府债", "rate": "95%", "oneAmount": 0,
                 "oneRateAmt": 0, "twoAmount": 0, "twoRateAmt": 0, "threeAmount": 0, "threeRateAmt": 0, "fourAmount": 0, "fourRateAmt": 0, "fiveAmount": 0, "fiveRateAmt": 0}
        data3 = {"categoryType": "", "description": "划入可供出售金融资产或交易性金融资产的省级政府债、准政府债、AAA 级的金融企业（公司）债；定期存款、协议存款", "rate": "95%", "oneAmount": data_3,
                "oneRateAmt": data_3_1, "twoAmount": data_3_2, "twoRateAmt": data_3_2_1, "threeAmount": data_3_3, "threeRateAmt": data_3_3_1, "fourAmount": data_3_4, "fourRateAmt": data_3_4_1, "fiveAmount": data_3_5, "fiveRateAmt": data_3_5_1}
        data4 = {"categoryType": "高流动性资产", "description": "划入可供出售金融资产或交易性金融资产的AAA级的非金融企业（公司）债；债券型基金", "rate": "85%", "oneAmount": data_4,
                 "oneRateAmt": data_4_1, "twoAmount": data_4_2, "twoRateAmt": data_4_2_1, "threeAmount": data_4_3, "threeRateAmt": data_4_3_1, "fourAmount": data_4_4, "fourRateAmt": data_4_4_1, "fiveAmount": data_4_5, "fiveRateAmt": data_4_5_1}
        data5 = {"categoryType": "", "description": "上市股票（不含举牌及计入长期股权投资的股票）；证券投资基金（不含货币市场基金、债券型基金）；可转债", "rate": "80%", "oneAmount": data_5,
                 "oneRateAmt": data_5_1, "twoAmount": data_5_2, "twoRateAmt": data_5_2_1, "threeAmount": data_5_3, "threeRateAmt": data_5_3_1, "fourAmount": data_5_4, "fourRateAmt": data_5_4_1, "fiveAmount": data_5_5, "fiveRateAmt": data_5_5_1}
        data6 = {"categoryType": "", "description": "划入持有至到期投资或贷款和应收款项的国债", "rate": "95%", "oneAmount": 0,
                 "oneRateAmt": 0, "twoAmount": 0, "twoRateAmt": 0, "threeAmount": 0, "threeRateAmt": 0, "fourAmount": 0, "fourRateAmt": 0, "fiveAmount": 0, "fiveRateAmt": 0}
        data7 = {"categoryType": "", "description": "划入持有至到期投资或贷款和应收款项的省级政府债、准政府债、AAA 级的金融企业（公司）债", "rate": "90%", "oneAmount": 0,
                 "oneRateAmt": 0, "twoAmount": 0, "twoRateAmt": 0, "threeAmount": 0, "threeRateAmt": 0, "fourAmount": 0, "fourRateAmt": 0, "fiveAmount": 0, "fiveRateAmt": 0}
        data8 = {"categoryType": "中低流动性资产", "description": "划入持有至到期投资或贷款和应收款项的AAA 级的非金融企业（公司）债", "rate": "85%", "oneAmount": 0,
                 "oneRateAmt": 0, "twoAmount": 0, "twoRateAmt": 0, "threeAmount": 0, "threeRateAmt": 0, "fourAmount": 0, "fourRateAmt": 0, "fiveAmount": 0, "fiveRateAmt": 0}
        data9 = {"categoryType": "", "description": "固定收益类保险资产管理产品、权益类保险资产管理产品", "rate": "75%", "oneAmount": data_9,
                 "oneRateAmt": data_9_1, "twoAmount": data_9_2, "twoRateAmt": data_9_2_1, "threeAmount": data_9_3, "threeRateAmt": data_9_3_1, "fourAmount": data_9_4, "fourRateAmt": data_9_4_1, "fiveAmount": data_9_5, "fiveRateAmt": data_9_5_1}
        data10 = {"categoryType": "", "description": "其他资产", "rate": "60%", "oneAmount": data_10,
                 "oneRateAmt": data_10_1, "twoAmount": data_10_2, "twoRateAmt": data_10_2_1, "threeAmount": data_10_3, "threeRateAmt": data_10_3_1, "fourAmount": data_10_4, "fourRateAmt": data_10_4_1, "fiveAmount": data_10_5, "fiveRateAmt": data_10_5_1}
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
    根据证券类型过滤
    '''

    def __getData_by_type_list(self, dataList, type):
        dataAll = []
        for data in dataList.get("list"):
            if data['secuCategoryCode'] in secuCategoryList.get(type):
                dataAll.append(data)
        return dataAll

    '''
    根据证券类型过滤
    '''

    def __getData_by_type_no_list(self, dataList, type):
        dataAll = []
        for data in dataList.get("list"):
            if data['secuCategoryCode'] not in secuCategoryList.get(type):
                dataAll.append(data)
        return dataAll

    '''
    根据证券到期日过滤
    '''

    def __getData_by_dueData_list(self, dataAll, dueDate):
        dataLastAll = []
        if dataAll > 0:
            for data in dataAll:
                if data['dueDate'] is None or data['dueDate'] == "":
                    dataLastAll.append(data)
                    continue
                elif data['dueDate'] > dueDate:
                    dataLastAll.append(data)
        return dataLastAll

    '''
    计算金额
    '''

    def __getAmount(self, dataList):
        count = 0
        for data in dataList:
            count += data["inveCost"]
        return count


    '''
    根据系数计算折算金额
    '''
    def __dealAmount(self, amount, type):
        rate = 1.0
        if type == "1":
            rate = 1.0
        elif type == "2":
            rate = 0.95
        elif type == "3":
            rate = 0.90
        elif type == "4":
            rate = 0.85
        elif type == "5":
            rate =0.80
        elif type == "6":
            rate = 0.75
        elif type == "7":
            rate = 0.60


        return amount * rate


    '''
    获取当前季度
    '''
    def __dealDate(self, settleDateStr):
        settleDate = datetime.datetime.strptime(settleDateStr, '%Y-%m-%d')
        month = (settleDate.month - 1) - (settleDate.month - 1) % 3 + 1
        if month == 10:
            newdate = datetime.datetime(settleDate.year + 1, 1, 1) + datetime.timedelta(days=-1)
        else:
            newdate = datetime.datetime(settleDate.year, month + 3, 1) + datetime.timedelta(days=-1)
        return newdate

    '''
    处理日期，settleDateStr日期3个月后日期
    '''
    def __get_three_month_Date(self, settleDateStr):
        settleDate = datetime.datetime.strptime(settleDateStr, '%Y-%m-%d')
        endDate = settleDate + relativedelta(months=3)
        return endDate
