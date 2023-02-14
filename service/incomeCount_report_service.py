import datetime

from sql import incomeCount_report_sql

"""
    收益率计算报表Service
"""

secuCategoryList = {"1": ["DDC", "DDN", "EUM", "DBFSM", "DPC", "DPO", "DBA", "DBN", "DRC"],
                    "2": ["DDA", "DDT"],
                    "3": ["DB", ],
                    "4": ["DDA", "DDT", "DB"],
                    "5": ["DBV", "DBVM", "ES", "EU"],
                    "6": [],
                    "7": [],
                    "8": ["EUF", "DBV", ],
                    "9": ["EUE"],
                    "10": ["DP"],
                    "11": ["DP"]

                    }

class IncomeCountReportService:

    def __init__(self):
        self.sql = incomeCount_report_sql

    """
        收益率计算报表列表查询
    """

    def incomeCount_report_list(self, query_data):
        settleDate = query_data.get("settleDate")
        days = self.__dealDate(settleDate)
        datalist = self.sql.get_incomeCount_report_list(query_data)

        dataAllList_1 = self.__getData_by_type_list(datalist, "1")
        data_1_tzsy = self.__getAmount(dataAllList_1);
        data_1_sjzygm = 1;
        data_1_pjzygm = data_1_sjzygm / days * 365
        data_1_zhtzsyl = data_1_tzsy / data_1_pjzygm
        data_1_nhsyl = data_1_tzsy / data_1_sjzygm

        dataAllList_2 = self.__getData_by_type_list(datalist, "2")
        data_2_tzsy = self.__getAmount(dataAllList_2);
        data_2_sjzygm = 1;
        data_2_pjzygm = data_2_sjzygm / days * 365
        data_2_zhtzsyl = data_2_tzsy / data_2_pjzygm
        data_2_nhsyl = data_2_tzsy / data_2_sjzygm

        dataAllList_3 = self.__getData_by_type_list(datalist, "3")
        data_3_tzsy = self.__getAmount(dataAllList_3);
        data_3_sjzygm = 1;
        data_3_pjzygm = data_3_sjzygm / days * 365
        data_3_zhtzsyl = data_3_tzsy / data_3_pjzygm
        data_3_nhsyl = data_3_tzsy / data_3_sjzygm

        dataAllList_5 = self.__getData_by_type_list(datalist, "5")
        data_5_tzsy = self.__getAmount(dataAllList_5);
        data_5_sjzygm = 1;
        data_5_pjzygm = data_5_sjzygm / days * 365
        data_5_zhtzsyl = data_5_tzsy / data_5_pjzygm
        data_5_nhsyl = data_5_tzsy / data_5_sjzygm

        dataAllList_7 = self.__getData_by_type_list(datalist, "7")
        data_7_tzsy = self.__getAmount(dataAllList_7);
        data_7_sjzygm = 1;
        data_7_pjzygm = data_7_sjzygm / days * 365
        data_7_zhtzsyl = data_7_tzsy / data_7_pjzygm
        data_7_nhsyl = data_7_tzsy / data_7_sjzygm

        dataAllList_8 = self.__getData_by_type_list(datalist, "8")
        data_8_tzsy = self.__getAmount(dataAllList_8);
        data_8_sjzygm = 1;
        data_8_pjzygm = data_8_sjzygm / days * 365
        data_8_zhtzsyl = data_8_tzsy / data_8_pjzygm
        data_8_nhsyl = data_8_tzsy / data_8_sjzygm

        dataAllList_11 = self.__getData_by_type_list(datalist, "11")
        data_11_tzsy = self.__getAmount(dataAllList_11);
        data_11_sjzygm = 1;
        data_11_pjzygm = data_11_sjzygm / days * 365
        data_11_zhtzsyl = data_11_tzsy / data_11_pjzygm
        data_11_nhsyl = data_11_tzsy / data_11_sjzygm


        data_14_tzsy = data_1_tzsy + data_2_tzsy + data_5_tzsy - data_11_tzsy;
        data_14_sjzygm = data_1_sjzygm + data_2_sjzygm + data_5_sjzygm - data_11_sjzygm;
        data_14_pjzygm = data_14_sjzygm / days * 365
        data_14_zhtzsyl = data_14_tzsy / data_14_pjzygm
        data_14_nhsyl = data_14_tzsy / data_14_sjzygm


        data = []
        data1 = {"positionNo": "1", "productName": "1、现金及流动性管理工具", "incomeRate": data_1_zhtzsyl, "incomeAmt": data_1_tzsy, "avgScale": data_1_pjzygm,
                 "realScale": data_1_sjzygm, "yearRate": data_1_nhsyl}
        data2 = {"positionNo": "2", "productName": "2、固定收益类投资资产", "incomeRate": data_2_zhtzsyl, "incomeAmt": data_2_tzsy, "avgScale": data_2_pjzygm,
                 "realScale": data_2_sjzygm, "yearRate": data_2_nhsyl}
        data3 = {"positionNo": "3", "productName": "2.1境内固定收益类投资资产", "incomeRate": data_3_zhtzsyl, "incomeAmt": data_3_tzsy, "avgScale": data_3_pjzygm,
                 "realScale": data_3_sjzygm, "yearRate": data_3_nhsyl}
        data4 = {"positionNo": "4", "productName": " 2.2境外固定收益类投资资产", "incomeRate": "", "incomeAmt": "", "avgScale": "",
                 "realScale": "", "yearRate": ""}
        data5 = {"positionNo": "5", "productName": "3、权益类投资资产", "incomeRate": data_5_zhtzsyl, "incomeAmt": data_5_tzsy, "avgScale": data_5_pjzygm,
                 "realScale": data_5_sjzygm, "yearRate": data_5_nhsyl}
        data6 = {"positionNo": "6", "productName": "3.1境内长期股权投资", "incomeRate": "", "incomeAmt": "", "avgScale": "",
                 "realScale": "", "yearRate": ""}
        data7 = {"positionNo": "7", "productName": "3.2境内不含长期股权投资的上市股票和基金", "incomeRate": data_7_zhtzsyl, "incomeAmt": data_7_tzsy, "avgScale": data_7_pjzygm,
                 "realScale": data_7_sjzygm, "yearRate": data_7_nhsyl}
        data8 = {"positionNo": "8", "productName": "3.3境内不含长期股权投资的其他权益投资资产", "incomeRate": data_8_zhtzsyl, "incomeAmt": data_8_tzsy, "avgScale": data_8_pjzygm,
                 "realScale": data_8_sjzygm, "yearRate": data_8_nhsyl}
        data9 = {"positionNo": "9", "productName": "3.4境外权益类投资", "incomeRate": "", "incomeAmt": "", "avgScale": "",
                 "realScale": "", "yearRate": ""}
        data10 = {"positionNo": "10", "productName": "4、投资性房地产", "incomeRate": "", "incomeAmt": "", "avgScale": "",
                 "realScale": "", "yearRate": ""}
        data11 = {"positionNo": "11`", "productName": "另：卖出回购证券", "incomeRate": data_11_zhtzsyl, "incomeAmt": data_11_tzsy, "avgScale": data_11_pjzygm,
                 "realScale": data_11_sjzygm, "yearRate": data_11_nhsyl}
        data12 = {"positionNo": "12", "productName": "贷款", "incomeRate": "", "incomeAmt": "", "avgScale": "",
                 "realScale": "", "yearRate": ""}
        data13 = {"positionNo": "13", "productName": "金融衍生工具", "incomeRate": "", "incomeAmt": "", "avgScale": "",
                  "realScale": "", "yearRate": ""}
        data14 = {"positionNo": "14", "productName": "资金运用净额", "incomeRate": data_14_zhtzsyl, "incomeAmt": data_14_tzsy, "avgScale": data_14_pjzygm,
                  "realScale": data_14_sjzygm, "yearRate": data_14_nhsyl}

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
    计算金额
    '''
    def __getAmount(self, dataList):
        count = 0
        for data in dataList:
            count += data["inveCost"] + data["inveCost"] + data["inveCost"]
        return count


    '''
    处理日期，当前日期和去年年底日期相差天数
    '''
    def __dealDate(self,settleDateStr):
        settleDate = datetime.datetime.strptime(settleDateStr, '%Y-%m-%d')
        lastYearEndDate = datetime.datetime(int(settleDate.year) - 1, 12, 31)
        return (settleDate - lastYearEndDate).days
