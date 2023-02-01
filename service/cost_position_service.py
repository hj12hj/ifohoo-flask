import json

from feign.data_center_feign_client import findCurrencyMap
from sql import cost_position_sql

"""
    每日持仓service
"""


class CostPositionService:

    def __init__(self):
        self.sql = cost_position_sql

    """
        每日持仓列表查询
    """

    def get_cost_position_list(self, query_data):
        currencyMap = json.loads(findCurrencyMap()).get("returnData")
        returnData = self.sql.get_cost_position_list(query_data)
        self.__transform_name(returnData=returnData, currencyMap=currencyMap)

        return returnData

    """
    转换名称
    """

    def __transform_name(self, returnData, currencyMap):
        for data in returnData.get("list"):
            data["tradeCurrencyCode"] = currencyMap.get(data["tradeCurrencyCode"])
            data["settleCurrencyCode"] = currencyMap.get(data["settleCurrencyCode"])
