from functools import wraps
from variables import local_token
import requests

from registry import registry

host_ip = None
host_port = None
"""
用于类似openFeign封装
用法：
logFeignClient = NacosFeignClient(注册到nacos的服务名)

标注请求url和请求方法
@logFeignClient.customRequestClient(url="/log", method="POST")
def hh():
    pass

函数传参 
params = {"name": "hh"}    
json={"name": "hh", "age": 18}    
直接调用    
hh(json={"name": "hh", "age": 18})

"""


# todo 负载均衡客户端未写

# nacosFeign客户端
class NacosFeignClient:
    def __init__(self, service_name, group="DEFAULT_GROUP"):
        self.service_name = service_name

    def customRequestClient(self, url, method, requestParamJson=False, https=False):
        def requestPro(f):
            @wraps(f)
            def mainPro(*args, **kwargs):
                token = local_token.token
                # 获取参数
                global host_ip, host_port
                data = kwargs.get("data")
                params = kwargs.get("params")
                json = kwargs.get("json")
                headers = {"token": token}
                host_list = registry.get_instance_by_service_name(self.service_name)
                if len(host_list) > 0:
                    host_ip = host_list[0].get("ip")
                    host_port = host_list[0].get("port")
                if host_ip is None or host_port is None:
                    raise Exception("未找到服务 {0}".format(self.service_name))
                reuqest_url = "http://" + host_ip + ":" + str(host_port) + url
                return requests.request(url=reuqest_url, data=data, params=params, json=json,
                                        method=method, headers=headers).content.decode(
                    'UTF8')

            return mainPro

        return requestPro
