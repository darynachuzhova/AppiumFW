import configparser
import os

def readConfigData(section, key):
    config = configparser.ConfigParser()
    configPath = os.path.join(os.path.dirname(__file__), "..", "TestData", "config.ini")
    config.read(configPath)
    return config.get(section, key)
