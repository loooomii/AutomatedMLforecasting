import pandas as pd


class DataLoader:
    def __init__(self, path):
        self.path = path

    def __data__(self):
        data = pd.read_csv(self.path)
        return data

    def __data_info__(self):
        data = self.__data__()
        return data.info()

    def info(self):
        return self.__data_info__()

    def data(self):
        return self.__data__()