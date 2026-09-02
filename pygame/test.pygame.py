import pygame
import math
import random

pygame.init()

WIDTH, HEIGHT = 1100, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hill Climb - Pygame")
clock = pygame.time.Clock()

# Colors
SKY = (135, 206, 235)
GROUND = (105, 180, 75)
GROUND_DARK = (65, 120, 45)
CAR_RED = (210, 45, 45)
CAR_DARK = (45, 45, 50)
WHEEL = (30, 30, 30)
WHITE = (255, 255, 255)
YELLOW = (255, 215, 40)
ORANGE = (245, 150, 30)

random.seed(4)

# Generate a smooth hilly track
points = []
step = 45
for i in range(220):
    x = i * step
    y = 470 + 75 * math.sin(i * 0.38) + 35 * math.sin(i * 0.91)
    if i < 4:
        y = 470
    points.append((x, y))

def terrain_y(x):
    if x <= points[0][0]:
        return points[0][1]
    i = int(x // step)
    i = max(0, min(i, len(points) - 2))
    x1, y1 = points[i]
    x2, y2 = points[i + 1]
    t = (x - x1) / (x2 - x1)
    return y1 + (y2 - y1) * t

def terrain_slope(x):
    d = 2
    return (terrain_y(x + d) - terrain_y(x - d)) / (2 * d)

# Coins placed above the track
coins = []
for i in range(8, 210, 9):
    x = i * step + random.randint(-10, 10)
    y = terrain_y(x) - random.randint(65, 105)
    coins.append([x, y, True])

# Fuel cans
fuel_cans = []
for i in range(30, 210, 35):
    x = i * step
    fuel_cans.append([x, terrain_y(x) - 55, True])

# Car state
car_x = 180.0
car_y = terrain_y(car_x) - 55
vx = 0.0
vy = 0.0
angle = 0.0
angular_velocity = 0.0
fuel = 100.0
score = 0
best_distance = 0
game_over = False

wheel_base = 82
wheel_radius = 17

def reset():
    global car_x, car_y, vx, vy, angle, angular_velocity, fuel, score, game_over
    car_x = 180.0
    car_y = terrain_y(car_x) - 55
    vx = 0.0
    vy = 0.0
    angle = 0.0
    angular_velocity = 0.0
    fuel = 100.0
    score = 0
    game_over = False
    for c in coins:
        c[2] = True
    for f in fuel_cans:
        f[2] = True

def draw_text(text, x, y, size=28):
    font = pygame.font.Font(None, size)
    screen.blit(font.render(text, True, WHITE), (x, y))

def rotate_point(px, py, cx, cy, a):
    ca, sa = math.cos(a), math.sin(a)
    return (cx + px * ca - py * sa, cy + px * sa + py * ca)

def draw_car(camera_x):
    cx = car_x - camera_x
    cy = car_y

    # Car body
    body = [
        (-55, -25), (-35, -45), (20, -45),
        (50, -25), (55, 0), (-55, 0)
    ]
    body_pts = [rotate_point(x, y, cx, cy, angle) for x, y in body]
    pygame.draw.polygon(screen, CAR_RED, body_pts)

    # Windows
    window = [(-25, -41), (12, -41), (29, -26), (-30, -26)]
    win_pts = [rotate_point(x, y, cx, cy, angle) for x, y in window]
    pygame.draw.polygon(screen, (80, 170, 210), win_pts)

    # Wheels
    for wx in (-wheel_base / 2, wheel_base / 2):
        p = rotate_point(wx, 8, cx, cy, angle)
        pygame.draw.circle(screen, WHEEL, (int(p[0]), int(p[1])), wheel_radius)
        pygame.draw.circle(screen, (100, 100, 100), (int(p[0]), int(p[1])), 7)

def draw_terrain(camera_x):
    visible = []
    for x, y in points:
        sx = x - camera_x
        if -100 <= sx <= WIDTH + 100:
            visible.append((int(sx), int(y)))
    if visible:
        poly = visible + [(WIDTH + 100, HEIGHT), (-100, HEIGHT)]
        pygame.draw.polygon(screen, GROUND, poly)
        pygame.draw.lines(screen, GROUND_DARK, False, visible, 7)

def draw_coin(x, y, camera_x):
    sx = int(x - camera_x)
    if -30 < sx < WIDTH + 30:
        pygame.draw.circle(screen, YELLOW, (sx, int(y)), 13)
        pygame.draw.circle(screen, ORANGE, (sx, int(y)), 8, 3)

def draw_fuel(x, y, camera_x):
    sx = int(x - camera_x)
    if -30 < sx < WIDTH + 30:
        pygame.draw.rect(screen, (220, 45, 45), (sx - 11, int(y) - 16, 22, 30), border_radius=4)
        pygame.draw.rect(screen, WHITE, (sx - 4, int(y) - 8, 8, 14))

running = True
while running:
    dt = min(clock.tick(60) / 1000.0, 0.03)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset()

    keys = pygame.key.get_pressed()

    if not game_over:
        # Engine
        throttle = 0
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            throttle += 1
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            throttle -= 1

        fuel -= (0.8 + abs(throttle) * 1.5) * dt
        if fuel <= 0:
            fuel = 0
            game_over = True

        # Gravity
        vy += 1000 * dt

        # Driving force
        vx += throttle * 520 * dt

        # Air resistance
        vx *= 0.995

        # Limit speed
        vx = max(-250, min(vx, 650))

        car_x += vx * dt
        car_y += vy * dt

        # Terrain collision using both wheels
        front_x = car_x + math.cos(angle) * wheel_base / 2
        back_x = car_x - math.cos(angle) * wheel_base / 2
        front_ground = terrain_y(front_x) - wheel_radius
        back_ground = terrain_y(back_x) - wheel_radius
        ground_y = min(front_ground, back_ground)

        if car_y > ground_y - 5:
            car_y = ground_y - 5
            if vy > 0:
                vy *= -0.12

            # Align car somewhat with the hill
            slope = terrain_slope(car_x)
            target_angle = math.atan2(slope, 1)
            angle_diff = (target_angle - angle + math.pi) % (2 * math.pi) - math.pi
            angle += angle_diff * min(8 * dt, 1)

            # Friction
            vx *= 0.985

        else:
            # Air control
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                angular_velocity += 2.0 * dt
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                angular_velocity -= 2.0 * dt
            angular_velocity *= 0.995
            angle += angular_velocity

        # Keep the car from reversing too far
        car_x = max(80, car_x)

        # Collect coins
        for c in coins:
            if c[2] and math.hypot(car_x - c[0], car_y - c[1]) < 55:
                c[2] = False
                score += 10

        # Collect fuel
        for f in fuel_cans:
            if f[2] and math.hypot(car_x - f[0], car_y - f[1]) < 55:
                f[2] = False
                fuel = min(100, fuel + 35)

        # Crash if upside down
        if abs((angle + math.pi) % (2 * math.pi) - math.pi) > 2.2:
            game_over = True

        best_distance = max(best_distance, int(car_x / 10))

    # Camera
    camera_x = max(0, car_x - 300)

    # Sky
    screen.fill(SKY)

    # Simple clouds
    for cloud_x, cloud_y in [(180, 100), (650, 140), (980, 80)]:
        cx = int(cloud_x - (camera_x * 0.15) % 1200)
        pygame.draw.circle(screen, WHITE, (cx, cloud_y), 25)
        pygame.draw.circle(screen, WHITE, (cx + 28, cloud_y + 5), 30)
        pygame.draw.circle(screen, WHITE, (cx + 55, cloud_y), 22)

    draw_terrain(camera_x)

    for c in coins:
        if c[2]:
            draw_coin(c[0], c[1], camera_x)

    for f in fuel_cans:
        if f[2]:
            draw_fuel(f[0], f[1], camera_x)

    draw_car(camera_x)

    # HUD
    draw_text(f"Distance: {int(car_x / 10)} m", 20, 20)
    draw_text(f"Coins: {score}", 20, 55)
    draw_text("Fuel", 20, 90)

    pygame.draw.rect(screen, (70, 70, 70), (85, 95, 220, 22), border_radius=5)
    pygame.draw.rect(screen, (50, 210, 70), (85, 95, int(220 * fuel / 100), 22), border_radius=5)

    draw_text("←/A og →/D = kjør   R = restart", 20, HEIGHT - 45, 24)

    if game_over:
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 120))
        screen.blit(overlay, (0, 0))
        draw_text("GAME OVER", WIDTH // 2 - 100, HEIGHT // 2 - 50, 60)
        draw_text("Trykk R for å starte på nytt", WIDTH // 2 - 155, HEIGHT // 2 + 20, 30)

    pygame.display.flip()

pygame.quit()
