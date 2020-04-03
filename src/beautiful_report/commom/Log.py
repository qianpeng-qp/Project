import logging
import tools, os


class Log:
    __logger = None  # 定义类的私有属性 默认值为 None

    def __new__(cls, *args, **kwargs):
        if cls.__logger == None:
            # 创建一下 日志类， 'cnodeApi' 为 logging name属性值
            cls.__logger = logging.getLogger('cnodeApi')
            cls.__logger.setLevel(logging.DEBUG)  # 设置日志级别 DEBUG

            log_path = tools.filepath('logs')
            logfile_path = os.path.join(log_path, 'api.log')
            fh = logging.FileHandler(logfile_path)  # 创建日志存储文件对象 app.log 日志存储文件名
            ch = logging.StreamHandler()  # 命令行输出流

            # log格式
            formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s %(message)s')

            fh.setFormatter(formatter)  # 文件存储赋给 __logger
            ch.setFormatter(formatter)  # 输出流 添加日志格式

            cls.__logger.addHandler(fh)  # 文件存储赋给 __logger
            cls.__logger.addHandler(ch)  # 输出流 赋给 __logger

        return cls.__logger


if __name__ == '__main__':
    log1 = Log()
    log2 = Log()
    print(log1 == log2)
    log1.debug('hello')
