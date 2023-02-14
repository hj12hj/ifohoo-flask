from datetime import datetime, timedelta
import datetime as dt
from feign.data_center_feign_client import findSecuCategoryMap
from sql import assetDetail_report_sql
import json

"""
    资产明细报表Service
"""

type_list = {"1.1": ["DDC", "DDN", "EUM", "DBFSM", "DPC", "DPO", "DBA", "DBN", "DRC"],
             "2.1.1": ["DDA", "DDT", "DBFM", "DBFEM", "DBFTM", "DBFSA", "DBFES", "DBFTS", "DBFSS"],
             "2.1.3": ["DBCA"],
             "2.1.3.1": ["EWE"],
             "3.1.1": ["ES", "ESC", "ESP", "ESV"],
             "3.1.2": ["EUN", "EUE", "EUL", "EUF", "EUQ", "EUG", "EUGD", "EUGE"],
             "3.1.4": ["DBV", "DBVM"]
             }

dict_invest1 = {'investType': "1、现金及流动性管理工具"}
dict_invest2 = {'investType': "1.1境内现金及流动性管理工具"}
dict_invest3 = {'investType': "1.2境外现金及流动性管理工具"}
dict_invest4 = {'investType': "2、固定收益类投资资产"}
dict_invest5 = {'investType': "2.1境内固定收益类投资资产"}
dict_invest6 = {'investType': "2.1.1传统固定收益类投资资产"}
dict_invest7 = {'investType': "其中：剩余期限不超过1年的政府债券、准政府债券"}
dict_invest8 = {'investType': "其中：债券型基金"}
dict_invest9 = {'investType': "2.1.2非标准固定收益类投资资产"}
dict_invest10 = {'investType': "2.1.2.1固定收益类保险资产管理产品"}
dict_invest11 = {'investType': "2.1.2.2另类保险资产管理产品"}
dict_invest12 = {'investType': "2.1.2.3项目资产支持计划"}
dict_invest13 = {'investType': "2.1.2.4基础设施债权投资计划"}
dict_invest14 = {'investType': "2.1.2.5不动产债权投资计划"}
dict_invest15 = {'investType': "2.1.2.6其他产品"}
dict_invest16 = {'investType': "2.1.3其他固定收益类金融产品"}
dict_invest17 = {'investType': "       其中：融资类信托计划"}
dict_invest18 = {'investType': "2.1.4含保证条款的权益类投资资产"}
dict_invest19 = {'investType': "      其中：优先股债务融资工具"}
dict_invest20 = {'investType': "      其中：基础资产为投资性房地产的含保证条款的权益投资资产"}
dict_invest21 = {'investType': "      其中：基础资产为基础设施的含保证条款的权益投资资产"}
dict_invest22 = {'investType': "2.2境外固定收益类投资资产"}
dict_invest23 = {'investType': "其中：剩余期限不超过1年的政府债券、国际金融组织债券、公司债券"}
dict_invest24 = {'investType': "其中：不具有银行保本承诺的结构性存款"}
dict_invest25 = {'investType': "3、权益类投资资产"}
dict_invest26 = {'investType': "3.1境内权益类投资资产"}
dict_invest27 = {'investType': "其中：境内直接投资股权和间接投资股权形成的长期股权投资"}
dict_invest28 = {'investType': "其中：以自有资金对保险类企业的股权投资"}
dict_invest29 = {'investType': "3.1.1 上市普通股票"}
dict_invest30 = {'investType': "3.1.2 证券投资基金（不含货币市场基金、债券型基金）"}
dict_invest31 = {'investType': "3.1.3 优先股权益融资工具"}
dict_invest32 = {'investType': "3.1.4 可转债"}
dict_invest33 = {'investType': "3.1.5 未上市企业股权"}
dict_invest34 = {'investType': "3.1.6 不含保证条款的权益类和混合类保险资产管理产品"}
dict_invest35 = {'investType': "3.1.7 不含保证条款的股权投资计划、私募股权投资基金"}
dict_invest36 = {'investType': "      其中：基础资产为投资性房地产的不含保证条款的股权投资计划、私募股权投资基金"}
dict_invest37 = {'investType': "      其中：基础资产为基础设施的不含保证条款的股权投资计划、私募股权投资基金"}
dict_invest38 = {'investType': "3.1.8权益类信托计划"}
dict_invest39 = {'investType': "      其中：基础资产为投资性房地产的权益类信托计划"}
dict_invest40 = {'investType': "3.1.9其他权益类资产"}
dict_invest41 = {'investType': "      其中：基础资产为投资性房地产的其他权益类资产"}
dict_invest42 = {'investType': "3.2境外权益类投资资产"}
dict_invest43 = {'investType': "其中：境外直接投资股权和间接投资股权形成的长期股权投资"}
dict_invest44 = {'investType': "其中：以自有资金对保险类企业的股权投资"}
dict_invest45 = {'investType': "3.2.1 普通股"}
dict_invest46 = {'investType': "3.2.2证券投资基金（不含货币市场基金、债券型基金）"}
dict_invest47 = {'investType': "3.2.3 优先股权益融资工具"}
dict_invest48 = {'investType': "3.2.4 可转债"}
dict_invest49 = {'investType': "3.2.5 全球存托凭证、美国存托凭证"}
dict_invest50 = {'investType': "3.2.6 房地产信托投资基金（REITs）"}
dict_invest51 = {'investType': "3.2.7 未上市企业股权"}
dict_invest52 = {'investType': "3.2.8 股权投资基金"}
dict_invest53 = {'investType': "3.2.9 其他权益类资产"}
dict_invest54 = {'investType': "4、投资性房地产"}
dict_invest55 = {'investType': "4.1境内投资性房地产"}
dict_invest56 = {'investType': "4.2境外投资性房地产"}
dict_invest57 = {'investType': "投资资产合计"}
dict_invest58 = {'investType': "另：卖出回购证券"}
dict_invest59 = {'investType': "投资资产净额"}
dict_invest60 = {'investType': "贷款"}
dict_invest61 = {'investType': "其中：保户质押贷款"}
dict_invest62 = {'investType': "其中：向不动产项目公司提供的股东借款"}
dict_invest63 = {'investType': "金融衍生工具"}
dict_invest64 = {'investType': "资金运用余额"}
dict_invest65 = {'investType': "资金运用净额"}
dict_invest66 = {'investType': "自用性不动产"}


class AssetDetailReportService:

    def __init__(self):
        self.sql = assetDetail_report_sql

    """
        资产明细报表列表查询
    """

    def assetDetail_report_list(self, query_data):
        rowKey = 1

        list_all = []

        # 定义固定的投资种类
        type_map = {"1.1": [], "2.1.1": [], "2.1.3": [], "2.1.3.1": [], "3.1.1": [], "3.1.2": [], "3.1.4": []}

        datalist = self.sql.get_assetDetail_report_list(query_data)
        # queryDate = query_data.get("settleDate")

        for data in datalist:
            if data["secuCategoryCode"] in type_list.get("1.1"):
                type_map.get("1.1").append(data)
            elif data["secuCategoryCode"] in type_list.get("2.1.1"):
                type_map.get("2.1.1").append(data)
            elif data["secuCategoryCode"] in type_list.get("2.1.3"):
                type_map.get("2.1.3").append(data)
            elif data["secuCategoryCode"] in type_list.get("2.1.3.1"):
                type_map.get("2.1.3.1").append(data)
            elif data["secuCategoryCode"] in type_list.get("3.1.1"):
                type_map.get("3.1.1").append(data)
            elif data["secuCategoryCode"] in type_list.get("3.1.2"):
                type_map.get("3.1.2").append(data)
            elif data["secuCategoryCode"] in type_list.get("3.1.4"):
                type_map.get("3.1.4").append(data)
        list_all.append(dict_invest1)
        list_all.append(dict_invest2)
        list_all.extend(type_map.get("1.1"))
        list_all.append(dict_invest3)
        list_all.append(dict_invest4)
        list_all.append(dict_invest5)
        list_all.append(dict_invest6)
        list_all.extend(type_map.get("2.1.1"))
        list_all.append(dict_invest7)
        list_all.append(dict_invest8)
        list_all.append(dict_invest9)
        list_all.append(dict_invest10)
        list_all.append(dict_invest11)
        list_all.append(dict_invest12)
        list_all.append(dict_invest13)
        list_all.append(dict_invest14)
        list_all.append(dict_invest15)
        list_all.append(dict_invest16)
        list_all.extend(type_map.get("2.1.3"))
        list_all.append(dict_invest17)
        list_all.extend(type_map.get("2.1.3.1"))
        list_all.append(dict_invest18)
        list_all.append(dict_invest19)
        list_all.append(dict_invest20)
        list_all.append(dict_invest21)
        list_all.append(dict_invest22)
        list_all.append(dict_invest23)
        list_all.append(dict_invest24)
        list_all.append(dict_invest25)
        list_all.append(dict_invest26)
        list_all.append(dict_invest27)
        list_all.append(dict_invest28)
        list_all.append(dict_invest29)
        list_all.extend(type_map.get("3.1.1"))
        list_all.append(dict_invest30)
        list_all.append(dict_invest31)
        list_all.append(dict_invest32)
        list_all.extend(type_map.get("3.1.4"))
        list_all.append(dict_invest33)
        list_all.append(dict_invest34)
        list_all.append(dict_invest35)
        list_all.append(dict_invest36)
        list_all.append(dict_invest37)
        list_all.append(dict_invest38)
        list_all.append(dict_invest39)
        list_all.append(dict_invest40)
        list_all.append(dict_invest41)
        list_all.append(dict_invest42)
        list_all.append(dict_invest43)
        list_all.append(dict_invest44)
        list_all.append(dict_invest45)
        list_all.append(dict_invest46)
        list_all.append(dict_invest47)
        list_all.append(dict_invest48)
        list_all.append(dict_invest49)
        list_all.append(dict_invest50)
        list_all.append(dict_invest51)
        list_all.append(dict_invest52)
        list_all.append(dict_invest53)
        list_all.append(dict_invest54)
        list_all.append(dict_invest55)
        list_all.append(dict_invest56)
        list_all.append(dict_invest57)
        list_all.append(dict_invest58)
        list_all.append(dict_invest59)
        list_all.append(dict_invest60)
        list_all.append(dict_invest61)
        list_all.append(dict_invest62)
        list_all.append(dict_invest63)
        list_all.append(dict_invest64)
        list_all.append(dict_invest65)
        list_all.append(dict_invest66)

        secuCategoryMap = json.loads(findSecuCategoryMap()).get("returnData")
        self.__transform_name(returnData=list_all, secuCategoryMap=secuCategoryMap)
        for list in list_all:
            list["assetDetailNo"] = rowKey
            rowKey += 1
            if "investType" not in list:
                list["eoqBalance"] = list["inveCost"]
                # list["eoqBalance"] = self.sql.get_face_value_list(list["secuGlobalCode"],
                #                                         self.__quarter_end(queryDate)[0])
                # list["lastEoqBalance"] = self.sql.get_face_value_list(list["secuGlobalCode"],
                #                                                      self.__quarter_end(queryDate)[1])
                # list["lastYearEoqBalance"] = self.sql.get_face_value_list(list["secuGlobalCode"],
                #                                                      self.__quarter_end(queryDate)[2])

        return {"list": list_all}

    """
        转换名称-将证券类别的code转成name
    """

    def __transform_name(self, returnData, secuCategoryMap):
        for data in returnData:
            if "secuCategoryCode" in data:
                data["secuCategoryCode"] = secuCategoryMap.get(data["secuCategoryCode"])

    """
        根据传入的时间获取当前季度末，上个季度末，去年年末
    """

    def __quarter_end(self, currentDate):
        YYYYmmdd = '%Y-%m-%d'
        day = dt.datetime.strptime(currentDate, "%Y-%m-%d")
        # 本季最后一天
        month = (day.month - 1) - (day.month - 1) % 3 + 1
        this_quarter_end_time = dt.datetime(day.year, month + 3, 1) - timedelta(days=1) + dt.timedelta(
            hours=23, minutes=59, seconds=59)
        this_quarter_end = this_quarter_end_time.strftime(YYYYmmdd)
        # 本季第一天
        this_quarter_start = dt.datetime(day.year, month, 1)
        # 上季最后一天
        last_quarter_end_time = this_quarter_start - timedelta(days=1) + dt.timedelta(hours=23, minutes=59,
                                                                                      seconds=59)
        last_quarter_end = last_quarter_end_time.strftime(YYYYmmdd)

        # 本年第一天
        this_year_start = dt.datetime(day.year, 1, 1)
        # 上年最后一天
        last_year_end_time = this_year_start - timedelta(days=1) + dt.timedelta(hours=23, minutes=59, seconds=59)
        last_year_end = last_year_end_time.strftime(YYYYmmdd)
        # 存放顺序：当前季度末，上个季度末，去年年末
        return [this_quarter_end, last_quarter_end, last_year_end]
