import numpy as np
import os
import time



class MatCal:


    def __init__(self, mat1, mat2):
        self.__mat1 = mat1
        self.__mat2 = mat2

    def add(self):
        """This function serves for adding matrix A and B"""
        if self.__mat1.shape != self.__mat2.shape:
            return None
        else:
            return self.__mat1 + self.__mat2

    def multi(self):
        """This function serves for multiply matrix A and B"""
        if self.__mat1.shape != self.__mat2.shape:
            return None
        return self.__mat1 * self.__mat2

    def matmulti(self):
        if self.__mat1.shape[1] != self.__mat2.shape[0]:
            return None
        return np.matmul(self.__mat1, self.__mat2)

    def sub(self):
        """This function serves for matrix A subtrating matrix B"""
        if self.__mat1.shape != self.__mat2.shape:
            return None
        return self.__mat1 - self.__mat2

    def divide(self):
        """This function serves for matrix A divided by matrix B"""
        if self.__mat1.shape != self.__mat2.shape:
            return None
        return self.__mat1 / self.__mat2




