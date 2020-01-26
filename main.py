# UP = (0, 1)
# DOWN = (0, -1)
# LEFT = (-1, 0)
# RIGHT = (1, 0)
import time

UP = (1, 0)
DOWN = (-1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

# UNIVERSAL METHODS
def cX(tuple):
    return tuple[0]

def cY(tuple):
    return tuple[1]

def addX(setA, setB):
    return cX(setA) + cX(setB)

def addY(setA, setB):
    return cY(setA) + cY(setB)

def addCo(setA, setB):
    return (addX(setA, setB), addY(setA, setB))



class Snake:
    def __init__(self, ini_body, ini_direction):
        # ini is initial
        self.body = ini_body
        self.direction = ini_direction

    def take_step(self, position):
        self.body = self.body[1:] + [position]
        # self.body = [ (self.body[1:][[i][0]]+position[0], self.body[1:][[i][1]]+position[1]) for i in self.body[1:] ]

    def set_direction(self, direction):
        self.direction = direction

    def head(self):
        return self.body[-1]

    def process(self, direction):
        # TODO: Write a method that runs take_step and set_direction
        pass




class Apple:
    pass


class Game:

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.snake = Snake([(0, 0), (1, 0), (2, 0), (3, 0)], UP)

    def boardMatrix(self):
        return [[" " for i in range(self.width)] for j in range(self.height)]

    def render(self):
        matrix = self.boardMatrix()


        snake = self.snake
        print(snake.body)

        matrix[snake.body[-1][0]][snake.body[-1][1]] = "X"
        for set in snake.body[:-1]:
            matrix[set[0]][set[1]] = "O"

        # Reversing the matrix so that (0, 0) is at bottom
        reverse = matrix[::-1]
        print("+----------+")
        for row in reverse:
            print("|", end="")
            for cell in row:
                if cell == "X" or "O":
                    print('\033[32m'+cell+'\033[39m', end="")
                else:
                    print(cell, end="")
            print("|")
        print("+----------+")





game = Game(10, 10)
game.render()

def runTheGame():
        snake = game.snake
        copy = snake.body.copy()

        def process():
            game.render()
            for cell in copy:
                if snake.head() == cell:
                    print("You collided unto thyself!")
                    print("You Lost!")
                    exit(2)


        x = input()
        if len(x) != 1:
            print("Press one key at a time.")
            exit(3)
        elif x == "w":
            if snake.direction == DOWN:
                print("You Lost!")
                exit(1)
            snake.set_direction(UP)
            snake.take_step(addCo(snake.head(), UP))
            process()
        elif x == "a":
            if snake.direction == RIGHT:
                print("You Lost!")
                exit(1)
            snake.set_direction(LEFT)
            snake.take_step(addCo(snake.head(), LEFT))
            process()
        elif x == "s":
            if snake.direction == UP:
                print("You Lost!")
                exit(1)
            snake.set_direction(DOWN)
            snake.take_step(addCo(snake.head(), DOWN))
            process()
        elif x == "d":
            if snake.direction == LEFT:
                print("You Lost!")
                exit(1)
            snake.set_direction(RIGHT)
            snake.take_step(addCo(snake.head(), RIGHT))
            process()
        else:
            print("You are pressing the wrong keys.")
 # and reset to default color
while True:
    runTheGame()



# snake.take_step(addCo(snake.head(), snake.direction))
# time.sleep(1)
# game.render()

# UP = (0, 1)
# DOWN = (0, -1)
# RIGHT = (1, 0)
# LEFT = (-1, 0)
# You can add for diagonal movements like L+U, R+U, L+D, R+D

# Body is stored as an array of tuples(co-ordinates). That means when snake moves,
# the coordinate of the last part is removed (first element of array)
# New position is added to the end of the list(i.e. after snake's head)
