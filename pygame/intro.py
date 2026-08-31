import pygame as p

p.init()

screen_width = 800
screen_height = 600

screen = p.display.set_mode((screen_width,screen_height))

player = p.Rect((300,250,50,50))

run = True
while run:

    p.draw.rect(screen, (255,0,0), player)

    key = p.key.get_pressed()
    if key[p.K_a] == True:
        player.move_ip(-1,0)
    key = p.key.get_pressed()
    if key[p.K_d] == True:
        player.move_ip(1,0)
    key = p.key.get_pressed()
    if key[p.K_w] == True:
        player.move_ip(0,-1)
    key = p.key.get_pressed()
    if key[p.K_s] == True:
        player.move_ip(0,1)

for event in p.event.get():
    if event.type == p.quit:
        run = False

    p.display.update()

p.quit()


