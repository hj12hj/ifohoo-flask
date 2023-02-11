from feign.nacos_feign_client import NacosFeignClient

dataCenterFeignClient = NacosFeignClient("datacenter")
costAccountingFeignService = NacosFeignClient("costAccounting")

"""
币种Map
"""


@dataCenterFeignClient.customRequestClient(url="/basic/dcCurrency/map", method="GET")
def findCurrencyMap():
    pass


@dataCenterFeignClient.customRequestClient(url="/secu/secuCategory/map", method="GET")
def findSecuCategoryMap():
    pass
