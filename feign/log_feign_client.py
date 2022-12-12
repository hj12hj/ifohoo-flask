from feign.nacos_feign_client import NacosFeignClient

logFeignClient = NacosFeignClient("providerServer")


@logFeignClient.customRequestClient(url="/log", method="POST")
def hh():
    pass

@logFeignClient.customRequestClient(url="/log1", method="GET")
def hh1():
    pass
