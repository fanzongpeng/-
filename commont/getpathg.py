import os


class GetPath:
    def dirpath(self) -> str:
        ##获取文件的目录的目录
        dirpath = os.path.dirname(os.path.dirname(__file__))
        return dirpath

    def filepath(self, dirname: str, filename: str) -> str:
        ##拼接文件的路径，目录名和文件名
        dirpath = self.dirpath()
        filepath = os.path.join(dirpath, dirname, filename)
        return filepath


if __name__ == '__main__':
    g = GetPath()
    g.dirpath()
    print(type(g.filepath("data", "hub.yaml")))
