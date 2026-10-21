import pygame as pg

### SET-UP

pg.init()
pg.display.set_caption('IT2 spill-mal')
WIDTH = 450
HEIGHT = 450
screen = pg.display.set_mode((WIDTH,HEIGHT))
FPS = 60
clock = pg.time.Clock()
run = True
game_objects = []


### KLASSER

class GameObject:
    def __init__(self, x_pos=0, y_pos=0):
        self.x_size = 50    #piksler
        self.y_size = 50    #piksler

        self.x_pos = x_pos
        self.y_pos = y_pos
        
        self.rect = pg.Rect(self.x_pos,self.y_pos,self.x_size, self.y_size)
    def draw(self):
        global screen

        pg.draw.rect(screen, (150,0,0), self.rect)


### FUNKSJONER

def actions():
    global run
    events = pg.event.get()
    keys = pg.key.get_pressed()
    mouse_buttons = pg.mouse.get_pressed()
    mouse_pos = pg.mouse.get_pos()

    #system shutdown
    if keys[pg.K_ESCAPE]:
        run = False

    for event in events:
        if event.type == pg.QUIT:
            run = False

def draw():
    global screen, game_objects

    screen.fill((45,60,100))

    for object in game_objects:
        object.draw()

    pg.display.update()


### IN-GAME OBJECTS

p1 = GameObject(100,100)

game_objects.append(p1)


### GAME-LOOP

while run:
    actions()

    draw()

    clock.tick(FPS)