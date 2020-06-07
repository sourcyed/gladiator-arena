import random

class Gladiator:
    def __init__(self, battleground, name, speed, dmg, hp):
        self.battleground = battleground
        self.name = name
        self.speed = speed
        self.dmg = dmg
        self.hp = hp
        self.x = -1
        self.y = -1
        self.battleground.add_gladiator(self)
        self.__set_start_position()
        self.alive = True

    def __str__(self):
        return "{}-{}".format(self.name, self.hp)

    def __set_start_position(self):
        while True:
            start_pos = (random.randint(0, self.battleground.length - 1),
                        random.randint(0, self.battleground.width - 1))
            if self.battleground.is_empty(start_pos):
                self.move(start_pos)
                break

    def id(self):
        return self.battleground.gladiators.index(self)

    def play(self):
        if self in self.battleground.gladiators:
            for _ in range(self.speed):
                nearest = self.find_nearest()
                new_pos = self.find_fastest_route(nearest)

                if self.battleground.matrix[new_pos[0]][new_pos[1]] == "x":
                    self.move(new_pos)
                if self.battleground.matrix[new_pos[0]][new_pos[1]] != "x" and self.battleground.matrix[new_pos[0]][new_pos[1]] != self:
                    self.attack(nearest)

    def find_nearest(self):
        gladiators = self.battleground.gladiators
        positions = []
        for i, gladiator in enumerate(gladiators):
            positions.append((i,abs(self.x - gladiator.x) + abs(self.y - gladiator.y)))
            
        positions.sort(key = lambda x: x[1])
        positions.pop(0)

        nearest = []
        nearest.append(positions[0])
        for i in range(len(positions) - 1):
            if positions[0][1] == positions[i + 1][1]:
                nearest.append(gladiators[positions[i][0]])
        
        return gladiators[positions[0][0]]
        

    def attack(self, enemy):
        #print("{} attacked {}.".format(str(self),str(enemy)))
        enemy.hp -= self.dmg
        if enemy.hp <= 0:
            self.battleground.remove_gladiator(enemy)

    def find_fastest_route(self, nearest):
        diff = (nearest.y - self.y, nearest.x - self.x)

        x, y = self.x, self.y

        if abs(diff[0]) > abs(diff[1]):
            move_vertical = True 

        elif abs(diff[0] < diff[1]):
            move_vertical = False

        else:
            move_vertical = bool(random.getrandbits(1))

        if move_vertical:
            if diff[0] > 0:
                y += 1
            elif diff[0] < 0:
                y -= 1
        else:
            if diff[1] > 0:
                x += 1
            elif diff[1] < 0:
                x -= 1

        new_pos = (y,x)
        #print(self.name, "-", diff, " - ", (self.y,self.x), new_pos)
        return new_pos


    def move(self, new_pos):
        self.battleground.move_player(self.id(), new_pos)
