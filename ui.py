from gladiator import Gladiator

class UI:
    def __init__(self, space_length):
        self.space_length = space_length

    def get_space(self, space_length):
        return "".join([" " for i in range(space_length)])

    def show_matrix(self, matrix):
        print(self.matrix_to_str(matrix))

    def matrix_to_str(self,matrix):
        matrix_str = []
        for row in matrix:
            for column in row:
                tmp_space_length = self.space_length
                if type(column) == Gladiator:
                    tmp_space_length -= len(str(column)) - 1

                matrix_str.append(str(column) + self.get_space(tmp_space_length))
                
            matrix_str.append("\n")

        return "".join(matrix_str)