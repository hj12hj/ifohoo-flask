import datetime
from dateutil.relativedelta import relativedelta
from sql import flowRate_report_sql

"""
    综合流动比率报表Service
"""
secuCategoryList = {"1": ["DDC", "DDN", "EUM", "DBFSM", "DPC", "DPO", "DBA", "DBN", "DRC"],
                    "3": ["DDA", "DDT"],
                    "4": ["DBG", "DBD", "DBDM"],
                    "5": ["DBF", "DBFM"],
                    "6": ["DBE", "DBEM"],
                    "8": ["EUF", "DBV", ],
                    "9": ["EUE"],
                    "10": ["DP"],
                    "28": ["DP"]

                    }

class FlowRateReportService:

    def __init__(self):
        self.sql = flowRate_report_sql

    """
        综合流动比率报表列表查询
    """

    def flowRate_report_list(self, query_data):
        settleDate = query_data.get("settleDate")
        #3个月后日期
        threeMonthDate = self.__get_three_month_Date(settleDate).strftime('%Y-%m-%d')
        #一年后日期
        lastYearDate = self.__get_last_year_Date(settleDate).strftime('%Y-%m-%d')
        datalist = self.sql.get_flowRate_report_list(query_data)

        data_1_amt = self.__getData_by_type_list(datalist, "1")

        data_3_amt = self.__getData_by_type_list(datalist, "3")
        data_3_threeMonth = self.__getData_by_dueData_list(data_3_amt, threeMonthDate)
        data_3_yearIn = self.__getData_by_dueData_list(data_3_amt, lastYearDate)
        data_3_yearOut = self.__getData_by_dueData_year_list(data_3_amt, lastYearDate)

        data_4_amt = self.__getData_by_type_list(datalist, "4")
        data_4_threeMonth = self.__getData_by_dueData_list(data_4_amt, threeMonthDate)
        data_4_yearIn = self.__getData_by_dueData_list(data_4_amt, lastYearDate)
        data_4_yearOut = self.__getData_by_dueData_year_list(data_4_amt, lastYearDate)

        data_5_amt = self.__getData_by_type_list(datalist, "5")
        data_5_threeMonth = self.__getData_by_dueData_list(data_5_amt, threeMonthDate)
        data_5_yearIn = self.__getData_by_dueData_list(data_5_amt, lastYearDate)
        data_5_yearOut = self.__getData_by_dueData_year_list(data_5_amt, lastYearDate)

        data_6_amt = self.__getData_by_type_list(datalist, "6")
        data_6_threeMonth = self.__getData_by_dueData_list(data_6_amt, threeMonthDate)
        data_6_yearIn = self.__getData_by_dueData_list(data_6_amt, lastYearDate)
        data_6_yearOut = self.__getData_by_dueData_year_list(data_6_amt, lastYearDate)

        data_28_amt = self.__getData_by_type_list(datalist, "28")
        data_28_threeMonth = self.__getData_by_dueData_list(data_28_amt, threeMonthDate)
        data_28_yearIn = self.__getData_by_dueData_list(data_28_amt, lastYearDate)
        data_28_yearOut = self.__getData_by_dueData_year_list(data_28_amt, lastYearDate)




        data = []
        data1 = {"flowRateNo": 1, "productName": "现金及现金等价物", "marketValueAmt": self.__deal_list_count(data_1_amt), "dealCashFlow": "", "undueCashFlow": "",
                 "threadMon": threeMonthDate, "oneYear": lastYearDate, "moreOneYear": lastYearDate}
        data2 = {"flowRateNo": 2, "productName": "投资资产：", "marketValueAmt": "", "dealCashFlow": "", "undueCashFlow": "",
                 "threadMon": "", "oneYear": "", "moreOneYear": ""}
        data3 = {"productName": "定期存款和协议存款", "marketValueAmt": self.__deal_list_count(data_3_amt), "dealCashFlow": "", "undueCashFlow": "",
                 "threadMon": self.__deal_list_count(data_3_threeMonth), "oneYear": self.__deal_list_count(data_3_yearIn), "moreOneYear": self.__deal_list_count(data_3_yearOut)}
        data4 = {"productName": "政府债券", "marketValueAmt": self.__deal_list_count(data_4_amt), "dealCashFlow": "", "undueCashFlow": "",
                 "threadMon": self.__deal_list_count(data_4_threeMonth), "oneYear": self.__deal_list_count(data_4_yearIn), "moreOneYear": self.__deal_list_count(data_4_yearOut)}
        data5 = {"productName": "金融债", "marketValueAmt": self.__deal_list_count(data_5_amt), "dealCashFlow": "", "undueCashFlow": "",
                 "threadMon": self.__deal_list_count(data_5_threeMonth), "oneYear": self.__deal_list_count(data_5_yearIn), "moreOneYear": self.__deal_list_count(data_5_yearOut)}
        data6 = {"productName": "企业债券", "marketValueAmt": self.__deal_list_count(data_6_amt), "dealCashFlow": "", "undueCashFlow": "",
                 "threadMon": self.__deal_list_count(data_6_threeMonth), "oneYear": self.__deal_list_count(data_6_yearIn), "moreOneYear": self.__deal_list_count(data_6_yearOut)}
        data7 = {"productName": "资产证券化产品", "marketValueAmt": "", "dealCashFlow": "", "undueCashFlow": "",
                 "threadMon": "", "oneYear": "", "moreOneYear": ""}
        data8 = {"productName": "信托资产", "marketValueAmt": "", "dealCashFlow": "", "undueCashFlow": "",
                 "threadMon": "", "oneYear": "", "moreOneYear": ""}
        data9 = {"productName": "基础设施投资", "marketValueAmt": "", "dealCashFlow": "", "undueCashFlow": "",
                 "threadMon": "", "oneYear": "", "moreOneYear": ""}
        data10 = {"productName": "保险资产管理产品", "marketValueAmt": "", "dealCashFlow": "", "undueCashFlow": "",
                  "threadMon": "", "oneYear": "", "moreOneYear": ""}
        data11 = {"productName": "权益投资", "marketValueAmt": "", "dealCashFlow": "", "undueCashFlow": "",
                  "threadMon": "", "oneYear": "", "moreOneYear": ""}
        data12 = {"productName": "贷款", "marketValueAmt": "", "dealCashFlow": "", "undueCashFlow": "",
                  "threadMon": "", "oneYear": "", "moreOneYear": ""}
        data13 = {"productName": "投资性不动产", "marketValueAmt": "", "dealCashFlow": "", "undueCashFlow": "",
                  "threadMon": "", "oneYear": "", "moreOneYear": ""}
        data14 = {"productName": "衍生金融工具", "marketValueAmt": "", "dealCashFlow": "", "undueCashFlow": "",
                  "threadMon": "", "oneYear": "", "moreOneYear": ""}
        data15 = {"productName": "其他投资资产", "marketValueAmt": "", "dealCashFlow": "", "undueCashFlow": "",
                  "threadMon": "", "oneYear": "", "moreOneYear": ""}
        data16 = {"productName": "应收款项", "marketValueAmt": "", "dealCashFlow": "", "undueCashFlow": "",
                  "threadMon": "", "oneYear": "", "moreOneYear": ""}
        data17 = {"productName": "其他资产", "marketValueAmt": "", "dealCashFlow": "", "undueCashFlow": "",
                  "threadMon": "", "oneYear": "", "moreOneYear": ""}
        data18 = {"productName": "独立账户资产", "marketValueAmt": "", "dealCashFlow": "", "undueCashFlow": "",
                  "threadMon": "", "oneYear": "", "moreOneYear": ""}
        data19 = {"productName": "合计", "marketValueAmt": "", "dealCashFlow": "", "undueCashFlow": "",
                  "threadMon": "", "oneYear": "", "moreOneYear": ""}
        data20 = {"productName": "未到期责任准备金", "marketValueAmt": "", "dealCashFlow": "", "undueCashFlow": "",
                  "threadMon": "", "oneYear": "", "moreOneYear": ""}
        data21 = {"productName": "寿险责任准备金", "marketValueAmt": "", "dealCashFlow": "", "undueCashFlow": "",
                  "threadMon": "", "oneYear": "", "moreOneYear": ""}
        data22 = {"productName": "长期健康险责任准备金", "marketValueAmt": "", "dealCashFlow": "", "undueCashFlow": "",
                  "threadMon": "", "oneYear": "", "moreOneYear": ""}
        data23 = {"productName": "未决赔款责任准备金", "marketValueAmt": "", "dealCashFlow": "", "undueCashFlow": "",
                  "threadMon": "", "oneYear": "", "moreOneYear": ""}
        data24 = {"productName": "保户储金及投资款", "marketValueAmt": "", "dealCashFlow": "", "undueCashFlow": "",
                  "threadMon": "", "oneYear": "", "moreOneYear": ""}
        data25 = {"productName": "应付保户红利", "marketValueAmt": "", "dealCashFlow": "", "undueCashFlow": "",
                  "threadMon": "", "oneYear": "", "moreOneYear": ""}
        data26 = {"productName": "应付佣金及手续费", "marketValueAmt": "", "dealCashFlow": "", "undueCashFlow": "",
                  "threadMon": "", "oneYear": "", "moreOneYear": ""}
        data27 = {"productName": "应付款项", "marketValueAmt": "", "dealCashFlow": "", "undueCashFlow": "",
                  "threadMon": "", "oneYear": "", "moreOneYear": ""}
        data28 = {"productName": "卖出回购证券", "marketValueAmt": self.__deal_list_count(data_28_amt), "dealCashFlow": "", "undueCashFlow": "",
                  "threadMon": self.__deal_list_count(data_28_threeMonth), "oneYear": self.__deal_list_count(data_28_yearIn), "moreOneYear": self.__deal_list_count(data_28_yearOut)}
        data29 = {"productName": "应付返售证券", "marketValueAmt": "", "dealCashFlow": "", "undueCashFlow": "",
                  "threadMon": "", "oneYear": "", "moreOneYear": ""}
        data30 = {"productName": "应付债券", "marketValueAmt": "", "dealCashFlow": "", "undueCashFlow": "",
                  "threadMon": "", "oneYear": "", "moreOneYear": ""}
        data31 = {"productName": "预计负债", "marketValueAmt": "", "dealCashFlow": "", "undueCashFlow": "",
                  "threadMon": "", "oneYear": "", "moreOneYear": ""}
        data32 = {"productName": "其他负债", "marketValueAmt": "", "dealCashFlow": "", "undueCashFlow": "",
                  "threadMon": "", "oneYear": "", "moreOneYear": ""}
        data33 = {"productName": "独立账户负债", "marketValueAmt": "", "dealCashFlow": "", "undueCashFlow": "",
                  "threadMon": "", "oneYear": "", "moreOneYear": ""}
        data34 = {"productName": "合计", "marketValueAmt": "", "dealCashFlow": "", "undueCashFlow": "",
                  "threadMon": "", "oneYear": "", "moreOneYear": ""}
        data35 = {"productName": "净现金流入", "marketValueAmt": "", "dealCashFlow": "", "undueCashFlow": "",
                  "threadMon": "", "oneYear": "", "moreOneYear": ""}
        data36 = {"productName": "综合流动比率", "marketValueAmt": "", "dealCashFlow": "", "undueCashFlow": "",
                  "threadMon": "", "oneYear": "", "moreOneYear": ""}
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
    根据证券类型过滤
    '''
    def __getData_by_type_list(self, dataList, type):
        dataAll = []
        for data in dataList.get("list"):
            if data['secuCategoryCode'] in secuCategoryList.get(type):
                dataAll.append(data)
        return dataAll


    '''
    根据证券到期日过滤(3个月内和1年内)
    '''
    def __getData_by_dueData_list(self, dataAll, dueDate):
        dataLastAll = []
        if len(dataAll) > 0:
            for data in dataAll:
                if data['dueDate'] is None or data['dueDate'] == "":
                    continue
                elif data['dueDate'] <= dueDate:
                    dataLastAll.append(data)
        return dataLastAll

    '''
    根据证券到期日过滤(1年以上)
    '''
    def __getData_by_dueData_year_list(self, dataAll, dueDate):
        dataLastAll = []
        if len(dataAll) > 0:
            for data in dataAll:
                if data['dueDate'] is None or data['dueDate'] == "":
                    dataLastAll.append(data)
                    continue
                elif data['dueDate'] > dueDate:
                    dataLastAll.append(data)
        return dataLastAll

    '''
    处理数据库获取数据
    '''
    def __deal_list_count(self, dataAll):
        count = 0
        for data in dataAll:
            count += data["inveCost"]
        return count


    '''
    处理日期，当前日期3个月后天数
    '''
    def __get_three_month_Date(self, settleDateStr):
        settleDate = datetime.datetime.strptime(settleDateStr, '%Y-%m-%d')
        endDate = settleDate + relativedelta(months=3)
        return endDate


    '''
    处理日期，当前日期和去年年底日期相差天数
    '''
    def __get_last_year_Date(self, settleDateStr):
        settleDate = datetime.datetime.strptime(settleDateStr, '%Y-%m-%d')
        lastYearEndDate = datetime.datetime(int(settleDate.year) - 1, settleDate.month, settleDate.day)
        return lastYearEndDate
