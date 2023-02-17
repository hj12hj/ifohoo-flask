from variables.db_connection import db
import datetime

"""
    短期报表列sql
"""


class IncomeCalculationReportSql:
    def __init__(self):
        self.db = db
        self.day = 365
        # 存款查询
        self.ck_sql = """select
                              settle_date,
                              position_create_date,
                              position_clear_date,
                              inve_cost,
                              ref_match_net_price/100 as ll,
                              ref_settle_date as dqrq
                                from cost_position_funds
                                    where settle_date = :1 and position_qty > 0 and secu_category_code in ('DDA','DDN','DDT') and organ_code = :2 """
        # 存单查询
        self.cd_sql = """select 
                           s.coupon_rate as ll,
                           s.interest_end_date as dqrq,
                           c.position_create_date,
                           c.position_clear_date,
                           c.inve_cost
                               from cost_position_security_invest c
                                    inner join secu_extend_bond s
                                        on c.biz_type_code = 'deposit_invest' and c.settle_date = :1 and c.secu_global_code = s.secu_global_code and c.organ_code = :2 """
        # 逆回购查询
        self.nhg_sql = """select 
                            settle_date,
                            position_create_date,
                            position_clear_date,
                            inve_cost,
                            ref_match_net_price/100 as ll,
                            ref_settle_date as dqrq
                                from cost_position_funds
                                    where settle_date = :1 and position_qty > 0 and biz_type_code = 'funds_repurchase' and organ_code = :2 """
        # 活期查询
        self.hq_sql = """select 
                            settle_date,
                            position_create_date,
                            position_clear_date,
                            inve_cost,
                            ref_match_net_price/100 as ll,
                            ref_settle_date as dqrq 
                            from cost_position_funds
                                where settle_date = :1 and position_qty > 0 and secu_category_code = 'DDC' and organ_code = :2 """
        # 股票和基金行情价
        self.hqj_sql = """select
                            occur_date,
                            secu_global_code,
                            latest_price
                                from secu_quota
                                    where secu_global_code in (
                                        select secu_global_code from cost_position_security_invest
                                            where (secu_category_code like 'ES%' or secu_category_code like 'EU%') and settle_date = :1 and position_qty > 0)
                                        and occur_date in (:2,:3) order by secu_global_code, occur_date asc"""
        # 货币基金查询
        self.hbjj_sql = """select 
                                position_create_date,
                                position_clear_date,
                                position_qty,
                                inve_cost
                                    from cost_position_security_invest
                                        where secu_category_code like 'EUM%' and settle_date = :1 and position_qty > 0 and organ_code = :2 """
        # 金融债 DBF
        self.jrz_sql = """select 
                                s.coupon_rate as ll,
                                s.interest_end_date as dqrq,
                                c.position_create_date,
                                c.position_clear_date,
                                c.inve_cost 
                                    from cost_position_security_invest c 
                                        inner join secu_extend_bond s 
                                            on c.secu_category_code like 'DBF%' and c.settle_date = :1 and c.secu_global_code = s.secu_global_code and c.organ_code = :2 """
        # 信用债 DBC公司债 DBE企业债
        self.xyz_sql = """select 
                                s.coupon_rate as ll,
                                s.interest_end_date as dqrq,
                                c.position_create_date,
                                c.position_clear_date,
                                c.inve_cost 
                                    from cost_position_security_invest c 
                                        inner join secu_extend_bond s 
                                            on (c.secu_category_code like 'DBC%' or c.secu_category_code like 'DBE%') and c.settle_date = :1 and c.secu_global_code = s.secu_global_code and organ_code = :2 """
        # 混合基金
        self.hhjj_sql = """select
                                secu_global_code,  
                                position_create_date,
                                position_clear_date,
                                position_qty,
                                inve_cost
                                    from cost_position_security_invest 
                                        where secu_category_code like 'EU%' and secu_category_code not like 'EUM%' and settle_date = :1 and position_qty > 0 and organ_code = :2 """
        # 股票
        self.gp_sql = """select 
                                secu_global_code, 
                                position_create_date,
                                position_clear_date,
                                position_qty,
                                inve_cost
                                    from cost_position_security_invest 
                                        where secu_category_code like 'ES%' and settle_date = :1 and position_qty > 0 and organ_code = :2 """

    """
    短期债券报表列表查询
    """

    def get_income_calculation_report_list(self, query_data):
        #
        organCode = query_data.get("organCode")
        startDate = query_data.get("startDate")
        endDate = query_data.get("endDate")

        # 获取查询结束日期的存款数据
        ck_end_data = self.db.query_all(self.ck_sql, (endDate, organCode,))
        ck_end_dict = self.cal_jrsc_data(ck_end_data, startDate, endDate)
        # 获取查询结束日期的存单数据
        cd_end_data = self.db.query_all(self.cd_sql, (endDate, organCode,))
        cd_end_dict = self.cal_jrsc_data(cd_end_data, startDate, endDate)
        # 获取查询结束日期的逆回购数据
        nhg_end_data = self.db.query_all(self.nhg_sql, (endDate, organCode,))
        nhg_end_dict = self.cal_jrsc_data(nhg_end_data, startDate, endDate)
        # 获取查询结束日期的活期数据
        hq_end_data = self.db.query_all(self.hq_sql, (endDate, organCode,))
        hq_end_dict = self.cal_jrsc_data(hq_end_data, startDate, endDate)
        # 获取查询日期的行情数据
        hqj_end_data = self.db.query_all(self.hqj_sql, [endDate, startDate, endDate, ])
        # 获取查询结束日期的货币基金数据
        hbjj_end_data = self.db.query_all(self.hbjj_sql, (endDate, organCode,))
        hbjj_end_dict = self.cal_zqtz_data(hbjj_end_data, hqj_end_data, startDate, endDate)
        # 获取查询结束日期的金融债数据
        jrz_end_data = self.db.query_all(self.jrz_sql, (endDate, organCode,))
        jrz_end_dict = self.cal_zq_data(jrz_end_data, startDate, endDate)
        # 获取查询结束日期的信用债数据
        xyz_end_data = self.db.query_all(self.xyz_sql, (endDate, organCode,))
        xyz_end_dict = self.cal_zq_data(xyz_end_data, startDate, endDate)
        # 获取查询结束日期的混合基金数据
        hhjj_end_data = self.db.query_all(self.hhjj_sql, (endDate, organCode,))
        hhjj_end_dict = self.cal_zqtz_data(hhjj_end_data, hqj_end_data, startDate, endDate)
        # 获取查询结束日期的股票数据
        gp_end_data = self.db.query_all(self.gp_sql, (endDate, organCode,))
        gp_end_dict = self.cal_zqtz_data(gp_end_data, hqj_end_data, startDate, endDate)
        data = self.convert_final_data(ck_end_dict, cd_end_dict, nhg_end_dict, hq_end_dict, hbjj_end_dict, jrz_end_dict,
                                       xyz_end_dict, hhjj_end_dict, gp_end_dict)
        # 处理精度
        for d in data:
            if "weightedOccupancyAmt" in d:
                d["weightedOccupancyAmt"] = round(d.get("weightedOccupancyAmt"), 2) if d.get(
                    "weightedOccupancyAmt") else 0
            if "incomeAmt" in d:
                d["incomeAmt"] = round(d.get("incomeAmt"), 2) if d.get("incomeAmt") else 0
            if "interestRate" in d:
                d["interestRate"] = round(d.get("interestRate"), 2) if d.get("interestRate") else 0
            if "scaleRatio" in d:
                d["scaleRatio"] = round(d.get("scaleRatio"), 2) if d.get("scaleRatio") else 0
        return {"total": len(data), "list": data}

    def convert_final_data(self, ck_end_dict, cd_end_dict, nhg_end_dict, hq_end_dict, hbjj_end_dict, jrz_end_dict,
                           xyz_end_dict, hhjj_end_dict, gp_end_dict):
        data = []
        ck_cl_one_year = {}
        ck_cl_six_month = {}
        ck_cl_three_month = {}
        ck_cl_three_month_bellow = {}
        ck_zl_one_year = {}
        ck_zl_six_month = {}
        ck_zl_three_month = {}
        ck_zl_three_month_bellow = {}
        if ck_end_dict and ck_end_dict.get("cl"):
            if "cl_one_year" in ck_end_dict.get("cl"):
                ck_cl_one_year = ck_end_dict.get("cl").get("cl_one_year")
            if "cl_six_month" in ck_end_dict.get("cl"):
                ck_cl_six_month = ck_end_dict.get("cl").get("cl_six_month")
            if "ck_cl_three_month" in ck_end_dict.get("cl"):
                ck_cl_three_month = ck_end_dict.get("cl").get("cl_three_month")
            if "cl_three_month_bellow" in ck_end_dict.get("cl"):
                ck_cl_three_month_bellow = ck_end_dict.get("cl").get("cl_three_month_bellow")
        if ck_end_dict and ck_end_dict.get("zl"):
            if "zl_one_year" in ck_end_dict.get("zl"):
                ck_zl_one_year = ck_end_dict.get("zl").get("zl_one_year")
            if "zl_six_month" in ck_end_dict.get("zl"):
                ck_zl_six_month = ck_end_dict.get("zl").get("zl_six_month")
            if "zk_cl_three_month" in ck_end_dict.get("zl"):
                ck_zl_three_month = ck_end_dict.get("zl").get("zl_three_month")
            if "zl_three_month_bellow" in ck_end_dict.get("zl"):
                ck_zl_three_month_bellow = ck_end_dict.get("zl").get("zl_three_month_bellow")

        cd_cl_one_year = {}
        cd_cl_six_month = {}
        cd_cl_three_month = {}
        cd_cl_three_month_bellow = {}
        cd_zl_one_year = {}
        cd_zl_six_month = {}
        cd_zl_three_month = {}
        cd_zl_three_month_bellow = {}
        if cd_end_dict and cd_end_dict.get("cl"):
            if "cl_one_year" in cd_end_dict.get("cl"):
                cd_cl_one_year = cd_end_dict.get("cl").get("cl_one_year")
            if "cl_six_month" in cd_end_dict.get("cl"):
                cd_cl_six_month = cd_end_dict.get("cl").get("cl_six_month")
            if "ck_cl_three_month" in cd_end_dict.get("cl"):
                cd_cl_three_month = cd_end_dict.get("cl").get("cl_three_month")
            if "cl_three_month_bellow" in cd_end_dict.get("cl"):
                cd_cl_three_month_bellow = cd_end_dict.get("cl").get("cl_three_month_bellow")
        if cd_end_dict and cd_end_dict.get("zl"):
            if "zl_one_year" in cd_end_dict.get("zl"):
                cd_zl_one_year = cd_end_dict.get("zl").get("zl_one_year")
            if "zl_six_month" in cd_end_dict.get("zl"):
                cd_zl_six_month = cd_end_dict.get("zl").get("zl_six_month")
            if "zk_cl_three_month" in cd_end_dict.get("zl"):
                cd_zl_three_month = cd_end_dict.get("zl").get("zl_three_month")
            if "zl_three_month_bellow" in cd_end_dict.get("zl"):
                cd_zl_three_month_bellow = cd_end_dict.get("zl").get("zl_three_month_bellow")

        nhg_cl_one_year = {}
        nhg_cl_six_month = {}
        nhg_cl_three_month = {}
        nhg_cl_three_month_bellow = {}
        nhg_zl_one_year = {}
        nhg_zl_six_month = {}
        nhg_zl_three_month = {}
        nhg_zl_three_month_bellow = {}
        if nhg_end_dict and nhg_end_dict.get("cl"):
            if "cl_one_year" in nhg_end_dict.get("cl"):
                nhg_cl_one_year = nhg_end_dict.get("cl").get("cl_one_year")
            if "cl_six_month" in nhg_end_dict.get("cl"):
                nhg_cl_six_month = nhg_end_dict.get("cl").get("cl_six_month")
            if "ck_cl_three_month" in nhg_end_dict.get("cl"):
                nhg_cl_three_month = nhg_end_dict.get("cl").get("cl_three_month")
            if "cl_three_month_bellow" in nhg_end_dict.get("cl"):
                nhg_cl_three_month_bellow = nhg_end_dict.get("cl").get("cl_three_month_bellow")
        if nhg_end_dict and nhg_end_dict.get("zl"):
            if "zl_one_year" in nhg_end_dict.get("zl"):
                nhg_zl_one_year = nhg_end_dict.get("zl").get("zl_one_year")
            if "zl_six_month" in nhg_end_dict.get("zl"):
                nhg_zl_six_month = nhg_end_dict.get("zl").get("zl_six_month")
            if "zk_cl_three_month" in nhg_end_dict.get("zl"):
                nhg_zl_three_month = nhg_end_dict.get("zl").get("zl_three_month")
            if "zl_three_month_bellow" in nhg_end_dict.get("zl"):
                nhg_zl_three_month_bellow = nhg_end_dict.get("zl").get("zl_three_month_bellow")

        hq_cl_one_year = {}
        hq_cl_six_month = {}
        hq_cl_three_month = {}
        hq_cl_three_month_bellow = {}
        hq_zl_one_year = {}
        hq_zl_six_month = {}
        hq_zl_three_month = {}
        hq_zl_three_month_bellow = {}
        if hq_end_dict and hq_end_dict.get("cl"):
            if "cl_one_year" in hq_end_dict.get("cl"):
                hq_cl_one_year = hq_end_dict.get("cl").get("cl_one_year")
            if "cl_six_month" in hq_end_dict.get("cl"):
                hq_cl_six_month = hq_end_dict.get("cl").get("cl_six_month")
            if "ck_cl_three_month" in hq_end_dict.get("cl"):
                hq_cl_three_month = hq_end_dict.get("cl").get("cl_three_month")
            if "cl_three_month_bellow" in hq_end_dict.get("cl"):
                hq_cl_three_month_bellow = hq_end_dict.get("cl").get("cl_three_month_bellow")
        if hq_end_dict and hq_end_dict.get("zl"):
            if "zl_one_year" in hq_end_dict.get("zl"):
                hq_zl_one_year = hq_end_dict.get("zl").get("zl_one_year")
            if "zl_six_month" in hq_end_dict.get("zl"):
                hq_zl_six_month = hq_end_dict.get("zl").get("zl_six_month")
            if "zk_cl_three_month" in hq_end_dict.get("zl"):
                hq_zl_three_month = hq_end_dict.get("zl").get("zl_three_month")
            if "zl_three_month_bellow" in hq_end_dict.get("zl"):
                hq_zl_three_month_bellow = hq_end_dict.get("zl").get("zl_three_month_bellow")

        hbjj_cl_data = {}
        hbjj_zl_data = {}
        if hbjj_end_dict and hbjj_end_dict.get("cl"):
            hbjj_cl_data = hbjj_end_dict.get("cl")[0]
        if hbjj_end_dict and hbjj_end_dict.get("zl"):
            hbjj_zl_data = hbjj_end_dict.get("zl")[0]

        jrz_cl_data = {}
        jrz_zl_data = {}
        if jrz_end_dict and jrz_end_dict.get("cl"):
            jrz_cl_data = jrz_end_dict.get("cl")[0]
        if jrz_end_dict and jrz_end_dict.get("zl"):
            jrz_zl_data = jrz_end_dict.get("zl")[0]

        xyz_cl_data = {}
        xyz_zl_data = {}
        if xyz_end_dict and xyz_end_dict.get("cl"):
            xyz_cl_data = xyz_end_dict.get("cl")[0]
        if xyz_end_dict and xyz_end_dict.get("zl"):
            xyz_zl_data = xyz_end_dict.get("zl")[0]

        hhjj_cl_data = {}
        hhjj_zl_data = {}
        if hhjj_end_dict and hhjj_end_dict.get("cl"):
            hhjj_cl_data = hhjj_end_dict.get("cl")[0]
        if hhjj_end_dict and hhjj_end_dict.get("zl"):
            hhjj_zl_data = hhjj_end_dict.get("zl")[0]

        gp_cl_data = {}
        gp_zl_data = {}
        if gp_end_dict and gp_end_dict.get("cl"):
            gp_cl_data = gp_end_dict.get("cl")[0]
        if gp_end_dict and gp_end_dict.get("zl"):
            gp_zl_data = gp_end_dict.get("zl")[0]
        cl_one_year = self.cal_total([ck_cl_one_year, cd_cl_one_year, nhg_cl_one_year, hq_cl_one_year])
        cl_one_year["productName"] = "1年期"

        cl_six_month = self.cal_total([ck_cl_six_month, cd_cl_six_month, nhg_cl_six_month, hq_cl_six_month])
        cl_six_month["productName"] = "6个月-1年期"

        cl_three_month = self.cal_total([ck_cl_three_month, cd_cl_three_month, nhg_cl_three_month,
                                         hq_cl_three_month])
        cl_three_month["productName"] = "3个月-6个月"

        cl_three_month_bellow = self.cal_total([ck_cl_three_month_bellow, cd_cl_three_month_bellow,
                                                nhg_cl_three_month_bellow, hq_cl_three_month_bellow])
        cl_three_month_bellow["productName"] = "3个月以下"

        ck_cl_three_month_bellow["productName"] = "存款"
        cd_cl_three_month_bellow["productName"] = "存单"
        nhg_cl_three_month_bellow["productName"] = "逆回购"
        hq_cl_three_month_bellow["productName"] = "活期"

        cl_jrschj = self.cal_total([cl_one_year, cl_six_month, cl_three_month, cl_three_month_bellow])
        cl_jrschj["productName"] = "金融市场合计"

        hbjj_cl_data["productName"] = "货币基金"
        jrz_cl_data["productName"] = "金融债"
        xyz_cl_data["productName"] = "信用债"
        hhjj_cl_data["productName"] = "混合基金"
        gp_cl_data["productName"] = "股票"

        cl_zqtz = self.cal_total([hbjj_cl_data, jrz_cl_data, xyz_cl_data, hhjj_cl_data, gp_cl_data])
        cl_zqtz["productName"] = "证券投资合计"
        cl_tl = {"productName": "套利"}

        cl_hj = self.cal_total([cl_jrschj, cl_zqtz, cl_tl])
        cl_hj["productName"] = "存量合计"

        zl_one_year = self.cal_total([ck_zl_one_year, cd_zl_one_year, nhg_zl_one_year, hq_zl_one_year])
        zl_one_year["productName"] = "1年期"

        zl_six_month = self.cal_total([ck_zl_six_month, cd_zl_six_month, nhg_zl_six_month, hq_zl_six_month])
        zl_six_month["productName"] = "6个月-1年期"

        zl_three_month = self.cal_total([ck_zl_three_month, cd_zl_three_month, nhg_zl_three_month,
                                         hq_zl_three_month])
        zl_three_month["productName"] = "3个月-6个月"

        zl_three_month_bellow = self.cal_total([ck_zl_three_month_bellow, cd_zl_three_month_bellow,
                                                nhg_zl_three_month_bellow, hq_zl_three_month_bellow])
        zl_three_month_bellow["productName"] = "3个月以下"

        ck_zl_three_month_bellow["productName"] = "存款"
        cd_zl_three_month_bellow["productName"] = "存单"
        nhg_zl_three_month_bellow["productName"] = "逆回购"
        hq_zl_three_month_bellow["productName"] = "活期"

        zl_jrschj = self.cal_total([zl_one_year, zl_six_month, zl_three_month, zl_three_month_bellow])
        zl_jrschj["productName"] = "金融市场合计"

        hbjj_zl_data["productName"] = "货币基金"
        jrz_zl_data["productName"] = "金融债"
        xyz_zl_data["productName"] = "信用债"
        hhjj_zl_data["productName"] = "混合基金"
        gp_zl_data["productName"] = "股票"

        zl_zqtz = self.cal_total([hbjj_zl_data, jrz_zl_data, xyz_zl_data, hhjj_zl_data, gp_zl_data])
        zl_zqtz["productName"] = "证券投资合计"

        zl_tl = {"productName": "套利"}

        zl_hj = self.cal_total([zl_jrschj, zl_zqtz, zl_tl])
        zl_hj["productName"] = "增量合计"

        zhj = self.cal_total([cl_hj, zl_hj])
        zhj["productName"] = "总合计"

        total_ck = self.cal_total(
            [ck_cl_one_year, ck_cl_six_month, ck_cl_three_month, ck_cl_three_month_bellow, ck_zl_one_year,
             ck_zl_six_month, ck_zl_three_month, ck_zl_three_month_bellow])
        total_ck["productName"] = "存款"

        total_cd = self.cal_total(
            [cd_cl_one_year, cd_cl_six_month, cd_cl_three_month, cd_cl_three_month_bellow, cd_zl_one_year,
             cd_zl_six_month, cd_zl_three_month, cd_zl_three_month_bellow])
        total_cd["productName"] = "存单"

        total_ck_cd = self.cal_total([total_ck, total_cd])
        total_ck_cd["productName"] = "存款、存单"

        total_nhg = self.cal_total(
            [nhg_cl_one_year, nhg_cl_six_month, nhg_cl_three_month, nhg_cl_three_month_bellow, nhg_zl_one_year,
             nhg_zl_six_month, nhg_zl_three_month, nhg_zl_three_month_bellow])
        total_nhg["productName"] = "逆回购"

        total_hq = self.cal_total(
            [hq_cl_one_year, hq_cl_six_month, hq_cl_three_month, hq_cl_three_month_bellow, hq_zl_one_year,
             hq_zl_six_month, hq_zl_three_month, hq_zl_three_month_bellow])
        total_hq["productName"] = "活期"

        total_nhg_hq = self.cal_total([total_nhg, total_hq])
        total_nhg_hq["productName"] = "逆回购、活期"

        total_jrsc = self.cal_total([total_ck_cd, total_nhg_hq])
        total_jrsc["productName"] = "金融市场合计"

        total_hbjj = self.cal_total([hbjj_cl_data, hbjj_zl_data])
        total_hbjj["productName"] = "货币基金"

        total_jrz = self.cal_total([jrz_cl_data, jrz_zl_data])
        total_jrz["productName"] = "金融债"

        total_xyz = self.cal_total([xyz_cl_data, xyz_zl_data])
        total_xyz["productName"] = "信用债"

        total_hhjj = self.cal_total([hhjj_cl_data, hhjj_zl_data])
        total_hhjj["productName"] = "混合基金"

        total_gp = self.cal_total([gp_cl_data, gp_zl_data])
        total_gp["productName"] = "股票"

        total_zqtz = self.cal_total([total_hbjj, total_jrz, total_xyz, total_hhjj, total_gp])
        total_zqtz["productName"] = "证券投资"

        total_tl = self.cal_total([cl_tl, zl_tl])
        total_tl["productName"] = "套利"

        total_zhj = self.cal_total([total_jrsc, total_zqtz, total_tl])
        total_zhj["productName"] = "合计"

        # 总计加权占用，用于计算规模占比
        total_jqzy = total_zhj.get("weightedOccupancyAmt")
        total_ck["scaleRatio"] = self.cal_scale_ratio(total_ck, total_jqzy)
        total_cd["scaleRatio"] = self.cal_scale_ratio(total_cd, total_jqzy)
        total_ck_cd["scaleRatio"] = self.cal_scale_ratio(total_ck_cd, total_jqzy)
        total_nhg["scaleRatio"] = self.cal_scale_ratio(total_nhg, total_jqzy)
        total_hq["scaleRatio"] = self.cal_scale_ratio(total_hq, total_jqzy)
        total_jrsc["scaleRatio"] = self.cal_scale_ratio(total_jrsc, total_jqzy)
        total_hbjj["scaleRatio"] = self.cal_scale_ratio(total_hbjj, total_jqzy)
        total_jrz["scaleRatio"] = self.cal_scale_ratio(total_jrz, total_jqzy)
        total_xyz["scaleRatio"] = self.cal_scale_ratio(total_xyz, total_jqzy)
        total_hhjj["scaleRatio"] = self.cal_scale_ratio(total_hhjj, total_jqzy)
        total_gp["scaleRatio"] = self.cal_scale_ratio(total_gp, total_jqzy)
        total_zqtz["scaleRatio"] = self.cal_scale_ratio(total_zqtz, total_jqzy)
        total_tl["scaleRatio"] = self.cal_scale_ratio(total_tl, total_jqzy)
        total_zhj["scaleRatio"] = self.cal_scale_ratio(total_zhj, total_jqzy)

        data.append(total_ck)
        data.append(total_cd)
        data.append(total_ck_cd)
        data.append(total_nhg)
        data.append(total_hq)
        data.append(total_nhg_hq)
        data.append(total_jrsc)
        data.append(total_hbjj)
        data.append(total_jrz)
        data.append(total_xyz)
        data.append(total_hhjj)
        data.append(total_gp)
        data.append(total_zqtz)
        data.append(total_tl)
        data.append(total_zhj)
        # 分隔
        cl_fg_data = {"productName": "存量"}
        data.append(cl_fg_data)
        data.append(cl_one_year)
        data.append(cl_six_month)
        data.append(cl_three_month)
        data.append(cl_three_month_bellow)
        data.append(ck_cl_three_month_bellow)
        data.append(cd_cl_three_month_bellow)
        data.append(nhg_cl_three_month_bellow)
        data.append(hq_cl_three_month_bellow)
        data.append(cl_jrschj)
        data.append(hbjj_cl_data)
        data.append(jrz_cl_data)
        data.append(xyz_cl_data)
        data.append(hhjj_cl_data)
        data.append(gp_cl_data)
        data.append(cl_zqtz)
        data.append(cl_hj)
        data.append(cl_tl)
        # 分隔
        zl_fg_data = {"productName": "增量"}
        data.append(zl_fg_data)
        data.append(zl_one_year)
        data.append(zl_six_month)
        data.append(zl_three_month)
        data.append(zl_three_month_bellow)
        data.append(zl_jrschj)
        data.append(ck_zl_three_month_bellow)
        data.append(cd_zl_three_month_bellow)
        data.append(nhg_zl_three_month_bellow)
        data.append(hq_zl_three_month_bellow)
        data.append(hbjj_zl_data)
        data.append(jrz_zl_data)
        data.append(xyz_zl_data)
        data.append(hhjj_zl_data)
        data.append(gp_zl_data)
        data.append(zl_zqtz)
        data.append(zl_hj)
        data.append(zl_tl)
        data.append(zhj)

        return data

    def cal_scale_ratio(self, data, jqzy):
        result = 0
        if jqzy:
            if "weightedOccupancyAmt" in data:
                if data.get("weightedOccupancyAmt") == 0:
                    result = 0
                else:
                    result = data.get("weightedOccupancyAmt") / jqzy * 100
        return result

    def cal_total(self, list_data):
        result_data = {"weightedOccupancyAmt": 0, "incomeAmt": 0, "interestRate": 0}
        if len(list_data) > 0:
            for data in list_data:
                weightedOccupancyAmt = 0
                incomeAmt = 0
                if "weightedOccupancyAmt" in data:
                    weightedOccupancyAmt = data.get("weightedOccupancyAmt") if data.get("weightedOccupancyAmt") else 0
                if "incomeAmt" in data:
                    incomeAmt = data.get("incomeAmt") if data.get("incomeAmt") else 0
                result_data["weightedOccupancyAmt"] = (result_data.get("weightedOccupancyAmt") if result_data.get("weightedOccupancyAmt") else 0) + weightedOccupancyAmt
                result_data["incomeAmt"] = (result_data.get("incomeAmt") if result_data.get("incomeAmt") else 0) + incomeAmt
            if result_data.get("weightedOccupancyAmt"):
                if result_data.get("weightedOccupancyAmt") == 0:
                    result_data["interestRate"] = 0
                else:
                    result_data["interestRate"] = result_data.get("incomeAmt") / result_data.get("weightedOccupancyAmt") * 100
        return result_data

    """ 计算证券投资数据 """

    def cal_zqtz_data(self, end_data, hqj_end_data, startDate, endDate):
        # 存量结果集
        cl_data = []
        # 增量结果集
        zl_data = []
        quot_dict = {}
        if len(hqj_end_data) > 0:
            for hq_data in hqj_end_data:
                hq_rq = hq_data.get("occurDate")
                hq_jg = hq_data.get("latestPrice")
                zqdm = hq_data.get("secuGlobalCode")
                quot_dict[hq_rq + "_" + zqdm] = hq_jg

        if len(end_data) > 0:
            zyts = self.cal_day_between(startDate, endDate)
            for data in end_data:
                data["inveCost"] = 0 if data.get("inveCost") == None else data.get("inveCost")
                data["positionQty"] = 0 if data.get("positionQty") == None else data.get("positionQty")
                data["secuGlobalCode"] = "0" if data.get("secuGlobalCode") == None else data.get("secuGlobalCode")
                ccj = 0
                if data.get("positionQty") == 0:
                    ccj = 0
                else:
                    # 持仓成本价，如果行情中未获取到数据，则用持仓成本价
                    ccj = data.get("inveCost") / data.get("positionQty")
                data["ZYTS"] = zyts

                key1 = startDate + "_" + data.get("secuGlobalCode")
                key2 = endDate + "_" + data.get("secuGlobalCode")
                if key1 in quot_dict:
                    data["KSLL"] = quot_dict.get(key1)
                else:
                    data["KSLL"] = ccj
                if key2 in quot_dict:
                    data["JSLL"] = quot_dict.get(key2)
                else:
                    data["JSLL"] = ccj
                # 加权占用 = 金额/365*占用天数
                jqzy = data.get("inveCost") / self.day * zyts
                data["weightedOccupancyAmt"] = jqzy
                # 收益额 = 持仓数量 * (期末行情价-期初行情价)
                sye = data.get("positionQty") * (data.get("JSLL") - data.get("KSLL"))
                data["incomeAmt"] = sye
            cl = {"weightedOccupancyAmt": 0, "incomeAmt": 0}
            zl = {"weightedOccupancyAmt": 0, "incomeAmt": 0}
            for data in end_data:
                # 存入日 用于判断增量还是存量
                crr = data.get("positionCreateDate")
                if crr != None:
                    # 查询结束日期年份
                    endDateYear = endDate[0:4]
                    crr_year = crr[0:4]
                    # 说明是存量
                    if endDateYear > crr_year:
                        cl["weightedOccupancyAmt"] = (cl.get("weightedOccupancyAmt") if cl.get("weightedOccupancyAmt") else 0) + data.get("weightedOccupancyAmt")
                        cl["incomeAmt"] = (cl.get("incomeAmt") if cl.get("incomeAmt")  else 0) + data.get("incomeAmt")
                    # 增量
                    else:
                        zl["weightedOccupancyAmt"] = (zl.get("weightedOccupancyAmt") if zl.get("weightedOccupancyAmt") else 0) + data.get("weightedOccupancyAmt")
                        zl["incomeAmt"] = (zl.get("incomeAmt") if zl.get("incomeAmt")  else 0) + data.get("incomeAmt")
            cl_data.append(cl)
            zl_data.append(zl)
        return {"cl": cl_data, "zl": zl_data}

    """ 计算债券类投资 """

    def cal_zq_data(self, cd_data, startDate, endDate):
        # 存量结果集
        cl_data = []
        # 增量结果集
        zl_data = []
        if len(cd_data) > 0:
            for cd in cd_data:
                # 存入日
                crr = cd.get("positionCreateDate")
                # 到期日
                dqr = cd.get("dqrq")
                cd["weightedOccupancyAmt"] = 0
                cd["incomeAmt"] = 0
                if (crr and len(str(crr)) == 10) and (dqr and len(str(dqr)) == 10):
                    # 存入日和到期日都是有值的,计算期限
                    cd["QX"] = self.cal_day_between(crr, dqr)
                    # 计算占用天数
                    if endDate > dqr:
                        zyts = self.cal_day_between(startDate, endDate)
                    else:
                        zyts = self.cal_day_between(startDate, dqr) - 1
                    cd["ZYTS"] = zyts
                    # 加权占用 = 金额/365*占用天数
                    jqzy = cd.get("inveCost") / self.day * zyts
                    cd["weightedOccupancyAmt"] = jqzy
                    # 收益额 = 加权占用额 * 利率
                    sye = jqzy * cd.get("ll")
                    cd["incomeAmt"] = sye
            # 基础值已算完毕，计算存量增量
            cl_zq_data = {"weightedOccupancyAmt": 0, "incomeAmt": 0}
            zl_zq_data = {"weightedOccupancyAmt": 0, "incomeAmt": 0}
            for cd in cd_data:
                if cd.get("QX"):
                    # 查询结束日期年份
                    endDateYear = endDate[0:4]
                    if cd.get("positionCreateDate") != None:
                        crr_year = cd.get("positionCreateDate")[0:4]
                        # 说明是存量
                        if endDateYear > crr_year:
                            cl_zq_data["weightedOccupancyAmt"] = (cl_zq_data.get("weightedOccupancyAmt") if cl_zq_data.get("weightedOccupancyAmt") else 0) + cd.get("weightedOccupancyAmt")
                            cl_zq_data["incomeAmt"] = (cl_zq_data.get("incomeAmt") if cl_zq_data.get("incomeAmt") else 0) + cd.get("incomeAmt")
                        # 增量
                        else:
                            zl_zq_data["weightedOccupancyAmt"] = (zl_zq_data.get("weightedOccupancyAmt") if zl_zq_data.get("weightedOccupancyAmt") else 0) + cd.get("weightedOccupancyAmt")
                            zl_zq_data["incomeAmt"] = (zl_zq_data.get("incomeAmt") if zl_zq_data.get("incomeAmt") else 0) + cd.get("incomeAmt")
            cl_data.append(cl_zq_data)
            zl_data.append(zl_zq_data)
        return {"cl": cl_data, "zl": zl_data}

    """计算金融市场数据"""

    def cal_jrsc_data(self, cd_data, startDate, endDate):
        # 存量结果集
        cl_data = []
        # 增量结果集
        zl_data = []
        if len(cd_data) > 0:
            for cd in cd_data:
                cd["weightedOccupancyAmt"] = 0
                cd["incomeAmt"] = 0
                # 存入日
                crr = cd.get("positionCreateDate")
                # 到期日
                dqr = cd.get("dqrq")
                if (crr and len(str(crr)) == 10) and (dqr and len(str(dqr)) == 10):
                    # 存入日和到期日都是有值的,计算期限
                    cd["QX"] = self.cal_day_between(crr, dqr)
                    # 计算占用天数
                    if endDate > dqr:
                        zyts = self.cal_day_between(startDate, endDate)
                    else:
                        zyts = self.cal_day_between(startDate, dqr) - 1
                    cd["ZYTS"] = zyts
                    # 加权占用 = 金额/365*占用天数
                    jqzy = cd.get("inveCost") / self.day * zyts
                    cd["weightedOccupancyAmt"] = jqzy
                    # 收益额 = 加权占用额 * 利率
                    sye = jqzy * cd.get("ll")
                    cd["incomeAmt"] = sye
            # 基础值已算完毕，计算存量增量
            cl_one_year = {"productName": "1年期", "weightedOccupancyAmt": 0, "incomeAmt": 0}
            cl_six_month = {"productName": "6个月-1年期", "weightedOccupancyAmt": 0, "incomeAmt": 0}
            cl_three_month = {"productName": "3个月-6个月", "weightedOccupancyAmt": 0, "incomeAmt": 0}
            cl_three_month_bellow = {"productName": "3个月以下", "weightedOccupancyAmt": 0, "incomeAmt": 0}

            zl_one_year = {"productName": "1年期", "weightedOccupancyAmt": 0, "incomeAmt": 0}
            zl_six_month = {"productName": "6个月-1年期", "weightedOccupancyAmt": 0, "incomeAmt": 0}
            zl_three_month = {"productName": "3个月-6个月", "weightedOccupancyAmt": 0, "incomeAmt": 0}
            zl_three_month_bellow = {"productName": "3个月以下", "weightedOccupancyAmt": 0, "incomeAmt": 0}
            for cd in cd_data:
                if cd.get("QX"):
                    # 查询结束日期年份
                    endDateYear = endDate[0:4]
                    crr_year = str(cd.get("positionCreateDate"))[0:4]
                    qx = 0
                    if cd.get("QX") == None:
                        qx = 0
                    else:
                        qx = cd.get("QX")
                    # 说明是存量
                    if endDateYear > crr_year:
                        # 1年期
                        if qx > 300 and qx <= 365:
                            cl_one_year["weightedOccupancyAmt"] = (cl_one_year.get("weightedOccupancyAmt") if cl_one_year.get("weightedOccupancyAmt") else 0) + cd.get("weightedOccupancyAmt")
                            cl_one_year["incomeAmt"] = (cl_one_year.get("incomeAmt") if cl_one_year.get("incomeAmt") else 0) + cd.get("incomeAmt")
                        # 六个月
                        elif qx > 180 and qx <= 300:
                            cl_six_month["weightedOccupancyAmt"] = (cl_six_month.get("weightedOccupancyAmt") if cl_six_month.get("weightedOccupancyAmt") else 0) + cd.get("weightedOccupancyAmt")
                            cl_six_month["incomeAmt"] = (cl_six_month.get("incomeAmt") if cl_six_month.get("incomeAmt") else 0) + cd.get("incomeAmt")
                        elif qx > 90 and qx <= 180:
                            cl_three_month["weightedOccupancyAmt"] = (cl_three_month.get("weightedOccupancyAmt") if cl_three_month.get("weightedOccupancyAmt") else 0) + cd.get("weightedOccupancyAmt")
                            cl_three_month["incomeAmt"] = (cl_three_month.get("incomeAmt") if cl_three_month["incomeAmt"] else 0) + cd.get("incomeAmt")
                        else:
                            cl_three_month_bellow["weightedOccupancyAmt"] = (cl_three_month_bellow.get("weightedOccupancyAmt") if cl_three_month_bellow.get("weightedOccupancyAmt") else 0) + cd.get("weightedOccupancyAmt")
                            cl_three_month_bellow["incomeAmt"] = (cl_three_month_bellow.get("incomeAmt") if cl_three_month_bellow.get("incomeAmt") else 0) + cd.get("incomeAmt")
                    # 增量
                    else:
                        # 1年期
                        if qx > 300 and qx <= 365:
                            zl_one_year["weightedOccupancyAmt"] = (zl_one_year.get("weightedOccupancyAmt") if zl_one_year.get("weightedOccupancyAmt") else 0) + cd.get("weightedOccupancyAmt")
                            zl_one_year["incomeAmt"] = (zl_one_year.get("incomeAmt") if zl_one_year.get("incomeAmt") else 0) + cd.get("incomeAmt")
                        # 六个月
                        elif qx > 180 and qx <= 300:
                            zl_six_month["weightedOccupancyAmt"] = (zl_six_month.get("weightedOccupancyAmt") if zl_six_month.get("weightedOccupancyAmt") else 0) + cd.get("weightedOccupancyAmt")
                            zl_six_month["incomeAmt"] = (zl_six_month.get("incomeAmt") if zl_six_month.get("incomeAmt") else 0) + cd.get("incomeAmt")
                        # 三个月
                        elif qx > 90 and qx <= 180:
                            zl_three_month["weightedOccupancyAmt"] = (zl_three_month.get("weightedOccupancyAmt") if zl_three_month.get("weightedOccupancyAmt") else 0) + cd.get("weightedOccupancyAmt")
                            zl_three_month["incomeAmt"] = (zl_three_month.get("incomeAmt") if zl_three_month.get("incomeAmt") else 0) + cd.get("incomeAmt")
                        # 三个月以下
                        else:
                            zl_three_month_bellow["weightedOccupancyAmt"] = (zl_three_month_bellow.get("weightedOccupancyAmt") if zl_three_month_bellow.get("weightedOccupancyAmt") else 0) + cd.get("weightedOccupancyAmt")
                            zl_three_month_bellow["incomeAmt"] = (zl_three_month_bellow.get("incomeAmt") if zl_three_month_bellow.get("incomeAmt") else 0) + cd.get("incomeAmt")
            cl_data.append({"cl_one_year": cl_one_year})
            cl_data.append({"cl_six_month": cl_six_month})
            cl_data.append({"cl_three_month": cl_three_month})
            cl_data.append({"cl_three_month_bellow": cl_three_month_bellow})
            zl_data.append({"zl_one_year": zl_one_year})
            zl_data.append({"zl_six_month": zl_six_month})
            zl_data.append({"zl_three_month": zl_three_month})
            zl_data.append({"zl_three_month_bellow": zl_three_month_bellow})
        return {"cl": cl_data, "zl": zl_data}

    """ 计算两个天数间隔 YYYY-MM-dd格式的 """

    def cal_day_between(self, startDate, endDate):
        start_date = datetime.datetime.strptime(startDate, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(endDate, "%Y-%m-%d")
        return (end_date - start_date).days
