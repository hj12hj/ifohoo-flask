import time
import nacos
import threading


# Nacos 注册中心实现


class NacosRegistry:
    def __init__(self, serverAddr, namespace, username, password, group, dataId, client_info):
        # nacos服务端信息
        self.client = nacos.NacosClient(server_addresses=serverAddr, namespace=namespace, username=username,
                                        password=password)
        # 客户端信息
        self.client_info = client_info

    def register(self):
        service_name = self.client_info.get("service_name")
        ip = self.client_info.get("ip")
        port = self.client_info.get("port")
        group = self.client_info.get("group")
        self.client.add_naming_instance(service_name=service_name, ip=ip, port=port, group_name=group,
                                        cluster_name="DEFAULT")
        # 开启线程定时发送心跳
        heart_beat_thread = threading.Thread(target=self.heart_beat, args=(service_name, ip, port, group))
        heart_beat_thread.daemon = True
        heart_beat_thread.start()

    # 根据服务名字获取 host列表
    def get_instance_by_service_name(self, service_name):
        service_info = self.client.list_naming_instance(service_name)
        host_list = service_info.get("hosts")
        return host_list

    # 五秒一次心跳
    def heart_beat(self, service_name, ip, port, group):
        while True:
            try:
                self.client.send_heartbeat(service_name=service_name, ip=ip, port=port, group_name=group,
                                           cluster_name="DEFAULT")
                time.sleep(5)
            except Exception as e:
                print(e)

    def get_config(self, data_id, group="DEFAULT_GROUP"):
        return self.client.get_config(data_id=data_id, group=group)




# if __name__ == '__main__':
#     # 获取Nacos客户端工具，四个参数(Nacos服务器地址，命名空间，用户名，密码)
#     registry = NacosRegistry("127.0.0.1:8848", "public", "nacos", "nacos",
#                              {"service_name": "nacos.test.service", "ip": "127.0.0.1", "port": 8080,
#                               "group": "DEFAULT_GROUP"})
#     registry.register()
#
#     time.sleep(1000000)
