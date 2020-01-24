UP = (0, 1)
DOWN = (0, -1)
RIGHT = (1, 0)
LEFT = (-1, 0)

class Snake:
    def __init__(self, ini_body, ini_direction):
        # ini is initial
        self.body = ini_body
        self.direction = ini_direction

    def take_step(self, position):
        self.body = self.body[1:] + [position]

    def set_direction(self, direction):
        self.direction = direction

    def head(self):
        return self.body[-1]


class Apple:
    pass


class Game:

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.snake = Snake([(0, 0), (1, 0), (2, 0), (3, 0)], DOWN)

    def boardMatrix(self):
        return [[" " for i in range(self.width)] for j in range(self.height)]

    def render(self):
        matrix = self.boardMatrix()


        snake = self.snake
        matrix[snake.body[-1][0]][snake.body[-1][1]] = "X"
        for set in snake.body[:-1]:
            matrix[set[0]][set[1]] = "#"

        print("+----------+")
        for row in matrix:
            print("|", end="")
            for cell in row:
                print(cell, end="")
            print("|")
        print("+----------+")




game = Game(10, 10)
game.render()
# UP = (0, 1)
# DOWN = (0, -1)
# RIGHT = (1, 0)
# LEFT = (-1, 0)
# You can add for diagonal movements like L+U, R+U, L+D, R+D

# Body is stored as an array of tuples(co-ordinates). That means when snake moves,
# the coordinate of the last part is removed (first element of array)
# New position is added to the end of the list(i.e. after snake's head)
