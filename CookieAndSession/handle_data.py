import yaml
import os

upPath = os.path.abspath(os.path.dirname(__file__))
yaml_path = os.path.join(upPath, 'config.yaml')


# 获取yaml文件数据
def get_yaml():
    f = open(yaml_path, 'rb')
    config = yaml.load(f)
    f.close()
    return config
