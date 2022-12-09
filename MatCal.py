import numpy as np


class MatCal:


    def __init__(self, mat1, mat2):
        self.__mat1 = mat1
        self.__mat2 = mat2

    def add(self):
        """This function does addition of the two numbers mat1 and mat2"""
        if self.__mat1.shape != self.__mat2.shape:
            return None
        else:
            return self.__mat1 + self.__mat2

    def multi(self):
        """This function does multiplication of the two numbers mat1 and mat2"""
        if self.__mat1.shape != self.__mat2.shape:
            return None
        return self.__mat1 * self.__mat2

    def matmulti(self):
        """This function does multiplication of the two matrix A and B"""
        if self.__mat1.shape[1] != self.__mat2.shape[0]:
            return None
        return np.matmul(self.__mat1, self.__mat2)

    def sub(self):
        """This function does subtraction of the two numbers mat1 and mat2"""
        if self.__mat1.shape != self.__mat2.shape:
            return None
        return self.__mat1 - self.__mat2

    def divide(self):
        """This function does division of the two numbers mat1 and mat2"""
        if self.__mat1.shape != self.__mat2.shape:
            return None
        return self.__mat1 / self.__mat2




