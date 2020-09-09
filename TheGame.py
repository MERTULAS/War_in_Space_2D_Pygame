import pygame
from random import randint
from time import time
from math import sqrt

fire_status_player = "ready"
particle_status = "ready"


class TheGame:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def game(self, stars, background_stars_list, falling_star_list, star_y_list_index, star_x_axis,
             star_y_temp, x_dif, y_dif_temp, falling_star_loop_time):
        font_fight_panel = pygame.font.Font("data\\skyridgesuperital.ttf", self.height // 25)
        font_score_panel = pygame.font.Font("data\\skyridgesuperital.ttf", self.height // 35)

        class Player:
            def __init__(self, vehicle_img, x_axis, y_axis, hit, health_pos_y, x_y_changer):
                self.vehicle_img = vehicle_img
                self.x_axis = x_axis
                self.y_axis = y_axis
                self.health = 100 - hit
                self.health_bar_pos_y_axis = health_pos_y
                self.x_y_changer = x_y_changer

            def blit_to_screen(self, screen_):
                screen_.blit(self.vehicle_img, (self.x_axis, self.y_axis))
                pygame.draw.rect(screen, (255, 0, 0), (self.x_axis - 20, self.health_bar_pos_y_axis + 70, 100, 15))
                pygame.draw.rect(screen, (0, 255, 0), (self.x_axis - 20, self.health_bar_pos_y_axis + 70,
                                                       self.health, 15))

            def left(self):
                self.x_axis -= self.x_y_changer
                if self.x_axis < 0:
                    self.x_axis = 0
                return self.x_axis

            def right(self, WIDTH):
                self.x_axis += self.x_y_changer
                if self.x_axis > WIDTH - 64:
                    self.x_axis = WIDTH - 64
                return self.x_axis

            def up(self, HEIGHT):
                self.y_axis -= self.x_y_changer
                if self.y_axis < HEIGHT // 3:
                    self.y_axis = HEIGHT // 3
                return self.y_axis

            def down(self, HEIGHT):
                self.y_axis += self.x_y_changer
                if self.y_axis > HEIGHT - HEIGHT // 24 - 94:
                    self.y_axis = HEIGHT - HEIGHT // 24 - 94
                return self.y_axis

        class Enemy(Player):
            def __init__(self, vehicle_img, x_axis, y_axis, hit, health_pos_y, x_y_changer):
                super().__init__(vehicle_img, x_axis, y_axis, hit, health_pos_y, x_y_changer)

            def boundaries(self, right_boundary, left_boundary, x_changer, width):
                self.x_axis += x_changer
                if self.x_axis > right_boundary:
                    x_changer *= -1
                    left_boundary = randint(0, 350)
                if self.x_axis < left_boundary:
                    x_changer *= -1
                    right_boundary = randint(450, width - 64)
                return right_boundary, left_boundary, x_changer, self.x_axis

        class PlayerBullet:
            def __init__(self, bullet_img, x_axis, y_axis, bullet_speed):
                self.bullet_img = bullet_img
                self.x_axis = x_axis
                self.y_axis = y_axis
                self.bullet_speed = bullet_speed

            def is_fire_ready(self):
                x_list = []
                y_list = []
                x_list.append(self.x_axis)
                if len(x_list) > 2:
                    x_list.pop(1)
                y_list.append(self.y_axis)
                if len(y_list) > 2:
                    y_list.pop(1)
                global fire_status_player
                fire_status_player = "wait"
                return x_list[0], y_list[0]

            def fire(self, bulletX, bulletY):
                self.x_axis, self.y_axis = bulletX, bulletY
                global fire_status_player
                if fire_status_player is "wait":
                    self.y_axis -= self.bullet_speed
                    screen.blit(self.bullet_img, (self.x_axis - 2, self.y_axis))
                    screen.blit(self.bullet_img, (self.x_axis + 36, self.y_axis))
                return self.y_axis

        class EnemyBullet(PlayerBullet):
            def __init__(self, bullet_img, x_axis, y_axis, bullet_speed):
                super().__init__(bullet_img, x_axis, y_axis, bullet_speed)

            def is_enemy_fire_ready(self):
                x_list = []
                y_list = []
                x_list.append(self.x_axis)
                if len(x_list) > 2:
                    x_list.pop(1)
                y_list.append(self.y_axis)
                if len(y_list) > 2:
                    y_list.pop(1)
                global fire_status_enemy
                fire_status_enemy = "wait"
                return x_list[0], y_list[0]

            def enemy_fire(self, bulletX, bulletY):
                self.x_axis, self.y_axis = bulletX, bulletY
                global fire_status_enemy
                if fire_status_enemy is "wait":
                    self.y_axis += self.bullet_speed
                    screen.blit(self.bullet_img, (self.x_axis - 2, self.y_axis))
                    screen.blit(self.bullet_img, (self.x_axis + 36, self.y_axis))
                return self.y_axis

        class Particle:
            def __init__(self, particle_img1, particle_img2, particle_img3, particle_x_axis, particle_y_axis):
                self.particle_img1 = particle_img1
                self.particle_img2 = particle_img2
                self.particle_img3 = particle_img3
                self.particle_x_axis = particle_x_axis
                self.particle_y_axis = particle_y_axis

            def blit_particle_group(self, particle_list, partic_x_changer, partic_y_changer):

                particle_list.append([[self.particle_x_axis, self.particle_y_axis],
                                     [randint(0, 20) / 10 - 1, randint(0, 20) / 10 - 1], randint(4, 6)])
                for particle in particle_list:
                    particle[0][0] += particle[1][0]
                    particle[0][1] += particle[1][1]
                    particle[2] -= 0.1
                    if -0.2 < particle[1][0] < 0.2:
                        screen.blit(self.particle_img1, (int(particle[0][0]), int(particle[0][1])))
                    elif -0.6 < particle[1][0] < 0.6:
                        screen.blit(self.particle_img2, (int(particle[0][0]), int(particle[0][1])))
                    elif -1 < particle[1][0] < 1:
                        screen.blit(self.particle_img3, (int(particle[0][0]), int(particle[0][1])))
                    if particle[2] <= 0:
                        particle_list.remove(particle)
                    self.particle_x_axis += partic_x_changer
                    self.particle_y_axis += partic_y_changer
                return particle_list, self.particle_x_axis, self.particle_y_axis, partic_x_changer, partic_y_changer

            def fire(self):
                x_list = []
                y_list = []
                x_list.append(self.particle_x_axis)
                if len(x_list) > 2:
                    x_list.pop(1)
                y_list.append(self.particle_y_axis)
                if len(y_list) > 2:
                    y_list.pop(1)
                global particle_status
                particle_status = "wait"
                return x_list[0], y_list[0]

            def particles_go_to_the_enemy(self, partic_y_changer):
                global particle_status
                if particle_status is "wait":
                    particles.append([[self.particle_x_axis, self.particle_y_axis],
                                     [randint(0, 20) / 10 - 1, randint(0, 20) / 10 - 1], randint(4, 6)])
                    for particle in particles:
                        particle[0][0] += particle[1][0]
                        particle[0][1] += particle[1][1]
                        particle[2] -= 0.1
                        if -0.2 < particle[1][0] < 0.2:
                            screen.blit(self.particle_img1, (int(particle[0][0]), int(particle[0][1])))
                        elif -0.6 < particle[1][0] < 0.6:
                            screen.blit(self.particle_img2, (int(particle[0][0]), int(particle[0][1])))
                        elif -1 < particle[1][0] < 1:
                            screen.blit(self.particle_img3, (int(particle[0][0]), int(particle[0][1])))
                        if particle[2] <= 0:
                            particles.remove(particle)
                    self.particle_y_axis += partic_y_changer
                return self.particle_y_axis

        def game_rectangles_and_bars(WIDTH, HEIGHT, PLASMA_BAR_FILLER, PLASMA_BAR_COLOR):
            pygame.draw.polygon(screen, (200, 0, 0), ((WIDTH // 2 - WIDTH // 3, HEIGHT // 11),
                                                      (WIDTH // 2 - WIDTH // 2.5, 0),
                                                      (WIDTH // 2 + WIDTH // 2.5, 0),
                                                      (WIDTH // 2 + WIDTH // 3, HEIGHT // 11)))
            pygame.draw.polygon(screen, (200, 0, 0), ((0, HEIGHT),
                                                      (WIDTH // 24, HEIGHT - HEIGHT // 24),
                                                      (WIDTH // 6, HEIGHT - HEIGHT // 24),
                                                      (WIDTH // 6 - WIDTH // 24, HEIGHT)))
            pygame.draw.polygon(screen, (0, 255, 0), ((0, HEIGHT),
                                                      (WIDTH // 24, HEIGHT - HEIGHT // 24),
                                                      (WIDTH // 24 + PLASMA_BAR_FILLER, HEIGHT - HEIGHT // 24),
                                                      (PLASMA_BAR_FILLER, HEIGHT)))
            pygame.draw.polygon(screen, (0, 0, 255), ((0, HEIGHT),
                                                      (WIDTH // 24, HEIGHT - HEIGHT // 24),
                                                      (WIDTH // 6, HEIGHT - HEIGHT // 24),
                                                      (WIDTH // 6 - WIDTH // 24, HEIGHT)), 3)
            pygame.draw.polygon(screen, PLASMA_BAR_COLOR, ((WIDTH // 6.66, HEIGHT),
                                                           (WIDTH // 5.21, HEIGHT - HEIGHT // 24),
                                                           (WIDTH // 2.08, HEIGHT - HEIGHT // 24),
                                                           (WIDTH // 2.28, HEIGHT)))

        def game_play_fonts(WIDTH, HEIGHT, PLAYER_SCORE, ENEMY_SCORE):

            fight = font_fight_panel.render("FIGHT!", True, (20, 20, 20))
            player_text = font_score_panel.render("PLAYER:", True, (20, 20, 20))
            player_scr = font_score_panel.render(str(PLAYER_SCORE), True, (20, 20, 20))
            enemy_text = font_score_panel.render(":ENEMY", True, (20, 20, 20))
            enemy_scr = font_score_panel.render(str(ENEMY_SCORE), True, (20, 20, 20))
            plasma_sig = font_score_panel.render("PLASMA BEAM", True, (20, 20, 20))
            screen.blit(fight, (WIDTH // 2 - WIDTH // 20, HEIGHT // 60))
            screen.blit(player_text, (WIDTH // 2 - WIDTH // 20 - WIDTH // 5, HEIGHT // 60))
            screen.blit(enemy_text, (WIDTH // 2 + WIDTH // 20 + WIDTH // 10, HEIGHT // 60))
            screen.blit(player_scr, (WIDTH // 2 - WIDTH // 20 - WIDTH // 7, HEIGHT // 20))
            screen.blit(enemy_scr, (WIDTH // 2 + WIDTH // 20 + WIDTH // 7, HEIGHT // 20))
            screen.blit(plasma_sig, (WIDTH // 5.21, HEIGHT - HEIGHT // 30))

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
                    pygame.draw.line(screen, (255, 255, 255), [int(a), int(b)],
                                     [int(particle[0][0]), int(particle[0][1])], 1)
                    if particle[2] <= 0:
                        background_stars_list.remove(particle)

        def falling_star(star_x, star_y, x_difference, y_difference, WIDTH):
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

        def collision(bullet_x_axis, bullet_y_axis, vehicle_x_axis, vehicle_y_axis):
            cols = sqrt((pow((bullet_x_axis - vehicle_x_axis - 16), 2)) +
                        (pow((bullet_y_axis - vehicle_y_axis), 2)))
            cols = int(cols)
            if cols < 64:
                return True
            else:
                return False

        def collision_particles(prtcls, cols_x, cols_y):
            prtcls.append([[cols_x, cols_y], [randint(0, 20) / 10 - 1, randint(0, 20) / 10 - 1],
                          randint(6, 10)])
            for particle in prtcls:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.09
                pygame.draw.circle(screen, (200, 200, 200), (int(particle[0][0]), int(particle[0][1])),
                                   int(particle[2]))
                if particle[2] <= 0:
                    prtcls.remove(particle)
            return prtcls

        screen = pygame.display.set_mode((self.width, self.height))

        player_img = pygame.image.load("data\\vehicle.png")
        player_x = self.width // 2
        player_y = (2 * self.height) // 3
        move_speed = self.width / 533
        score_player = 0
        hit_player = 0

        global fire_status_enemy
        fire_status_enemy = "ready"
        bullet_player_x = player_x
        bullet_player_y = player_y
        bullet_player_img = pygame.image.load("data\\bullet.png")

        enemy_img = pygame.image.load("data\\invaders_rev.png")
        enemy_x = self.width // 2
        enemy_y = self.height // 6
        enemy_x_changer = self.width / 800
        score_enemy = 0
        hit_enemy = 0
        enemy_x_up_limit = randint(450, self.width - 64)
        enemy_x_low_limit = randint(0, 350)
        bullet_enemy_img = pygame.image.load("data\\laser_beam.png")
        bullet_enemy_x = enemy_x
        bullet_enemy_y = enemy_y
        bullet_move_speed = self.width / 400
        plasma_blast_bar_filler = 0
        time_enemy_fire = time()
        time_laps = randint(0, 2)

        y_dif = [0.5, -0.8, 0.2, -0.6]
        star_y_axis = [self.height // 4, self.height - self.height // 24,
                       self.height // 2, self.height - self.height // 3]

        particleimg_1 = pygame.image.load("data\\fire_yellow.png")
        particleimg_2 = pygame.image.load("data\\fire.png")
        particleimg_3 = pygame.image.load("data\\white.png")
        particle_x = self.width // 80
        particle_y = self.height - self.height // 24
        particle_x_changer = 0
        particle_y_changer = 0
        plasma_sig_color = (200, 0, 0)
        particles = []
        truth = False
        is_on_the_player = False
        time_for_bar = time()

        enemy_collision_particle = False
        enemy_cols_particles = []
        enemy_collision_loop_time = time()
        player_collision_particle = False
        player_cols_particles = []
        player_collision_loop_time = time()
        run_game = True
        while run_game:

            screen.fill((3, 3, 15))
            player = Player(player_img, player_x, player_y, hit_player, player_y, move_speed)
            enemy = Enemy(enemy_img, enemy_x, enemy_y, hit_enemy, enemy_y - 90, move_speed)
            player_bullet = PlayerBullet(bullet_player_img, player_x, player_y, bullet_move_speed)
            enemy_bullet = EnemyBullet(bullet_enemy_img, enemy_x, enemy_y, bullet_move_speed)
            plasma_beam = Particle(particleimg_1, particleimg_2, particleimg_3, particle_x, particle_y)

            game_rectangles_and_bars(self.width, self.height, plasma_blast_bar_filler, plasma_sig_color)
            game_play_fonts(self.width, self.height, score_player, score_enemy)

            background_stars(stars)
            if len(stars) > 100:
                stars.pop(len(stars) - 1)

            if time() >= falling_star_loop_time + 2:
                star_x_axis, star_y_temp, x_dif, y_dif_temp = falling_star(star_x_axis, star_y_temp,
                                                                           x_dif, y_dif_temp, self.width)
                if star_x_axis == self.width + 50:
                    falling_star_loop_time = time()
                    x_dif = 1
                    star_y_list_index += 1
                    if star_y_list_index == 4:
                        star_y_list_index = 0
                    star_y_temp = star_y_axis[star_y_list_index]
                    y_dif_temp = y_dif[star_y_list_index]

            particles, particle_x, particle_y, particle_x_changer, particle_y_changer = plasma_beam.blit_particle_group(
                particles, particle_x_changer, particle_y_changer)

            if time() > time_for_bar + 0.5 and plasma_blast_bar_filler < 31 * self.width // 250 and not truth:
                particle_x_changer = self.width / 16000
                plasma_blast_bar_filler += self.width // 250
                time_for_bar = time()

            else:
                particle_x_changer = 0
                plasma_blast_bar_filler += 0

            if plasma_blast_bar_filler >= 31 * self.width // 250 and not truth:
                plasma_sig_color = (0, 255, 0)
                if particle_x != player_x and particle_y != player_y:
                    if particle_x < player_x + 16:
                        particle_x_changer = self.width / 8000
                    if particle_x > player_x + 16:
                        particle_x_changer = -self.width / 8000
                    if particle_y > player_y:
                        particle_y_changer = -self.width / 8000
                    if particle_y < player_y:
                        particle_y_changer = self.width / 8000
                    if particle_x == player_x + 16:
                        particle_x_changer = 0
                    if particle_y == player_y:
                        particle_y_changer = 0
                    if particle_x_changer == 0 and particle_y_changer == 0:
                        particle_x = player_x + 16
                        particle_y = player_y

                if player_x - 10 < particle_x < player_x + 10:
                    is_on_the_player = True

            if hit_enemy > 100:
                hit_enemy = 0
                score_player += 1
            if hit_player > 100:
                hit_player = 0
                score_enemy += 1

            global event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run_game = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    player_x = player.right(WIDTH=self.width)
                if event.key == pygame.K_a:
                    player_x = player.left()
                if event.key == pygame.K_w:
                    player_y = player.up(HEIGHT=self.height)
                if event.key == pygame.K_s:
                    player_y = player.down(HEIGHT=self.height)
                if event.key == pygame.K_SPACE:
                    if plasma_blast_bar_filler >= 31 * self.width // 250 and is_on_the_player:
                        global particle_status
                        if particle_status is "ready":
                            particle_x, particle_y = plasma_beam.fire()
                            truth = True
                            plasma_blast_bar_filler = 0
                    if plasma_blast_bar_filler != 0 and not truth:
                        global fire_status_player
                        if fire_status_player is "ready":
                            bullet_player_x, bullet_player_y = player_bullet.is_fire_ready()

            enemy_x_up_limit, enemy_x_low_limit, enemy_x_changer, enemy_x = enemy.boundaries(enemy_x_up_limit,
                                                                                             enemy_x_low_limit,
                                                                                             enemy_x_changer,
                                                                                             self.width)
            bullet_player_y = player_bullet.fire(bullet_player_x, bullet_player_y)
            collision_enemy = collision(bullet_player_x, bullet_player_y, enemy_x, enemy_y)
            if collision_enemy:
                hit_enemy += 10
                enemy_collision_particle = True

            if not enemy_collision_particle:
                enemy_collision_loop_time = time()
                enemy_cols_particles = []
            if enemy_collision_particle:
                enemy_cols_particles = collision_particles(enemy_cols_particles, enemy_x + 32, enemy_y + 32)
            if time() > enemy_collision_loop_time + 0.25:
                enemy_collision_loop_time = time()
                enemy_collision_particle = False
            if bullet_player_y < 0 or collision_enemy:
                bullet_player_x, bullet_player_y = player_x, player_y
                fire_status_player = "ready"

            if time() >= time_enemy_fire + time_laps:
                time_enemy_fire = time()
                time_laps = randint(0, 2)
                if fire_status_enemy is "ready":
                    bullet_enemy_x, bullet_enemy_y = enemy_bullet.is_enemy_fire_ready()
            bullet_enemy_y = enemy_bullet.enemy_fire(bullet_enemy_x, bullet_enemy_y)
            collision_player = collision(bullet_enemy_x, bullet_enemy_y, player_x, player_y)
            if collision_player:
                hit_player += 10
                player_collision_particle = True
            if not player_collision_particle:
                player_collision_loop_time = time()
                player_cols_particles = []
            if player_collision_particle:
                player_cols_particles = collision_particles(player_cols_particles, player_x + 32, player_y + 32)
                if time() > player_collision_loop_time + 0.25:
                    player_collision_loop_time = time()
                    player_collision_particle = False
            if bullet_enemy_y > self.height or collision_player:
                bullet_enemy_x, bullet_enemy_y = enemy_x, enemy_y
                fire_status_enemy = "ready"

            if truth:
                particle_y_changer = -self.width / 8000
                particle_y = plasma_beam.particles_go_to_the_enemy(self.width / 8000)
            collision_plasma_beam = collision(particle_x, particle_y, enemy_x, enemy_y)
            if collision_plasma_beam:
                hit_enemy += 50
            if particle_y < 0 or collision_plasma_beam:
                particle_x, particle_y = self.width // 80, self.height - self.height // 24
                particle_status = "ready"
                plasma_blast_bar_filler = 0
                plasma_sig_color = (200, 0, 0)
                particle_y_changer = 0
                truth = False
                is_on_the_player = False
            player.blit_to_screen(screen)
            enemy.blit_to_screen(screen)
            pygame.display.update()

    def settings(self, stars, background_stars_list, falling_star_list, star_y_list_index, star_x_axis,
                 star_y_temp, x_dif, y_dif_temp):

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
                    pygame.draw.line(screen, (255, 255, 255), [int(a), int(b)],
                                     [int(particle[0][0]), int(particle[0][1])], 1)
                    if particle[2] <= 0:
                        background_stars_list.remove(particle)

        def falling_star(star_x_axs, star_y, x_difference, y_difference, WIDTH):
            falling_star_list.append([[star_x_axs, star_y], [randint(0, 10), randint(0, 2) - 1],
                                      randint(4, 6)])
            for particle in falling_star_list:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.2
                pygame.draw.circle(screen, (220, 220, 255), [int(particle[0][0]), int(particle[0][1])],
                                   int(particle[2]))
                if particle[2] <= 0:
                    falling_star_list.remove(particle)
            star_x_axs -= x_difference
            star_y += y_difference
            if star_x_axs < -125:
                star_x_axs = WIDTH + 50
                star_y = 400
                x_difference = 0
                y_difference = 0
            return star_x_axs, star_y, x_difference, y_difference

        font_start_header = pygame.font.Font("data\\skyridgegradital.ttf", (self.width // 15))
        font_start_menu = pygame.font.Font("data\\skyridgesuperital.ttf", self.width // 46)
        screen = pygame.display.set_mode((self.width, self.height))

        y_dif = [0.5, -0.8, 0.2, -0.6]
        star_y_axis = [self.height // 4, self.height - self.height // 24,
                       self.height // 2, self.height - self.height // 3]
        falling_star_loop_time = time()
        running = True
        while running:
            screen.fill((3, 3, 15))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            stars.append([randint(0, self.width), randint(0, self.height)])

            background_stars(stars)
            if len(stars) > 100:
                stars.pop(len(stars) - 1)

            if time() >= falling_star_loop_time + 2:
                star_x_axis, star_y_temp, x_dif, y_dif_temp = falling_star(star_x_axis, star_y_temp,
                                                                           x_dif, y_dif_temp, self.width)
                if star_x_axis == self.width + 50:
                    falling_star_loop_time = time()
                    x_dif = 1
                    star_y_list_index += 1
                    if star_y_list_index == 4:
                        star_y_list_index = 0
                    star_y_temp = star_y_axis[star_y_list_index]
                    y_dif_temp = y_dif[star_y_list_index]

            pygame.draw.rect(screen, (255, 0, 0), (self.width // 8, self.height // 3,
                                                   self.width // 4, self.height // 8))
            pygame.draw.rect(screen, (255, 0, 0), (self.width // 8, (2 * self.height) // 3,
                                                   self.width // 4, self.height // 8))
            pygame.draw.rect(screen, (255, 0, 0), (self.width // 2 + self.width // 8, self.height // 3,
                                                   self.width // 4, self.height // 8))
            pygame.draw.rect(screen, (255, 0, 0), (self.width // 2 + self.width // 8, (2 * self.height) // 3,
                                                   self.width // 4, self.height // 8))
            header = font_start_header.render("WAR IN SPACE", True, (255, 0, 0))
            setting1_text = font_start_menu.render("640x480", True, (25, 25, 25))
            setting2_text = font_start_menu.render("800x600", True, (25, 25, 25))
            setting3_text = font_start_menu.render("1024x768", True, (25, 25, 25))
            setting4_text = font_start_menu.render("1280x960", True, (25, 25, 25))
            x1, y1 = pygame.mouse.get_pos()
            if self.width // 8 < x1 < self.width // 8 + self.width // 4 and \
                    self.height // 3 < y1 < self.height // 3 + self.height // 8:
                pygame.draw.rect(screen, (0, 255, 0), (self.width // 8, self.height // 3,
                                                       self.width // 4, self.height // 8))
                click = pygame.mouse.get_pressed()
                if click == (1, 0, 0):
                    self.width, self.height = 640, 480
                    pygame.display.set_mode((self.width, self.height))
                    star_x_axis, star_y_axis = self.width + 50, [self.height // 4, self.height - self.height // 24,
                                                                 self.height // 2, self.height - self.height // 3]
                    background_list = []
                    return self.width, self.height, background_list, star_x_axis, star_y_axis
            if self.width // 8 < x1 < self.width // 8 + self.width // 4 and \
                    (2 * self.height) // 3 < y1 < (2 * self.height) // 3 + self.height // 8:
                pygame.draw.rect(screen, (0, 255, 0), (self.width // 8, (2 * self.height) // 3,
                                                       self.width // 4, self.height // 8))
                click = pygame.mouse.get_pressed()
                if click == (1, 0, 0):
                    self.width, self.height = 1024, 768
                    pygame.display.set_mode((self.width, self.height))
                    star_x_axis, star_y_axis = self.width + 50, [self.height // 4, self.height - self.height // 24,
                                                                 self.height // 2, self.height - self.height // 3]
                    background_list = []
                    return self.width, self.height, background_list, star_x_axis, star_y_axis
            if self.width // 2 + self.width // 8 < x1 < self.width // 2 + self.width // 8 + self.width // 4 and \
                    self.height // 3 < y1 < self.height // 3 + self.height // 8:
                pygame.draw.rect(screen, (0, 255, 0), (self.width // 2 + self.width // 8, self.height // 3,
                                                       self.width // 4, self.height // 8))
                click = pygame.mouse.get_pressed()
                if click == (1, 0, 0):
                    self.width, self.height = 800, 600
                    pygame.display.set_mode((self.width, self.height))
                    star_x_axis, star_y_axis = self.width + 50, [self.height // 4, self.height - self.height // 24,
                                                                 self.height // 2, self.height - self.height // 3]
                    background_list = []
                    return self.width, self.height, background_list, star_x_axis, star_y_axis
            if self.width // 2 + self.width // 8 < x1 < self.width // 2 + self.width // 8 + self.width // 4 and \
                    (2 * self.height) // 3 < y1 < (2 * self.height) // 3 + self.height // 8:
                pygame.draw.rect(screen, (0, 255, 0), (self.width // 2 + self.width // 8, (2 * self.height) // 3,
                                                       self.width // 4, self.height // 8))
                click = pygame.mouse.get_pressed()
                if click == (1, 0, 0):
                    self.width, self.height = 1280, 960
                    pygame.display.set_mode((self.width, self.height))
                    star_x_axis, star_y_axis = self.width + 50, [self.height // 4, self.height - self.height // 24,
                                                                 self.height // 2, self.height - self.height // 3]
                    background_list = []
                    return self.width, self.height, background_list, star_x_axis, star_y_axis
            screen.blit(header, (self.width // 2 - self.height // 2, self.width // 10))
            screen.blit(setting1_text, (self.width // 4 - self.width // 15, self.height // 2.70))
            screen.blit(setting2_text, (self.width // 1.45, self.height // 2.70))
            screen.blit(setting3_text, (self.width // 4 - self.width // 14.5, self.height // 1.41))
            screen.blit(setting4_text, (self.width // 1.48, self.height // 1.41))
            pygame.display.update()

    def credits(self, stars, background_stars_list, falling_star_list, star_y_list_index, star_x_axis,
                star_y_temp, x_dif, y_dif_temp):
        font_start_menu = pygame.font.Font("data\\skyridgesuperital.ttf", self.width // 46)
        screen = pygame.display.set_mode((self.width, self.height))

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
                    pygame.draw.line(screen, (255, 255, 255), [int(a), int(b)],
                                     [int(particle[0][0]), int(particle[0][1])], 1)
                    if particle[2] <= 0:
                        background_stars_list.remove(particle)

        def falling_star(star_x_axs, star_y, x_difference, y_difference, WIDTH):
            falling_star_list.append([[star_x_axs, star_y], [randint(0, 10), randint(0, 2) - 1],
                                      randint(4, 6)])
            for particle in falling_star_list:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.2
                pygame.draw.circle(screen, (220, 220, 255), [int(particle[0][0]), int(particle[0][1])],
                                   int(particle[2]))
                if particle[2] <= 0:
                    falling_star_list.remove(particle)
            star_x_axs -= x_difference
            star_y += y_difference
            if star_x_axs < -125:
                star_x_axs = WIDTH + 50
                star_y = 400
                x_difference = 0
                y_difference = 0
            return star_x_axs, star_y, x_difference, y_difference

        y_dif = [0.5, -0.8, 0.2, -0.6]
        star_y_axis = [self.height // 4, self.height - self.height // 24,
                       self.height // 2, self.height - self.height // 3]
        falling_star_loop_time = time()
        credits_list_up = self.height
        running = True
        while running:
            screen.fill((3, 3, 15))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.draw.rect(screen, (255, 0, 0), (self.width // 1.17, self.height // 1.1,
                                                   self.width // 8, self.height // 15))
            back_text = font_start_menu.render("BACK", True, (25, 25, 25))

            designer = font_start_menu.render(" GAME DESIGNER", True, (255, 255, 255))
            mert_ulas = font_start_menu.render("MERT ULAS", True, (255, 255, 255))
            musics = font_start_menu.render("SOUND EFFECTS & MUSIC", True, (255, 255, 255))
            contacts = font_start_menu.render("CONTACT", True, (255, 255, 255))
            e_mail = font_start_menu.render("h.mert.ulas@gmail.com", True, (255, 255, 255))

            screen.blit(designer, (self.width // 2 - self.width // 7.25, credits_list_up))
            screen.blit(mert_ulas, (self.width // 2 - self.width // 11.5, credits_list_up + self.height // 12))
            screen.blit(musics, (self.width // 2 - self.width // 5, credits_list_up + self.height // 4))
            screen.blit(mert_ulas, (self.width // 2 - self.width // 11.5, credits_list_up + self.height // 3))
            screen.blit(contacts, (self.width // 2 - self.width // 13, credits_list_up + self.height // 2))
            screen.blit(e_mail, (self.width // 2 - self.width // 6, credits_list_up + (7 * self.height) // 12))

            credits_list_up -= self.height / 2000

            stars.append([randint(0, self.width), randint(0, self.height)])
            x, y = pygame.mouse.get_pos()
            if self.width // 1.17 < x < self.width // 1.17 + self.width // 8 and \
                    self.height // 1.1 < y < self.height // 1.1 + self.height // 15:
                pygame.draw.rect(screen, (0, 255, 0), (self.width // 1.17, self.height // 1.1,
                                                       self.width // 8, self.height // 15))
                click = pygame.mouse.get_pressed()
                if click == (1, 0, 0):
                    break

            background_stars(stars)
            if len(stars) > 100:
                stars.pop(len(stars) - 1)

            if time() >= falling_star_loop_time + 2:
                star_x_axis, star_y_temp, x_dif, y_dif_temp = falling_star(star_x_axis, star_y_temp,
                                                                           x_dif, y_dif_temp, self.width)
                if star_x_axis == self.width + 50:
                    falling_star_loop_time = time()
                    x_dif = 1
                    star_y_list_index += 1
                    if star_y_list_index == 4:
                        star_y_list_index = 0
                    star_y_temp = star_y_axis[star_y_list_index]
                    y_dif_temp = y_dif[star_y_list_index]

            screen.blit(back_text, (self.width // 1.14, self.height // 1.08))
            pygame.display.update()

    @staticmethod
    def quit_game():
        game_run = False
        return game_run
