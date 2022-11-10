import math
from typing import List


def golden_fibonacci(n: int) -> int:
    fi = (1 + math.sqrt(5)) / 2
    fn = int(fi ** n / math.sqrt(5) + 1 / 2)
    return fn


def print_matrix(matrix: [[int], [int]]) -> None:
    for i in matrix:
        for j in i:
            print(f'{j}  ', end='')
        print()
    print()


class Matrix:
    @staticmethod
    def mul_matrix(matrix_a: [[int], [int]], matrix_b: [[int], [int]]) -> [[int], [int]]:
        rows_a = len(matrix_a)
        cols_a = len(matrix_a[0])
        cols_b = len(matrix_b[0])

        if cols_a != rows_a:
            print("Матрицы разного размера")
            return
        new_matrix = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

        for i in range(rows_a):
            for j in range(cols_b):
                for k in range(cols_a):
                    new_matrix[i][j] += matrix_a[i][k] * matrix_b[k][j]

        return new_matrix

    @staticmethod
    def sqr_matrix(matrix: [[int], [int]]) -> [[int], [int]]:
        rows_a = len(matrix)
        cols_a = len(matrix[0])
        new_matrix = [[0 for _ in range(cols_a)] for _ in range(rows_a)]
        for i in range(rows_a):
            for j in range(cols_a):
                for k in range(cols_a):
                    new_matrix[i][j] += matrix[i][k] * matrix[k][j]
        return new_matrix

    @staticmethod
    def pow_matrix(matrix: [[int], [int]], n: int) -> [[int], [int]]:
        d = matrix
        i = n
        p = [[1, 1], [1, 0]]
        while i >= 1:
            i //= 2
            d = Matrix.sqr_matrix(d)
            if i % 2 != 0:
                p = Matrix.mul_matrix(p, d)
        if n % 2 == 1:
            p = Matrix.mul_matrix(p, matrix)
        return p


def matrix_fibonacci(n: int) -> int:
    m = [[1, 1], [1, 0]]
    m = Matrix.pow_matrix(m, n - 2)
    return m[0][0]


if __name__ == '__main__':
    print('Фибоначчи через золотое сечение')
    print(golden_fibonacci(10))
    print(golden_fibonacci(15))
    print(golden_fibonacci(20))
    print('Фибоначчи через матрицы')
    m = [[1, 1], [1, 0]]
    m = Matrix.sqr_matrix(m)
    m = Matrix.sqr_matrix(m)
    m = Matrix.sqr_matrix(m)  # F(9)
    print_matrix(m)
    m = [[1, 1], [1, 0]]
    m = Matrix.pow_matrix(m, 7)  # F(9)
    print_matrix(m)
    print(matrix_fibonacci(25))
    print(golden_fibonacci(25))
