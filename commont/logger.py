import logging
import time


class Logger:
    def logger(self):
        logger=logging.getLogger("logger")
        logger.setLevel(logging.DEBUG)
        stream=logging.StreamHandler()
        file=logging.FileHandler(filename="E:\阳光产险只能生命表系统\log\{}-log.txt".format(time.strftime("%y%m%d%H%M%S",time.localtime())),
                                      encoding="utf-8")
        logger.addHandler(stream)
        logger.addHandler(file)
        fomate=logging.Formatter(fmt=" %(asctime)s 方法：%(funcName)s 目录：%(filename)s %(message)s",
                                      datefmt="%y%m%d%H%M%S")
        stream.setFormatter(fomate)
        file.setFormatter(fomate)

        return logger
        # self.logger.debug("这是debug数据")




if __name__ == '__main__':
    f=Logger()
    f.logger()