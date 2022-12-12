import yaml


class YamlResolve:
    def __init__(self):
        with open('application.yaml') as f:
            self.data = yaml.load(f, Loader=yaml.FullLoader)

    def get_local_config(self):
        return self.data
