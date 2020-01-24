class Snake:
    pass
class Apple:
    pass
class Game:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def boardMatrix(self):
        return [[" " for i in range(4)] for j in range(4)]
    def render(self):
        matrix = self.boardMatrix()
        print("+----+")
        for row in matrix:
            print("|", end="")
            for cell in row:
                print(cell, end="")
            print("|")
        print("+----+")
    pass

game = Game(10, 20)
game.render()
