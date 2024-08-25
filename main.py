import pygame
import random
import math
from pygame import mixer

# Initialize Pygame
pygame.init()

# add screen with resolution
screen = pygame.display.set_mode((800, 600))

# add name of the game
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("icons\ship.png")
space = pygame.image.load("icons\space.jpg")
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load("icons\ship.png")

playerImg = pygame.transform.scale(playerImg, (50, 50))

player_x = 368
player_y = 500
player_x_change = 0


# enemies
enemies = []
enemies_x = []
enemies_y = []
enemies_x_change = []
enemies_y_change = []
num_of_enemies = 8

for e in range(num_of_enemies):
    enemiesImg = pygame.image.load("icons\enemies.png")
    enemiesImgsize = pygame.transform.scale(enemiesImg, (50, 50))
    enemies.append(enemiesImgsize)
    enemies_x.append(random.randint(0, 750))
    enemies_y.append(random.randint(50, 200))
    enemies_x_change.append(0.5)
    enemies_y_change.append(50)

# add music
mixer.music.load("music/theme.mp3")
mixer.music.set_volume(0.3)
mixer.music.play(-1)

# shoot
shootImg = pygame.image.load("icons\shoot.png")
shootImg = pygame.transform.scale(shootImg, (15, 15))
shoot_x = 0
shoot_y = 500
shoot_x_change = 0
shoot_y_change = 3
shoot_visible = False

# points
points = 0
fonts = pygame.font.Font("freesansbold.ttf", 32)
fonts_x = 10
fonts_y = 10


def view_points(x, y):
    point = fonts.render(f"Points: {points}", True, (255, 255, 255))
    screen.blit(point, (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))


def draw_enemies(x, y, ene):
    screen.blit(enemies[ene], (x, y))


def shoot(x, y):
    global shoot_visible
    shoot_visible = True
    screen.blit(shootImg, (x + 16, y + 10))


def colision(x1, y1, x2, y2):
    distance = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
    if distance < 27:
        return True
    else:
        return False


execute = True

while execute:
    screen.blit(space, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            execute = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change -= 0.5
            if event.key == pygame.K_RIGHT:
                player_x_change += 0.5
            if event.key == pygame.K_SPACE:
                if not shoot_visible:
                    shoot_sound = mixer.Sound("sounds\shoot.mp3")
                    shoot_sound.play()
                    shoot_x = player_x
                    shoot(shoot_x, shoot_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    player_x += player_x_change

    if player_x <= 0:
        player_x = 0
    elif player_x >= 750:
        player_x = 750

    for e in range(num_of_enemies):
        # game over
        if enemies_y[e] > 460:
            for k in range(num_of_enemies):
                enemies_y[k] = 2000
            game_over_font = pygame.font.Font("freesansbold.ttf", 64)
            game_over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
            screen.blit(game_over_text, (200, 250))
            break

        enemies_x[e] += enemies_x_change[e]
        if enemies_x[e] <= 0:
            enemies_x_change[e] = 0.5
            enemies_y[e] += enemies_y_change[e]
        elif enemies_x[e] >= 750:
            enemies_x_change[e] = -0.5
            enemies_y[e] += enemies_y_change[e]
        exists_colision = colision(enemies_x[e], enemies_y[e], shoot_x, shoot_y)
        # colision
        if exists_colision:
            colision_sound = mixer.Sound("sounds\heat.mp3")
            colision_sound.play()
            shoot_y = 500
            shoot_visible = False
            enemies_x[e] = random.randint(0, 750)
            enemies_y[e] = random.randint(50, 200)
            points += 1
        draw_enemies(enemies_x[e], enemies_y[e], e)

    if shoot_y <= -15:
        shoot_y = 500
        shoot_visible = False
    if shoot_visible:
        shoot(shoot_x, shoot_y)
        shoot_y -= shoot_y_change

    player(player_x, player_y)

    view_points(fonts_x, fonts_y)

    pygame.display.update()
