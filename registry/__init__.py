from registry.nacos_registry import NacosRegistry
from config import configContent
from netifaces import interfaces, ifaddresses, AF_INET

addresses = []
local_ip = "127.0.0.1"
# 获取本机Ip
for ifaceName in interfaces():
    addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr': 'No IP addr'}])]
    addresses = [i for i in addresses if i != 'No IP addr']
    for address in addresses:
        if address != "127.0.0.1":
            local_ip = address
            break

nacosConfig = configContent.get("nacos")
applicationConfig = configContent.get("application")
port = applicationConfig.get("port")
dataId = nacosConfig.get("dataId")

applicationIp = applicationConfig.get("ip")
if applicationIp is None or applicationIp == "127.0.0.1":
    applicationIp = local_ip

# 初始化nacos todo 这里可以通过配置文件初始化nacos还是Eukera
registry = NacosRegistry(**nacosConfig,
                         client_info={"service_name": applicationConfig.get("name"), "ip": applicationIp,
                                      "port": applicationConfig.get("port"), "group": applicationConfig.get("group")})
# 注册服务
registry.register()

# 获取配置中心配置
config = registry.get_config(data_id=dataId)

