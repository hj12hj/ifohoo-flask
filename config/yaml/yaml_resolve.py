import yaml


class YamlResolve:
    def __init__(self):
        with open('application.yaml', encoding="utf-8") as f:
            self.data = yaml.load(f, Loader=yaml.FullLoader)

    def get_local_config(self):
        return self.data
