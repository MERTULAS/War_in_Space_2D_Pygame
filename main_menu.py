import pygame
from TheGame import TheGame
from random import randint
from time import time
from fonts import Fonts

pygame.init()
WIDTH = 800
HEIGHT = 600

font = Fonts(WIDTH, HEIGHT)

pygame.display.set_caption("War In Space 2D")
icon = pygame.image.load("data\\warinspaceicon.png")
pygame.display.set_icon(icon)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
run_game = True


def background_stars(stars_list):
    for star in stars_list:
        background_stars_list.append([[star[0], star[1]], [randint(0, 10) - 5, randint(0, 10) - 5],
                                     randint(1, 2)])
        for particle in background_stars_list:
            a = particle[0][0]
            b = particle[0][1]
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= 1
            pygame.draw.circle(screen, (255, 255, 255), [int(particle[0][0]), int(particle[0][1])],
                               int(particle[2]))
            pygame.draw.line(screen, (255, 255, 255), [int(a), int(b)], [int(particle[0][0]), int(particle[0][1])], 1)
            if particle[2] <= 0:
                background_stars_list.remove(particle)


def falling_star(star_x, star_y, x_difference, y_difference):
    falling_star_list.append([[star_x, star_y], [randint(0, 10), randint(0, 2) - 1],
                             randint(4, 6)])
    for particle in falling_star_list:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.2
        pygame.draw.circle(screen, (220, 220, 255), [int(particle[0][0]), int(particle[0][1])],
                           int(particle[2]))
        if particle[2] <= 0:
            falling_star_list.remove(particle)
    star_x -= x_difference
    star_y += y_difference
    if star_x < -125:
        star_x = WIDTH + 50
        star_y = 400
        x_difference = 0
        y_difference = 0
    return star_x, star_y, x_difference, y_difference


stars = []
background_stars_list = []

falling_star_list = []
falling_star_loop_time = time()
falling_star_status = False
x_dif = 1
y_dif = [0.5, -0.8, 0.2, -0.6]
star_y_list_index = 0
y_dif_temp = y_dif[star_y_list_index]
star_x_axis, star_y_axis = WIDTH + 50, [HEIGHT // 4, HEIGHT - HEIGHT // 24, HEIGHT // 2, HEIGHT - HEIGHT // 3]
star_y_temp = star_y_axis[star_y_list_index]
while run_game:
    game = TheGame(WIDTH, HEIGHT)
    screen.fill((3, 3, 15))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False

    stars.append([randint(0, WIDTH), randint(0, HEIGHT)])
    background_stars(stars)
    if len(stars) > 100:
        stars.pop(len(stars) - 1)

    if time() >= falling_star_loop_time + 2:
        star_x_axis, star_y_temp, x_dif, y_dif_temp = falling_star(star_x_axis, star_y_temp, x_dif, y_dif_temp)
        if star_x_axis == WIDTH + 50:
            falling_star_loop_time = time()
            x_dif = 1
            star_y_list_index += 1
            if star_y_list_index == 4:
                star_y_list_index = 0
            star_y_temp = star_y_axis[star_y_list_index]
            y_dif_temp = y_dif[star_y_list_index]

    start_game_button = pygame.draw.rect(screen, (255, 0, 0), (WIDTH//2 - WIDTH//8, HEIGHT//3.5,
                                                               WIDTH//4, HEIGHT//10))
    settings_button = pygame.draw.rect(screen, (255, 0, 0), (WIDTH//2 - WIDTH//8, HEIGHT//3.5 + (11 * HEIGHT)//60,
                                                             WIDTH//4, HEIGHT//10))
    credits_button = pygame.draw.rect(screen, (255, 0, 0), (WIDTH//2 - WIDTH//8, HEIGHT//3.5 + (22 * HEIGHT)//60,
                                                            WIDTH//4, HEIGHT//10))
    quit_game_button = pygame.draw.rect(screen, (255, 0, 0), (WIDTH // 2 - WIDTH // 8,
                                                              HEIGHT // 3.5 + (33 * HEIGHT) // 60,
                                                              WIDTH // 4, HEIGHT // 10))
    header = font.start_header_font().render("WAR IN SPACE", True, (255, 0, 0))
    start_game = font.start_menu_font().render("START GAME", True, (25, 25, 25))
    settings = font.start_menu_font().render("SETTINGS", True, (25, 25, 25))
    credit = font.start_menu_font().render("CREDITS", True, (25, 25, 25))
    quit_game = font.start_menu_font().render("QUIT GAME", True, (25, 25, 25))

    x, y = pygame.mouse.get_pos()
    if WIDTH//2 - WIDTH//8 < x < WIDTH//2 + WIDTH//8 and HEIGHT//3.5 < y < HEIGHT//3.5 + HEIGHT//10:
        pygame.draw.rect(screen, (0, 255, 0), (WIDTH//2 - WIDTH//8, HEIGHT//3.5, WIDTH//4, HEIGHT//10))
        click = pygame.mouse.get_pressed()
        if click == (1, 0, 0):

            game.game(stars, background_stars_list, falling_star_list, star_y_list_index,
                      star_x_axis, star_y_temp, x_dif, y_dif_temp, falling_star_loop_time)

    if WIDTH//2 - WIDTH//8 < x < WIDTH//2 + WIDTH//8 and \
            HEIGHT//3.5 + (11 * HEIGHT)//60 < y < HEIGHT//3.5 + (11 * HEIGHT)//60 + HEIGHT//10:
        pygame.draw.rect(screen, (0, 255, 0), (WIDTH//2 - WIDTH//8, HEIGHT//3.5 + (11 * HEIGHT)//60,
                                               WIDTH//4, HEIGHT//10))
        click = pygame.mouse.get_pressed()
        if click == (1, 0, 0):
            WIDTH, HEIGHT, stars, star_x_axis, star_y_axis = game.settings(stars, background_stars_list,
                                                                           falling_star_list, star_y_list_index,
                                                                           star_x_axis, star_y_temp, x_dif, y_dif_temp)
            font = Fonts(WIDTH, HEIGHT)

    if WIDTH//2 - WIDTH//8 < x < WIDTH//2 + WIDTH//8 and \
            HEIGHT//3.5 + (22 * HEIGHT)//60 < y < HEIGHT//3.5 + (22 * HEIGHT)//60 + HEIGHT//10:
        pygame.draw.rect(screen, (0, 255, 0), (WIDTH//2 - WIDTH//8, HEIGHT//3.5 + (22 * HEIGHT)//60,
                                               WIDTH//4, HEIGHT//10))
        click = pygame.mouse.get_pressed()
        if click == (1, 0, 0):

            game.credits(stars, background_stars_list, falling_star_list, star_y_list_index,
                         star_x_axis, star_y_temp, x_dif, y_dif_temp)

    if WIDTH//2 - WIDTH//8 < x < WIDTH//2 + WIDTH//8 and \
            HEIGHT // 3.5 + (33 * HEIGHT) // 60 < y < HEIGHT // 3.5 + (33 * HEIGHT) // 60 + HEIGHT // 10:
        pygame.draw.rect(screen, (0, 255, 0), (WIDTH // 2 - WIDTH // 8, HEIGHT // 3.5 + (33 * HEIGHT) // 60,
                                               WIDTH // 4, HEIGHT // 10))
        click = pygame.mouse.get_pressed()
        if click == (1, 0, 0):

            quit_game()

    screen.blit(header, (WIDTH // 2 - HEIGHT // 2, WIDTH // 10))
    screen.blit(start_game, (WIDTH // 2 - WIDTH // 10, HEIGHT // 3.15))
    screen.blit(settings, (WIDTH // 2 - WIDTH // 12.5, HEIGHT // 2))
    screen.blit(credit, (WIDTH // 2 - WIDTH // 14, HEIGHT // 1.46))
    screen.blit(quit_game, (WIDTH // 2 - WIDTH // 11.5, HEIGHT // 1.15))
    pygame.display.update()
