import pandas as pd

"""
    This class is used to load the data from the path provided.
"""


class DataLoader:
    """
        A class for loading the data from the path provided.
    """

    def __init__(self, path):
        """
        Constructor
        :param path: path of the data file.
        """
        # TODO：添加path
        self.path = path

    def __data__(self):
        data = pd.read_csv(self.path)
        return data

    def __data_info__(self):
        data = self.__data__()
        return data.info()

    """
        This method is for calculating the volatility estimator of the data.
    """
    def __estimator__(self):
        # TODO: 添加realized volatility的计算
        pass

    """
        This method returns the data information.
    """

    def info(self):
        return self.__data_info__()

    """
        This method returns the data itself.
    """

    def data(self):
        return self.__data__()
