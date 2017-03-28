import pygame
import sys

pygame.init()

#all box properties.
BOX_WIDTH = 100
BOX_HEIGHT = 30
BOX_LINE_SIZE = 0

class box_class:
    def __init__(self, screen, x, y):
        self.y = y
        self.x = x
        self.width = BOX_WIDTH
        self.height = BOX_HEIGHT
        self.show = False
        self.center = (int(screen_matrix[self.y][self.x][0] + 10 + (BOX_WIDTH/2)),
                       int(screen_matrix[self.y][self.x][1] +10 +(BOX_HEIGHT/2)))
        self.screen = screen
        box = pygame.draw.rect(screen, BLUE,
                               [screen_matrix[y][x][0] + 10, screen_matrix[y][x][1] + 10, self.width,
                                self.height],
                               BOX_LINE_SIZE)

    def flash(self):
        clock = pygame.time.Clock()
        for i in range(100):
            box = pygame.draw.rect(self.screen, (50, 220-i, 255-i),
                                   [screen_matrix[self.y][self.x][0] + 10, screen_matrix[self.y][self.x][1] + 10, self.width,
                                    self.height],
                                   BOX_LINE_SIZE)
            pygame.display.update()

            clock.tick(300)


    def connect(self, to_box):
        line = pygame.draw.line(screen, BLUE , self.center, to_box.center, 5)
        pygame.display.update()

    def send_signal_to(self, to_box):
        clock = pygame.time.Clock()
        high_center = (self.center[0] if self.center[0] > to_box.center[0] else to_box.center[0],
                       self.center[1] if self.center[1] > to_box.center[1] else to_box.center[1])
        low_center = (self.center[0] if self.center[0] < to_box.center[0] else to_box.center[0],
                      self.center[1] if self.center[1] < to_box.center[1] else to_box.center[1])
        dir = LEFT if self.center[0] > to_box.center[0] else RIGHT

        dx = int(high_center[0] - low_center[0])
        dy = int(high_center[1] - low_center[1])
        px = 0
        py = int(self.center[1] + dy * ((px - self.center[0]) / (1 if dx == 0 else dx)))
        for x in range(0, dx):
            y = int(self.center[1] + dy * ((x - self.center[0]) / (1 if dx == 0 else dx)))
            self.connect(to_box)
            if dir == LEFT:
                x *= -1
            line = pygame.draw.line(screen, WHITE, (x+self.center[0],y), (px+self.center[0], py),5)
            pygame.display.update()
            clock.tick(300)
            px = x
            py = y
        dir = UP if self.center[1] > to_box.center[1] else DOWN
        px = int(self.center[0] + dx * ((py - self.center[1]) / (1 if dy == 0 else dy)))
        py = 0
        for y in range(0, dy):
            x = int(self.center[0] + dx * ((y - self.center[1]) / (1 if dy == 0 else dy)))
            self.connect(to_box)
            if dir == UP:
                y *= -1
            line = pygame.draw.line(screen, WHITE, (x,y +self.center[1] ), (px, py+self.center[1]),5)
            pygame.display.update()
            clock.tick(500)
            px = x
            py = y
        to_box.flash()



# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 120, 155)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#directions
LEFT = 1
RIGHT = 2
UP = 3
DOWN = 4

#Screen properties
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
size = [SCREEN_WIDTH, SCREEN_HEIGHT]

# divide the screen spaces 5 by 5 matrix
CELL_WIDTH = SCREEN_WIDTH / 5
CELL_HEIGHT = SCREEN_HEIGHT / 5

screen_matrix = [[[0 * CELL_WIDTH, 0 * CELL_HEIGHT],
                  [0 * CELL_WIDTH, 2 * CELL_HEIGHT],
                  [0 * CELL_WIDTH, 4 * CELL_HEIGHT]],
                 [[2 * CELL_WIDTH, 0 * CELL_HEIGHT],
                  [2 * CELL_WIDTH, 2 * CELL_HEIGHT],
                  [2 * CELL_WIDTH, 4 * CELL_HEIGHT]],
                 [[4 * CELL_WIDTH, 0 * CELL_HEIGHT],
                  [4 * CELL_WIDTH, 2 * CELL_HEIGHT],
                  [4 * CELL_WIDTH, 4 * CELL_HEIGHT]]]

box_matrix = [[0, 1, 0],
              [1, 1, 1],
              [0, 1, 0]]

boxes = [[1, 2, 3],
         [1, 2, 3],
         [1, 2 ,3]]

# MAIN DISPLAY STARTS FROM HERE.
# create screen
screen = pygame.display.set_mode(size)
screen.fill(BLACK)

#obj = pygame.Surface(screen_matrix[2][2]).convert()
#obj.fill(BLACK)

for i in range(3):
    for j in range(3):
        if box_matrix[i][j] == 1:
            b = box_class(screen, i, j)
            boxes[i][j] = b
            b.show = True

close = False
clock = pygame.time.Clock()

while not close:
    clock.tick(100)
    # look for the quit event and close the screen.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                boxes[1][0].send_signal_to(boxes[1][1])
                boxes[0][1].send_signal_to(boxes[1][1])
                boxes[1][2].send_signal_to(boxes[1][1])
                boxes[2][1].send_signal_to(boxes[1][1])

    boxes[1][0].connect(boxes[1][1])
    boxes[1][2].connect(boxes[1][1])
    boxes[0][1].connect(boxes[1][1])
    boxes[2][1].connect(boxes[1][1])
    pygame.display.update()
