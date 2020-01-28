import time
import curses

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

        direction = self.snake.direction
        score = 0
        while True:
            screen.erase()

            screen.addstr(*self.snake.body[0], '@')
            for segment in self.snake.body[1:]:
                screen.addstr(*segment, '*')

            if self.snake.head() == self.apple.position:
                score = score + 1
                apple.getNew

            self.snake.take_step(direction)
            direction = directions.get(screen.getch(), direction)

            screen.refresh()
            time.sleep(0.19)

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

    def setNew():
        self.position = (random.randrange(0, 10), random.randrange(0, 10))


game = Game()
game.render()


# Get a tuple of screen dimensions
# screen.getmaxyx()
