import pygame as p

p.init()

screen_width = 800
screen_height = 600

screen = p.display.set_mode((screen_width, screen_height))
p.display.set_caption("Pygame")

player = p.Rect((300, 250, 50, 50))

run = True

while run:

    screen.fill((245, 245, 220))  # clear the screen each frame
    p.draw.rect(screen,(173, 216, 230) , player)

    key = p.key.get_pressed()
    if key[p.K_a]:
        player.move_ip(-1, 0)
    if key[p.K_d]:
        player.move_ip(1, 0)
    if key[p.K_w]:
        player.move_ip(0, -1)
    if key[p.K_s]:
        player.move_ip(0, 1)

    for event in p.event.get():
        if event.type == p.QUIT:
            run = False

    p.display.update()

p.quit()