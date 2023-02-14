from datetime import datetime, timedelta
import datetime as dt

from sql import insurance_profit_calculation_sql

"""
    短期债券报表Service
"""


class InsuranceProfitCalculationService:

    def __init__(self):
        self.sql = insurance_profit_calculation_sql

    """
        保险收益测算表查询
    """

    def profit_calculation_report_list(self, query_data):

        queryDate = query_data.get("settleDate")
        if(queryDate == None):
            queryDate = dt.date.today().strftime('%Y-%m-%d')
        fundsDataReturn = self.sql.get_funds_list(queryDate, self.__quarter_end(queryDate))
        investDataReturn = self.sql.get_security_invest_list(queryDate, self.__quarter_end(queryDate))

        lineRecordMap = {}
        self.__init_lineRecordMap(lineRecordMap)

        self.__calculation_by_dbData(fundsDataReturn, lineRecordMap)
        self.__calculation_by_dbData(investDataReturn, lineRecordMap)

        hjLineRecord = lineRecordMap["hj"]
        wttzzhjLineRecord = lineRecordMap["wttzzh"]
        for key in lineRecordMap.keys():
            lineRecord = lineRecordMap[key]
            if(key == "wttzzh"):
                wttzzhjLineRecord["inveCost"] = lineRecord["inveCost"]
                wttzzhjLineRecord["wAvgOccupy"] = lineRecord["wAvgOccupy"]
                wttzzhjLineRecord["profit"] = lineRecord["profit"]
            if(key != "hj" and key != "wttzzh" and key != "yjzzs" and key != "hjzy" and key != "hjshzy"):
                hjLineRecord["inveCost"] = hjLineRecord["inveCost"] + lineRecord["inveCost"]
                hjLineRecord["wAvgOccupy"] = hjLineRecord["wAvgOccupy"] + lineRecord["wAvgOccupy"]

        lineRecordMap["hj"] = hjLineRecord
        lineRecordMap["wttzzh"] = wttzzhjLineRecord
        lineRecordMap["hjzy"]["inveCost"] = hjLineRecord["inveCost"] + wttzzhjLineRecord["inveCost"]
        lineRecordMap["hjzy"]["wAvgOccupy"] = hjLineRecord["wAvgOccupy"] + wttzzhjLineRecord["wAvgOccupy"]
        lineRecordMap["hjzy"]["profit"] = hjLineRecord["profit"] + wttzzhjLineRecord["profit"]
        lineRecordMap["hjshzy"]["inveCost"] = lineRecordMap["hjzy"]["inveCost"]
        lineRecordMap["hjshzy"]["wAvgOccupy"] = lineRecordMap["hjzy"]["wAvgOccupy"]
        lineRecordMap["hjshzy"]["profit"] = lineRecordMap["hjzy"]["profit"]

        for key in lineRecordMap.keys():
            lineRecord = lineRecordMap[key]
            if(lineRecord["wAvgOccupy"] != 0):
                lineRecord["yield"] = lineRecord["profit"]/lineRecord["wAvgOccupy"]*100
            if(lineRecordMap["hjzy"]["inveCost"] != 0):
                lineRecord["proportion"] = lineRecord["inveCost"] / lineRecordMap["hjzy"]["inveCost"] *100
            lineRecordMap[key] = lineRecord
            print(lineRecord)

        returnData = {}
        returnDataList = []
        for key in lineRecordMap.keys():
            returnDataList.append(lineRecordMap[key])

        returnData['list'] = returnDataList
        returnData['total'] = returnDataList.__len__()
        return returnData

    """
        转换名称
    """


    def __init_lineRecordMap(self, lineRecordMap):
        lineRecordMap['gdsyl'] = {'name': "1 固定收益类"}
        # 保证金存款
        lineRecordMap['1.1bzjck'] = {'name': "    1.1 保证金存款"}
        bzjck = {'name': "保证金存款"}
        lineRecordMap['bzjck'] = bzjck
        # 协议/定期存款
        lineRecordMap['1.2dqck'] = {'name': "    1.2 协议/定期存款"}
        dqck = {'name': "协议/定期存款"}
        lineRecordMap['dqck'] = dqck
        # 通知存款
        lineRecordMap['1.3tzck'] = {'name': "    1.3 通知存款"}
        tzck = {'name': "通知存款"}
        lineRecordMap['tzck'] = tzck
        # 保险资管产品
        lineRecordMap['1.4bxzgcp'] = {'name': "    1.4 保险资管产品"}
        bxzgcp = {'name': "保险资管产品"}
        lineRecordMap['bxzgcp'] = bxzgcp
        # 债券
        lineRecordMap['1.5zq'] = {'name': "   1.5 债券（委托）"}
        zq = {'name': "债券"}
        lineRecordMap['zq'] = zq
        #2. 现金及流动性管理工具
        lineRecordMap['2.0zq'] = {'name': "2 现金及流动性管理工具"}
        # 现金（自有及委托）
        lineRecordMap['2.1xj'] = {'name': "   2. 1 现金"}
        xj = {'name': "现金（自有及委托）"}
        lineRecordMap['xj'] = xj
        # 货币基金
        lineRecordMap['2.2hbjj'] = {'name': "   2. 2 货币市场基金"}
        hbjj = {'name': "货币基金（自有）"}
        lineRecordMap['hbjj'] = hbjj
        # 货币市场类资管产品
        lineRecordMap['2.3hbsczgcp'] = {'name': "   2. 3 货币市场类资管产品"}
        hbsczgcp = {'name': "货币市场类资管产品"}
        lineRecordMap['hbsczgcp'] = hbsczgcp
        # 交易所逆回购
        lineRecordMap['2.4hg'] = {'name': "   2. 4回购"}
        jysnhg = {'name': "交易所逆回购"}
        lineRecordMap['jysnhg'] = jysnhg
        # 正回购（委托）
        zhg = {'name': "正回购（委托）"}
        lineRecordMap['zhg'] = zhg
        #权益类
        lineRecordMap['3.0qyl'] = {'name': "3 权益类"}
        # 权益类 基金
        qyljj = {'name': "基金"}
        lineRecordMap['qyljj'] = qyljj
        # 权益类 资管产品
        qylzgcp = {'name': "资管产品"}
        lineRecordMap['qylzgcp'] = qylzgcp
        # 权益类 股票与基金（委托）
        gpjj = {'name': "股票与基金（委托）"}
        lineRecordMap['gpjj'] = gpjj
        # 其它金融产品
        lineRecordMap['4.0qtjrcp'] = {'name': "4 其它金融产品"}
        qtjrcp = {'name': "其它金融产品"}
        lineRecordMap['qtjrcp'] = qtjrcp
        # 不动产类资产
        lineRecordMap['5.0bdc'] = {'name': "5 不动产类资产"}
        bdc = {'name': "不动产类资产"}
        lineRecordMap['bdc'] = bdc
        lineRecordMap['hj'] = {'name': "合计"}
        lineRecordMap['wttzzh'] = {'name': "委托投资组合融资"}
        lineRecordMap['yjzzs'] = {'name': "预计增值税"}
        lineRecordMap['hjzy'] = {'name': "合计（自有）"}
        lineRecordMap['hjshzy'] = {'name': "合计（税后自有）"}
        self.__init_lineRecordColumns(lineRecordMap)

    def __init_lineRecordColumns(self, lineRecordMap):
        columns = ['inveCost', 'wAvgOccupy', 'proportion', 'yield', 'profit']
        for key in lineRecordMap.keys():
            for column in columns:
                lineRecordMap.get(key)[column] = 0

    def __calculation_by_dbData(self, dbData, lineRecordMap):
        for item in dbData:
            typeStr = ''
            secuCategoryCode = item['secucategorycode']
            bizTypeCode = item["biztypecode"]
            if secuCategoryCode == None:
                secuCategoryCode = ''
            else:
                if(secuCategoryCode == "BZJCK"):  # 保证金存款
                    typeStr = 'bzjck'
                elif (secuCategoryCode == "DDT"):  # 协议/定期存款
                    typeStr = 'dqck'
                elif (secuCategoryCode == "DDN"):  # 通知存款
                    typeStr = 'tzck'
                elif (secuCategoryCode == "BXZGCP"):  # 保险资管产品
                    typeStr = 'bxzgcp'
                elif (secuCategoryCode.startswith("DB")):  # 债券（委托）
                    typeStr = 'zq'
                elif (secuCategoryCode == "DDC"):  # 现金
                    typeStr = 'xj'
                elif (secuCategoryCode == "EUM"):  # 货币市场基金
                    typeStr = 'hbjj'
                elif (secuCategoryCode == "BXZGCP"):  # 货币市场类资管产品
                    typeStr = 'hbsczgcp'
                elif (secuCategoryCode == "DP"):  # 回购
                    if(bizTypeCode == "funds_repurchase_nhg"): # 交易所逆回购
                        typeStr = 'jysnhg'
                    elif(bizTypeCode == "funds_repurchase_zhg"): # 正回购（委托）
                        typeStr = 'zhg'
                elif (secuCategoryCode.startswith("EU")):
                    if (secuCategoryCode != "EUM"):  # 权益类 基金
                        typeStr = 'qyljj'
                elif (secuCategoryCode == "ZGCP"):  # 权益类 资管产品
                    typeStr = 'qylzgcp'
                elif (secuCategoryCode == "GPYJJWT"):  # 权益类 股票与基金（委托）
                    typeStr = 'gpjj'
                elif (secuCategoryCode == "EWE"):  # 其它金融产品
                    typeStr = 'qtjrcp'
                elif (secuCategoryCode == "BDC"):  # 不动产
                    typeStr = 'bdc'
            if typeStr != '':
               self.__use_data(typeStr, item, lineRecordMap)

    def __use_data(self, typeStr, data, lineRecordMap):
        lineRecord = lineRecordMap[typeStr]
        lineRecord['inveCost'] = lineRecord['inveCost'] + data['invecost']
        lineRecord['profit'] = lineRecord['profit'] + data['inverealprofit']
        positionQty = data['positionqty']
        settleDate = data['settledate']
        positionCreateDate = data['positioncreatedate']
        positionClearDate = data['positioncleardate']
        lastYearEed = self.__quarter_end(settleDate)
        if(positionQty>0):
            if(positionCreateDate<=lastYearEed):
                inveCost = data['invecost'] * self._cal_day_between(lastYearEed, settleDate)/365
            else:
                inveCost = data['invecost'] * self._cal_day_between(positionCreateDate, settleDate)/365
        elif(positionQty==0):
            if(positionClearDate>lastYearEed):
                costPositionData = self.sql.get_cost_position_data(data["secuglobalcode"], positionClearDate)
                inveCost = costPositionData['invecost'] * self._cal_day_between(lastYearEed, positionClearDate)/365
                print(data['invecost'])
        lineRecord['wAvgOccupy'] = lineRecord['wAvgOccupy'] + inveCost


    """
        根据传入的时间获取上年年末日期
    """

    def __quarter_end(self, currentDate):
        YYYYmmdd = '%Y-%m-%d'
        day = dt.datetime.strptime(currentDate, "%Y-%m-%d")
        # 本年第一天
        this_year_start = dt.datetime(day.year, 1, 1)
        # 上年最后一天
        last_year_end_time = this_year_start - timedelta(days=1) + dt.timedelta(hours=23, minutes=59, seconds=59)
        last_year_end = last_year_end_time.strftime(YYYYmmdd)
        # 存放顺序：当前季度末，上个季度末，去年年末
        return last_year_end

    """
         计算两日期之间的天数
     """

    def _cal_day_between(self, startDate, endDate):
        start_date = dt.datetime.strptime(startDate, "%Y-%m-%d")
        end_date = dt.datetime.strptime(endDate, "%Y-%m-%d")
        return (end_date - start_date).days


