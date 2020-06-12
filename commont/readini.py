import configparser
from commont.getpathg import GetPath


class ReadIni:

        def __init__(self, file_path):
            self.file_path = file_path
            self.data=self.read_ini()
        def read_ini(self):
            config =configparser.ConfigParser()
            config.read(self.file_path)
            return config

        # 通过key获取对应的value
        # def get_section(self,section):
        #     try:
        #         value=self.data.get(section)
        #     except:
        #         print("")
        #     return value
        def get_value(self, section,key):
            try:
                value = self.data.get(section,key)
            except:
                value = None
            return value
if __name__ == '__main__':
    filepath = GetPath().filepath("data", "element.ini")
    print(filepath)
    r=ReadIni(filepath)
    print(r.data)
    value=r.get_value("login_element","username")
    print(value)

