import datetime

from sql import income_calculation_report_sql, insurance_profit_calculation_sql

"""
    短期债券报表Service
"""


class InsuranceProfitCalculationService:

    def __init__(self):
        self.sql = insurance_profit_calculation_sql

    """
        短期债券报表列表查询
    """

    def profit_calculation_report_list(self, query_data):
        datalist = self.sql.get_profit_calculation_report_list(query_data)
        returnData = []
        data1_1 = []
        data1_2 = []
        data1_3 = []
        data1_4 = []
        data1_5 = []
        data2_1 = []
        data2_2 = []
        data2_3 = []
        data2_4 = []
        data3_1 = []
        data3_2 = []
        data3_3 = []
        data4_1 = []
        data5_1 = []
        data1 = []
        data2 = []
        data3 = []
        data4 = []
        data5 = []
        row1 = {"secuName": "1. 固定收益类", }
        row2 = {"secuName": "    1.1 保证金存款", }
        data1.append(row1), data1.append(row2)
        row3 = {"secuName": "2. 现金及流动性管理工具", }
        row4 = {"secuName": "   2. 1 现金", }
        data2.append(row3), data2.append(row4)
        row5 = {"secuName": "3 .权益类", }
        data3.append(row5)
        row6 = {"secuName": "4 其它金融产品", }
        data4.append(row6)
        row7 = {"secuName": "5 不动产类资产", }
        data5.append(row7)
        print(datalist.get("list"))
        for data in datalist.get("list"):
            if(data["secuCategoryCode"] == "BZJCK"):  #保证金存款
                data1_1.append(data)
            elif(data["secuCategoryCode"] == "DDT"): #协议/定期存款
                data1_2.append(data)
            elif (data["secuCategoryCode"] == "DDN"): #通知存款
                data1_3.append(data)
            elif (data["secuCategoryCode"] == "BXZGCP"):  #保险资管产品
                data1_4.append(data)
            elif (data["secuCategoryCode"] == "DB"): #债券（委托）
                data1_5.append(data)
            elif(data["secuCategoryCode"] == "DDC"): #现金
                data2_1.append(data)
            elif (data["secuCategoryCode"] == "EUM"): #货币市场基金
                data2_2.append(data)
            elif (data["secuCategoryCode"] == "BXZGCP"): #货币市场类资管产品
                data2_3.append(data)
            elif (data["secuCategoryCode"] == "DP"): #回购
                data2_4.append(data)
            elif(data["secuCategoryCode"].startWith("EU")):
                if(data["secuCategoryCode"] != "EUM"):  #权益类 基金
                    data3_1.append(data)
            elif (data["secuCategoryCode"] == "ZGCP"):  #权益类 资管产品
                data3_2.append(data)
            elif (data["secuCategoryCode"] == "GPYJJWT"): #权益类 股票与基金（委托）
                data3_3.append(data)
            elif (data["secuCategoryCode"] == "EWE"): #其它金融产品
                data4_1.append(data)
            elif (data["secuCategoryCode"] == "BDC"): #不动产
                data5_1.append(data)

        returnData.append(row1)
        returnData.append(row2)
        returnData.append(row3)
        returnData.append(row4)
        returnData.append(row5)
        returnData.append(row6)
        returnData.append(row7)
        datalist["list"] = returnData
        return datalist


