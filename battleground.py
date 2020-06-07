class Battleground:
    gladiators = []

    def __init__(self, width, length):
        self.width = width
        self.length = length
        self.matrix = [["x" for i in range(self.width)] for j in range(self.length)]
        self.end = False

    def __str__(self):
        return self.matrix

    def get_matrix(self):
        return self.matrix

    def set_matrix(self, matrix):
        self.matrix = matrix

    def add_gladiator(self, gladiator):
        self.gladiators.append(gladiator)

    def remove_gladiator(self, gladiator):
        gladiator.alive == False
        self.clear_field(gladiator.x, gladiator.y)
        self.gladiators.remove(gladiator)
        if len(self.gladiators) < 2:
            self.end = True

    def is_empty(self, pos):
        y, x = pos
        if self.matrix[y][x] == "x":
            return True
        else:
            return False

    def move_player(self, id, newPos):
        gladiator = self.gladiators[id]
        if gladiator.x != -1 and gladiator.y != -1:
            self.clear_field(gladiator.x, gladiator.y)
        self.matrix[newPos[0]][newPos[1]] = gladiator
        gladiator.y, gladiator.x = newPos

    def clear_field(self, x, y):
        self.matrix[y][x] = "x"