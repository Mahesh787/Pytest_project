import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class Readconfig:

    @staticmethod
    def getApplicationUrl():
        URL = config.get('common info','Base_URl')
        return URL

    @staticmethod
    def getUsername():
        USERNAME = config.get('common info', 'Username')
        return USERNAME

    @staticmethod
    def getPassword():
        PASSWORD = config.get('common info', 'Password')
        return PASSWORD

