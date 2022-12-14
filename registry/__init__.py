from netifaces import interfaces, ifaddresses, AF_INET

from config import configContent
from registry.nacos_registry import NacosRegistry
import yaml

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

print("Star register Server")
print("nacos_config is ----->>>>  " + str(nacosConfig))
print("local_server_config_is ---->>>> " + str(applicationConfig))

applicationIp = applicationConfig.get("ip")
if applicationIp is None or applicationIp == "127.0.0.1":
    applicationIp = local_ip

# 初始化nacos todo 这里可以通过配置文件初始化nacos还是Eukera
registry = NacosRegistry(**nacosConfig,
                         client_info={"service_name": applicationConfig.get("name"), "ip": applicationIp,
                                      "port": applicationConfig.get("port"), "group": applicationConfig.get("group")})
# 注册服务
registry.register()

print("Register Server Successful")

# 获取配置中心配置 todo 配置中心配置应该覆盖本地的配置
try:
    config = yaml.safe_load(registry.get_config(data_id=dataId))
except Exception as e:
    config = None

if config is not None:
    remote_applicationConfig = config.get("application")
    remote_port = config.get("port")

    if remote_applicationConfig is not None:
        applicationConfig = remote_applicationConfig
        port = applicationConfig.get("port")

print("pull Config from center is ---->>>> " + str(config))
