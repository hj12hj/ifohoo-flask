from config.yaml.yaml_resolve import YamlResolve

yamlResolve = YamlResolve()
configContent = yamlResolve.get_local_config()
dataId = configContent.get("nacos").get("dataId")
dbInfo = configContent.get("dbInfo")
redisConfig = configContent.get("redis")
