import yaml

from commont.getpathg import GetPath


class GetData:
    ##读取yaml文件的数据并返回
    def read_yaml(self, filepath):
        with open(filepath, 'r') as f:
            yaml_data = yaml.safe_load(f)
        return yaml_data

    def yaml_data(self, filepath, key):
        ##获取yaml文件中指定key的值
        yaml_data = self.read_yaml(filepath)
        data = yaml_data[key]
        return data
if __name__ == '__main__':
    g=GetPath()
    filepath=g.filepath("data","hub.yaml")
    print(filepath)
    d=GetData()
    yamldata=d.read_yaml(filepath)
    print(yamldata)
    data=d.yaml_data(filepath,"hub")
    print(data)
    print(data["brows"][0])
