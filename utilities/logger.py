import inspect
import logging


class logggen:

    @staticmethod
    def logger():
        LoggerName = inspect.stack()[1][3]
        log = logging.getLogger(LoggerName)

        file_handler = logging.FileHandler('F:\\Pratice_Python\\Project_Automation\\Logs\\logss.log')
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(message)s",datefmt='%Y-%m-%d %H:%M:%S %p')

        file_handler.setFormatter(formatter)

        log.addHandler(file_handler)
        log.setLevel(logging.INFO)
        return log

