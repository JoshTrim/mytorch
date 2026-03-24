import numpy as np
from numpy import ndarray

class Tensor:

    def __init__(self, data: list | ndarray | int):
        
        if not isinstance(data, ndarray):
            self.data = np.ndarray(data)
        else:
            self.data = data

        self.shape = self.data.shape
        self.size = self.data.size
        self.dtype = self.data.dtype

    def __add__(self, other: Tensor | int):
        if isinstance(other, Tensor):
            return Tensor(self.data + other.data)
        else:
            return Tensor(self.data + other)

    def __sub__(self, other: Tensor | int):
        pass

    def __mul__(self, other: Tensor | int):
        pass

    def __truediv__(self, other: Tensor | int):
        pass

    def matmul(self, other: Tensor | int) -> Tensor:
        pass

    def reshape(self, shape: int | tuple) -> Tensor:
        pass

    def transpose(self, other: Tensor | int) -> Tensor:
        pass

    def sum(self, other: Tensor | int) -> Tensor:
        pass

    def mean(self, other: Tensor | int) -> Tensor:
        pass

    def max(self, other: Tensor | int) -> Tensor:
        pass

t = Tensor(1)
