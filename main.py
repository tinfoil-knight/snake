import time
import curses
import random

directions = {
    curses.KEY_UP: (-1, 0),
    curses.KEY_DOWN: (1, 0),
    curses.KEY_LEFT: (0, -1),
    curses.KEY_RIGHT: (0, 1),
}

class Game:

    def __init__(self):
        self.snake = Snake([(0, i) for i in reversed(range(15))], directions[curses.KEY_RIGHT])
        self.apple = Apple((4,4))

    def main(self, screen):
        curses.curs_set(0)    # Hide the cursor
        screen.nodelay(True)  # Don't block I/O calls
        snake = self.snake

        direction = snake.direction
        score = 0

        state = True

        while state == True:
            try:
                assert(len(snake.body) == len(set(snake.body)))
            except:
                state == False
                screen.erase()
                screen.addstr(0,0, "Thee collid'd unto thy-self!")
                screen.addstr(1,0, f"Thy score : {score}")
                screen.addstr(3,0, "Press Ctrl + C to exit.")
            else:
                try:
                    screen.erase()

                    screen.addstr(*snake.body[0], 'X')
                    for segment in snake.body[1:]:
                        screen.addstr(*segment, 'O')

                    if snake.head() == self.apple.position:
                        score = score + 1
                        # Get a tuple of screen dimensions by using getmaxyx()
                        self.apple.position = self.apple.spawn(screen.getmaxyx())
                        snake.body.insert(0, tuple(map(sum, zip(snake.head(), direction))))

                    screen.addstr(*self.apple.position, '🍎')
                    snake.take_step(direction)

                    direction = directions.get(screen.getch(), direction)
                except:
                    state == False
                    screen.erase() 
                    screen.addstr(0,0, "Thee collid'd into the big wall!")
                    screen.addstr(1,0, f"Thy score : {score}")
                    screen.addstr(3,0, "Press Ctrl + C to exit.")

            screen.refresh()
            time.sleep(0.1)

    def render(self):
        curses.wrapper(self.main)




class Snake:
    def __init__(self, ini_body, ini_direction):
        # ini is initial
        self.body = ini_body
        self.direction = ini_direction

    def take_step(self, direction):
        self.body.pop()
        self.body.insert(0, tuple(map(sum, zip(self.head(), direction))))

    def head(self):
        return self.body[0]


class Apple:
    def __init__(self, position):
        self.position = position

    def spawn(self, dimension):
        return (random.randrange(0, dimension[0]), random.randrange(0, dimension[1]))

# class Error(Exception):
#     """Base class"""
#     pass

# class Collision(Error):
#     """Raised when the Snake collides into itself or the Wall"""
#     def __init__(self, message):
#         self.message = message

game = Game()
game.render()
