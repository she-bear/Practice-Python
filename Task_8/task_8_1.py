"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
[[], [], []]def __init__(self, width, length):

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода add() для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

"""
import numpy as np


class Matrix:
    def __init__(self, width, length, data_matrix=None):
        if data_matrix is None:
            data_matrix = []
        self.width = width
        self.length = length
        self.data_matrix = data_matrix

    def __str__(self):
        return '\n'.join(
            [' '.join([str(j) for j in i]) for i in self.data_matrix])

    def __add__(self, other):
        if (self.width != other.width) or (self.length != other.length):
            return None

        ret = Matrix(self.width, self.length)
        ret.data_matrix = [
            [self.data_matrix[i][j] + other.data_matrix[i][j] for j in
             range(len(self.data_matrix[0]))] for i in
            range(len(self.data_matrix))]
        return ret


matrix_1 = Matrix(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_3 = Matrix(3, 3, [[1, 1, 1], [1, 1, 1], [1, 1, 1]])

print(matrix_1)
print()
print(matrix_1 + matrix_2)
print('Тройное сложение тоже умеем:')
print(matrix_1 + matrix_2 + matrix_3)
print()

# в python для работы с матрицами используется библиотека NumPy
print("Пробуем NumPy...")
a = np.array(((1, 2, 3), (4, 5, 6), (7, 8, 9)))
b = np.array(((1, 1, 1), (2, 2, 2), (3, 3, 3)))
print(a)
print()
print(a + b)
