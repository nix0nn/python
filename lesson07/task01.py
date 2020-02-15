from sys import argv


class Matrix:
    def __init__(self, *args):
        self.array = args

    def __str__(self):
        line = ''
        for i, _ in enumerate(self.array):
            line += str(self.array[i]) + '\n'
        return line

    def __add__(self, other):
        new_array = []
        for i in range(len(self.array)):
            list_a = []
            new_array.append(list_a)
            for j in range(len(self.array[i])):
                list_a.append((int(self.array[i][j]) + int(other.array[i][j])))
        return Matrix(new_array)


matrix_one = Matrix([20, 22], [37, 49], [51, 86])
matrix_two = Matrix([28, 35], [18, 69], [30, 69])

print(matrix_two + matrix_one)

