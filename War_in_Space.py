import pygame
import random
import math
import time
from pygame import mixer

pygame.init()

pygame.display.set_caption("War In Space 2D")
icon = pygame.image.load("data\warinspaceicon.png")
pygame.display.set_icon(icon)


fire_status_player = "ready"
fire_status_enemy = "ready"
particle_status = "ready"

def the_game(event):

    class player_():
        def __init__(self, pImg, pX, pY, move_speed):
            self.pImg = pImg
            self.pX = pX
            self.pY = pY
            self.move_speed = move_speed

        def blit_to_screen(self, health):
            self.hit = health
            screen.blit(self.pImg, (self.pX, self.pY))
            pygame.draw.rect(screen, (255, 0, 0), (self.pX - 20, self.pY + 70, 100, 15))
            pygame.draw.rect(screen, (0, 255, 0), (self.pX - 20 + self.hit, self.pY + 70, 100 - self.hit, 15))

        def circles(self, circle, i):

            circle_particles_coordinates.append(
                [[circle[i][0], circle[i][1]], [random.randint(0, 20) / 10 - 1, random.randint(0, 20) / 10 - 1],
                 random.randint(4, 6)])

            for particle in circle_particles_coordinates:
                particle[0][0] -= particle[1][0]
                particle[0][1] -= particle[1][1]
                particle[2] -= 0.1
                if -0.2 < particle[1][0] < 0.2:
                    screen.blit(particleImg1, (int(particle[0][0]), int(particle[0][1])))
                elif -0.6 < particle[1][0] < 0.6:
                    screen.blit(particleImg2, (int(particle[0][0]), int(particle[0][1])))
                elif -1 < particle[1][0] < 1:
                    screen.blit(particleImg3, (int(particle[0][0]), int(particle[0][1])))
                if particle[2] <= 0:
                    circle_particles_coordinates.remove(particle)
                if len(circle_particles_coordinates) > 15:
                    circle_particles_coordinates.remove(particle)

            i += 1
            if len(circle) - 1 == i:
                i = 0
            return i

        def left(self):
            self.pX -= self.move_speed
            if self.pX < 0:
                self.pX = 0
            return self.pX

        def right(self):
            self.pX += self.move_speed
            if self.pX > WIDTH - 64:
                self.pX = WIDTH - 64
            return self.pX

        def up(self):
            self.pY -= self.move_speed
            if self.pY < HEIGHT // 3:
                self.pY = HEIGHT // 3
            return self.pY

        def down(self):
            self.pY += self.move_speed
            if self.pY > HEIGHT - HEIGHT//24 - 94:
                self.pY = HEIGHT - HEIGHT//24 - 94
            return self.pY

        def right_up(self):
            self.pX += self.move_speed
            self.pY -= self.move_speed
            if self.pX > WIDTH - 64:
                self.pX = WIDTH - 64
            if self.pY < HEIGHT // 3:
                self.pY = HEIGHT // 3
            return self.pX, self.pY

        def left_up(self):
            self.pX -= self.move_speed
            self.pY -= self.move_speed
            if self.pX < 0:
                self.pX = 0
            if self.pY < HEIGHT // 3:
                self.pY = HEIGHT // 3
            return self.pX, self.pY

        def right_down(self):
            self.pX += self.move_speed
            self.pY += self.move_speed
            if self.pX > WIDTH - 64:
                self.pX = WIDTH - 64
            if self.pY > HEIGHT - HEIGHT//24 - 94:
                self.pY = HEIGHT - HEIGHT//24 - 94
            return self.pX, self.pY

        def left_down(self):
            self.pX -= self.move_speed
            self.pY += self.move_speed
            if self.pX < 0:
                self.pX = 0
            if self.pY > HEIGHT - HEIGHT//24 - 94:
                self.pY = HEIGHT - HEIGHT//24 - 94
            return self.pX, self.pY


    class enemy_forces(player_):
        def __init__(self, pImg, pX, pY, move_speed):
            super().__init__(pImg, pX, pY, move_speed)

        def blit_to_screen_(self, health):
            self.hit = health
            screen.blit(self.pImg, (self.pX, self.pY))
            pygame.draw.rect(screen, (255, 0, 0), (self.pX - 20, self.pY - 25, 100, 15))
            pygame.draw.rect(screen, (0, 255, 0), (self.pX - 20 + self.hit, self.pY - 25, 100 - self.hit, 15))

        def enemy_initial_move(self, pX_changer, random_, random_up):
            self.pX += pX_changer
            if self.pX > WIDTH - 64:
                pX_changer = -self.move_speed
                random_ = random.randint(1, 350)
                random_up = random.randint(WIDTH//2 + 50, WIDTH - 64)
            if self.pX < random_:
                pX_changer = +self.move_speed
                random_up = random.randint(WIDTH//2 + 50, WIDTH - 64)
                if random_up % 60 != 0:
                    while True:
                        random_up = random.randint(WIDTH//2 + 50, WIDTH - 64)
                        if random_up % 60 == 0:
                            break
                # print(random_)
            if self.pX > random_up:
                pX_changer = -self.move_speed
                random_ = random.randint(1, WIDTH//2 - 50)
                if random_ % 60 != 0:
                    while True:
                        random_ = random.randint(1, WIDTH//2 - 50)
                        if random_ % 60 == 0:
                            break
                # print(random_up)
            return self.pX, pX_changer, random_, random_up


    class bullet_(player_):
        def __init__(self, bImg, b2Img, pX, pY, move_speed):
            super().__init__(self, pX, pY, move_speed)
            self.bImg = bImg
            self.b2Img = b2Img

        def fire(self):
            x_list = []
            y_list = []
            x_list.append(self.pX)
            if len(x_list) > 2:
                x_list.pop(1)
            y_list.append(self.pY)
            if len(y_list) > 2:
                y_list.pop(1)
            global fire_status_player
            fire_status_player = "wait"
            return x_list[0], y_list[0]

        def blit_to_screenn(self, bullet_X, bullet_Y):
            self.bX, self.bY = bullet_X, bullet_Y
            global fire_status_player
            if fire_status_player is "wait":
                self.bY -= self.move_speed
                screen.blit(self.bImg, (self.bX - 2, self.bY))
                screen.blit(self.b2Img, (self.bX + 36, self.bY))
            return self.bY

    class bullet_enemy_(player_):
        def __init__(self, bImg, b1Img, pX, pY, move_speed):
            super().__init__(self, pX, pY, move_speed)
            self.bImg = bImg
            self.b1Img = b1Img

        def fire(self):
            x_list = []
            y_list = []
            x_list.append(self.pX)
            if len(x_list) > 2:
                x_list.pop(1)
            y_list.append(self.pY)
            if len(y_list) > 2:
                y_list.pop(1)
            global fire_status_enemy
            fire_status_enemy = "wait"
            return x_list[0], y_list[0]

        def blit_to_screenn(self, bullet_X, bullet_Y):
            self.bX, self.bY = bullet_X, bullet_Y
            global fire_status_enemy
            if fire_status_enemy is "wait":
                self.bY += self.move_speed
                screen.blit(self.bImg, (self.bX - 2, self.bY))
                screen.blit(self.b1Img, (self.bX + 36, self.bY))
            return self.bY


    class particle_():
        def __init__(self, particle_img1, particle_img2, particle_img3, particle_x, particle_y):
            self.particle_img1 = particle_img1
            self.particle_img2 = particle_img2
            self.particle_img3 = particle_img3
            self.particle_x = particle_x
            self.particle_y = particle_y

        def blit_particle_group(self, particles, particleX_changer, particleY_changer):
            self.particles_coordinates = particles
            self.particles_coordinates.append([[self.particle_x, self.particle_y],
                                               [random.randint(0, 20) / 10 - 1,
                                                random.randint(0, 20) / 10 - 1],
                                                   random.randint(4, 6)])
            for particle in self.particles_coordinates:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.1
                if -0.2 < particle[1][0] < 0.2:
                    screen.blit(self.particle_img1, (int(particle[0][0]), int(particle[0][1])))
                elif -0.6 < particle[1][0] < 0.6:
                    screen.blit(self.particle_img2, (int(particle[0][0]), int(particle[0][1])))
                elif -1 < particle[1][0] < 1:
                    screen.blit(self.particle_img3, (int(particle[0][0]), int(particle[0][1])))
                if particle [2] <= 0:
                    self.particles_coordinates.remove(particle)
                self.particle_x += particleX_changer
                self.particle_y += particleY_changer
            return self.particles_coordinates, self.particle_x, self.particle_y, particleX_changer, particleY_changer

        def fire(self):
            x_list = []
            y_list = []
            x_list.append(self.particle_x)
            if len(x_list) > 2:
                x_list.pop(1)
            y_list.append(self.particle_y)
            if len(y_list) > 2:
                y_list.pop(1)
            global particle_status
            particle_status = "wait"
            return x_list[0], y_list[0]

        def particles_go_to_the_enemy(self, particleY_changer):
            global particle_status
            if particle_status is "wait":
                self.particles_coordinates = particles
                self.particles_coordinates.append([[self.particle_x, self.particle_y],
                                                   [random.randint(0, 20) / 10 - 1,
                                                    random.randint(0, 20) / 10 - 1],
                                                   random.randint(4, 6)])
                for particle in self.particles_coordinates:
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
                        self.particles_coordinates.remove(particle)
                self.particle_y += particleY_changer
            return self.particle_y

    def collission_particles(prtcl, colsx, colsy):
        prtcl.append([[colsx, colsy],[random.randint(0, 20) / 10 - 1, random.randint(0, 20) / 10 - 1], random.randint(6, 10)])
        for particle in prtcl:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= 0.09
            pygame.draw.circle(screen, (200, 200, 200), (int(particle[0][0]), int(particle[0][1])),
                               int(particle[2]))
            if particle[2] <= 0:
                prtcl.remove(particle)
        return prtcl

    def collission_with_the_enemy(bullet_x, bullet_y, enemy_x, enemy_y):
        cols = math.sqrt((math.pow((bullet_x - enemy_x - 16), 2)) + (math.pow((bullet_y - enemy_y), 2)))
        cols = int(cols)
        if cols < 64:
            return True
        else:
            return False

    def collission_with_the_player(bullet_x, bullet_y, player_x, player_y):
        cols = math.sqrt((math.pow((bullet_x - player_x - 16), 2)) + (math.pow((bullet_y - player_y), 2)))
        cols = int(cols)
        if cols < 64:
            return True
        else:
            return False

    def collission_for_plasma_beam(plasma_x, plasma_y, enemy_x, enemy_y):
        cols = math.sqrt((math.pow((plasma_x - enemy_x - 16), 2)) + (math.pow((plasma_y - enemy_y), 2)))
        cols = int(cols)
        if cols < 120:
            return True
        else:
            return False

    playerX = WIDTH // 2 - 32
    playerY = HEIGHT - HEIGHT//24 - 94
    health = 0
    playerImg = pygame.image.load("data\\vehicle.png")
    bulletImg = pygame.image.load("data\\bullet.png")
    bullet2Img = pygame.image.load("data\\bullet.png")
    enemyBulletImg = pygame.image.load("data\laser_beam.png")
    global p_bulletX
    global p_bulletY
    p_bulletX = playerX
    p_bulletY = playerY
    enemyX = WIDTH // 2 - 32
    enemyY = HEIGHT // 6
    global enemy_bulletX
    global enemy_bulletY
    enemy_bulletX = enemyX
    enemy_bulletY = enemyY
    enemyImg = pygame.image.load("data\invaders_rev.png")
    particleImg1 = pygame.image.load("data\\fire_yellow.png")
    particleImg2 = pygame.image.load("data\\fire.png")
    particleImg3 = pygame.image.load("data\white.png")
    enemy_col_x = 0
    enemy_col_y = 0
    random_ = 0
    random_up = WIDTH - 64
    hit = 0
    time_laps = random.randint(0, 2)
    time_ = time.time()
    time_for_bar = time.time()
    running = True
    player_score = 0
    enemy_score = 0
    particles = []
    cols_particles = []
    cols_list = []
    enemy_collission_particle = False
    player_collission_particle = False
    particleX = WIDTH // 80
    particleY = HEIGHT - HEIGHT//24
    particleX_changer = 0
    particleY_changer = 0
    plasma_blast_bar_filler = 0
    plasma_sig_color = (200, 0, 0)
    circle_particles_coordinates = []
    truth = False
    is_on_the_player = False
    if WIDTH == 640:
        speed_changer = 1
        speed = speed_changer
        bullet_speed = 1
        pX_move = 0.75
        enemy_speed = 0.75
    if WIDTH == 800:
        speed_changer = 1.5
        speed = speed_changer
        bullet_speed = 2
        pX_move = 1
        enemy_speed = 1
    if WIDTH == 1024:
        speed_changer = 2
        speed = speed_changer
        bullet_speed = 2.5
        pX_move = 1.5
        enemy_speed = 1.5
    if WIDTH == 1280:
        speed_changer = 2.5
        speed = speed_changer
        bullet_speed = 3
        pX_move = 2
        enemy_speed = 2

    enemy_collission_loop_time = time.time()
    while running:
        screen.fill((3, 3, 15))
        player = player_(playerImg, playerX, playerY, speed)
        bullet = bullet_(bulletImg, bullet2Img, playerX, playerY, bullet_speed)
        bullet_enemy = bullet_enemy_(enemyBulletImg, enemyBulletImg, enemyX, enemyY, bullet_speed)
        enemy = enemy_forces(enemyImg, enemyX, enemyY, enemy_speed)
        pygame.draw.polygon(screen, (200, 0, 0), ((WIDTH//2 - WIDTH//3, HEIGHT//11),
                                                  (WIDTH//2 - WIDTH//2.5, 0),
                                                  (WIDTH//2 + WIDTH//2.5, 0),
                                                  (WIDTH//2 + WIDTH//3, HEIGHT//11)))
        pygame.draw.polygon(screen, (200, 0, 0), ((0, HEIGHT),
                                                  (WIDTH//24, HEIGHT - HEIGHT//24),
                                                  (WIDTH//6 , HEIGHT - HEIGHT//24),
                                                  (WIDTH//6 - WIDTH//24, HEIGHT)))
        pygame.draw.polygon(screen, (0, 255, 0), ((0, HEIGHT),
                                                  (WIDTH // 24, HEIGHT - HEIGHT // 24),
                                                  (WIDTH // 24 + plasma_blast_bar_filler, HEIGHT - HEIGHT // 24),
                                                  (plasma_blast_bar_filler, HEIGHT)))
        pygame.draw.polygon(screen, (0, 0, 255), ((0, HEIGHT),
                                                  (WIDTH // 24, HEIGHT - HEIGHT // 24),
                                                  (WIDTH // 6, HEIGHT - HEIGHT // 24),
                                                  (WIDTH // 6 - WIDTH // 24, HEIGHT)), 3)
        pygame.draw.polygon(screen, plasma_sig_color, ((WIDTH // 6.66, HEIGHT),
                                                  (WIDTH // 5.21, HEIGHT - HEIGHT // 24),
                                                  (WIDTH // 2.08, HEIGHT - HEIGHT // 24),
                                                  (WIDTH // 2.28, HEIGHT)))
        fight = font_fight_panel.render("FIGHT!", True, (20, 20, 20))
        player_text = font_score_panel.render("PLAYER:", True, (20, 20, 20))
        player_scr = font_score_panel.render(str(player_score), True, (20, 20, 20))
        enemy_text = font_score_panel.render(":ENEMY", True, (20, 20, 20))
        enemy_scr = font_score_panel.render(str(enemy_score), True, (20, 20, 20))
        plasma_sig = font_score_panel.render("PLASMA BEAM", True, (20, 20, 20))

        stars.append([random.randint(0, 1024), random.randint(0, 768)])

        background_stars(stars)
        if len(stars) > 100:
            stars.pop(len(stars) - 1)

        global falling_star_loop_time
        if time.time() >= falling_star_loop_time + 2:
            global starrx, star_y_temp, x_dif, y_dif_temp, star_y_index
            starrx, star_y_temp, x_dif, y_dif_temp = falling_star(starrx, star_y_temp, x_dif, y_dif_temp)
            if starrx == WIDTH + 50:
                falling_star_loop_time = time.time()
                x_dif = 1
                global star_y_index
                star_y_index += 1
                if star_y_index == 4:
                    star_y_index = 0
                star_y_temp = starry[star_y_index]
                y_dif_temp = y_dif[star_y_index]

        plasma_beam = particle_(particleImg1, particleImg2, particleImg3, particleX, particleY)
        particles, particleX, particleY, particleX_changer, particleY_changer = plasma_beam.blit_particle_group(
            particles, particleX_changer, particleY_changer)

        if time.time() > time_for_bar + 0.5 and plasma_blast_bar_filler < 31 * WIDTH // 250 and truth == False:
            particleX_changer = WIDTH / 16000
            plasma_blast_bar_filler += WIDTH // 250
            time_for_bar = time.time()

        else:
            particleX_changer = 0
            plasma_blast_bar_filler += 0

        if plasma_blast_bar_filler >= 31 * WIDTH // 250 and truth == False:
            plasma_sig_color = (0, 255, 0)
            if particleX != playerX and particleY != playerY:
                if particleX < playerX + 16:
                    particleX_changer = WIDTH / 8000
                if particleX > playerX + 16:
                    particleX_changer = -WIDTH / 8000
                if particleY > playerY:
                    particleY_changer = -WIDTH / 8000
                if particleY < playerY:
                    particleY_changer = WIDTH / 8000
                if particleX == playerX + 16:
                    particleX_changer = 0
                if particleY == playerY:
                    particleY_changer = 0
                if particleX_changer == 0 and particleY_changer == 0:
                    particleX = playerX + 16
                    particleY = playerY

            if playerX - 10 < particleX < playerX + 10:
                is_on_the_player = True
        collision_enemy = collission_with_the_enemy(p_bulletX, p_bulletY, enemyX, enemyY)
        if collision_enemy:
            hit += 10
            enemy_collission_particle = True
        if enemy_collission_particle == False:
            enemy_collission_loop_time = time.time()
            enemy_cols_particles = []
        if enemy_collission_particle == True:
            enemy_cols_particles = collission_particles(enemy_cols_particles, enemyX + 32, enemyY + 32)
        if time.time() > enemy_collission_loop_time + 0.25:
            enemy_collission_loop_time = time.time()
            enemy_collission_particle = False

        collision_player = collission_with_the_player(enemy_bulletX, enemy_bulletY, playerX, playerY)
        if collision_player:
            health += 20
            player_collission_particle = True
        if player_collission_particle == False:
            player_collission_loop_time = time.time()
            player_cols_particles = []
        if player_collission_particle == True:
            player_cols_particles = collission_particles(player_cols_particles, playerX + 32, playerY + 32)
            if time.time() > player_collission_loop_time + 0.25:
                player_collission_loop_time = time.time()
                player_collission_particle = False


        collision_for_beam = collission_for_plasma_beam(particleX, particleY, enemyX, enemyY)
        if collision_for_beam:
            hit += 50
            enemy_collission_particle = True
        if hit > 100:
            player_score += 1
            hit = 0
        if health > 100:
            enemy_score += 1
            health = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP6:
                playerX = player.right()
            if event.key == pygame.K_KP4:
                playerX = player.left()
            if event.key == pygame.K_KP8:
                playerY = player.up()
            if event.key == pygame.K_KP2:
                playerY = player.down()
            if event.key == pygame.K_KP9:
                playerX, playerY = player.right_up()
            if event.key == pygame.K_KP7:
                playerX, playerY = player.left_up()
            if event.key == pygame.K_KP3:
                playerX, playerY = player.right_down()
            if event.key == pygame.K_KP1:
                playerX, playerY = player.left_down()
            if event.key == pygame.K_KP5:
                if plasma_blast_bar_filler >= 31 * WIDTH // 250 and is_on_the_player == True:
                    global particle_status
                    if particle_status is "ready":
                        particleX, particleY = plasma_beam.fire()
                        truth = True
                        plasma_blast_bar_filler = 0
                if plasma_blast_bar_filler != 0:
                    global fire_status_player
                    if fire_status_player is "ready":
                        p_bulletX, p_bulletY = bullet.fire()

        player.blit_to_screen(health)
        enemyX, pX_move, random_, random_up = enemy.enemy_initial_move(pX_move, random_, random_up)
        p_bulletY = bullet.blit_to_screenn(p_bulletX, p_bulletY)
        if p_bulletY < 0 or collision_enemy == True:
            p_bulletX, p_bulletY = playerX, playerY
            fire_status_player = "ready"

        if time.time() >= time_ + time_laps:
            time_ = time.time()
            time_laps = random.randint(0, 2)
            global fire_status_enemy
            if fire_status_enemy is "ready":
                enemy_bulletX, enemy_bulletY = bullet_enemy.fire()
        enemy_bulletY = bullet_enemy.blit_to_screenn(enemy_bulletX, enemy_bulletY)
        if enemy_bulletY > HEIGHT or collision_player == True:
            enemy_bulletX, enemy_bulletY = enemyX, enemyY
            fire_status_enemy = "ready"
        if truth == True:
            particleY_changer = -WIDTH / 8000
            particleY = plasma_beam.particles_go_to_the_enemy(WIDTH / 8000)
        if particleY < 0 or collision_for_beam == True:
            particleX, particleY = WIDTH // 80, HEIGHT - HEIGHT//24
            particle_status = "ready"
            plasma_blast_bar_filler = 0
            plasma_sig_color = (200, 0, 0)
            circle = []
            particleY_changer = 0
            speed = speed_changer
            truth = False
            is_on_the_player = False

        enemy.blit_to_screen_(hit)
        screen.blit(fight, (WIDTH//2 - WIDTH//20, HEIGHT//60))
        screen.blit(player_text, (WIDTH//2 - WIDTH//20 - WIDTH // 5, HEIGHT // 60))
        screen.blit(enemy_text, (WIDTH//2 + WIDTH//20 + WIDTH // 10, HEIGHT // 60))
        screen.blit(player_scr, (WIDTH // 2 - WIDTH // 20 - WIDTH // 7, HEIGHT // 20))
        screen.blit(enemy_scr, (WIDTH // 2 + WIDTH // 20 + WIDTH // 7, HEIGHT // 20))
        screen.blit(plasma_sig, (WIDTH // 5.21, HEIGHT - HEIGHT // 30))
        pygame.display.update()

def settings_menu(screen):
    running = True
    while running:
        global WIDTH, HEIGHT
        screen.fill((3, 3, 15))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        stars.append([random.randint(0, WIDTH), random.randint(0, HEIGHT)])

        background_stars(stars)
        if len(stars) > 100:
            stars.pop(len(stars) - 1)
        global falling_star_loop_time
        if time.time() >= falling_star_loop_time + 2:
            global starrx, star_y_temp, x_dif, y_dif_temp, star_y_index
            starrx, star_y_temp, x_dif, y_dif_temp = falling_star(starrx, star_y_temp, x_dif, y_dif_temp)
            if starrx == WIDTH + 50:
                falling_star_loop_time = time.time()
                x_dif = 1
                star_y_index += 1
                if star_y_index == 4:
                    star_y_index = 0
                global starry, y_dif
                star_y_temp = starry[star_y_index]
                y_dif_temp = y_dif[star_y_index]

        setting1 = pygame.draw.rect(screen, (255, 0, 0), (WIDTH // 8, HEIGHT // 3, WIDTH//4, HEIGHT//8))
        setting2 = pygame.draw.rect(screen, (255, 0, 0), (WIDTH // 8, (2 * HEIGHT) // 3, WIDTH//4, HEIGHT//8))
        setting3 = pygame.draw.rect(screen, (255, 0, 0), (WIDTH // 2 + WIDTH // 8, HEIGHT // 3, WIDTH//4, HEIGHT//8))
        setting4 = pygame.draw.rect(screen, (255, 0, 0), (WIDTH // 2 + WIDTH // 8, (2 * HEIGHT) // 3, WIDTH // 4, HEIGHT // 8))
        header = font_start_header.render("WAR IN SPACE", True, (255, 0, 0))
        setting1_text = font_start_menu.render("640x480", True, (25, 25, 25))
        setting2_text = font_start_menu.render("800x600", True, (25, 25, 25))
        setting3_text = font_start_menu.render("1024x768", True, (25, 25, 25))
        setting4_text = font_start_menu.render("1280x960", True, (25, 25, 25))
        x1, y1 = pygame.mouse.get_pos()
        if WIDTH // 8 < x1 < WIDTH // 8 + WIDTH//4 and HEIGHT // 3 < y1 < HEIGHT // 3 + HEIGHT//8:
            pygame.draw.rect(screen, (0, 255, 0), (WIDTH // 8, HEIGHT // 3, WIDTH//4, HEIGHT//8))
            click = pygame.mouse.get_pressed()
            if click == (1, 0, 0):
                WIDTH, HEIGHT = 640, 480
                screen = pygame.display.set_mode((WIDTH, HEIGHT))
                starrx, starry = WIDTH + 50, [HEIGHT // 4, HEIGHT - HEIGHT // 24, HEIGHT // 2, HEIGHT - HEIGHT // 3]
                bgr_list = []
                break
        if WIDTH // 8 < x1 < WIDTH // 8 + WIDTH//4 and (2 * HEIGHT) // 3 < y1 < (2 * HEIGHT) // 3 + HEIGHT//8:
            pygame.draw.rect(screen, (0, 255, 0), (WIDTH // 8, (2 * HEIGHT) // 3, WIDTH//4, HEIGHT//8))
            click = pygame.mouse.get_pressed()
            if click == (1, 0, 0):
                WIDTH, HEIGHT = 1024, 768
                screen = pygame.display.set_mode((WIDTH, HEIGHT))
                starrx, starry = WIDTH + 50, [HEIGHT // 4, HEIGHT - HEIGHT // 24, HEIGHT // 2, HEIGHT - HEIGHT // 3]
                bgr_list = []
                break
        if WIDTH // 2 + WIDTH // 8 < x1 < WIDTH // 2 + WIDTH // 8 + WIDTH//4 and HEIGHT // 3 < y1 < HEIGHT // 3 + HEIGHT // 8:
            pygame.draw.rect(screen, (0, 255, 0), (WIDTH // 2 + WIDTH // 8, HEIGHT // 3, WIDTH//4, HEIGHT//8))
            click = pygame.mouse.get_pressed()
            if click == (1, 0, 0):
                WIDTH, HEIGHT = 800, 600
                screen = pygame.display.set_mode((WIDTH, HEIGHT))
                starrx, starry = WIDTH + 50, [HEIGHT // 4, HEIGHT - HEIGHT // 24, HEIGHT // 2, HEIGHT - HEIGHT // 3]
                bgr_list = []
                break
        if WIDTH // 2 + WIDTH // 8 < x1 < WIDTH // 2 + WIDTH // 8 + WIDTH//4 and (2 * HEIGHT) // 3 < y1 < (2 * HEIGHT) // 3 + HEIGHT // 8:
            pygame.draw.rect(screen, (0, 255, 0), (WIDTH // 2 + WIDTH // 8, (2 * HEIGHT) // 3, WIDTH // 4, HEIGHT // 8))
            click = pygame.mouse.get_pressed()
            if click == (1, 0, 0):
                WIDTH, HEIGHT = 1280, 960
                screen = pygame.display.set_mode((WIDTH, HEIGHT))
                starrx, starry = WIDTH + 50, [HEIGHT // 4, HEIGHT - HEIGHT // 24, HEIGHT // 2, HEIGHT - HEIGHT // 3]
                bgr_list = []
                break
        screen.blit(header, (WIDTH // 2 - HEIGHT // 2, WIDTH // 10))
        screen.blit(setting1_text, (WIDTH // 4 - WIDTH // 15, HEIGHT // 2.70))
        screen.blit(setting2_text, (WIDTH // 1.45, HEIGHT // 2.70))
        screen.blit(setting3_text, (WIDTH // 4 - WIDTH // 14.5, HEIGHT // 1.41))
        screen.blit(setting4_text, (WIDTH // 1.48, HEIGHT // 1.41))
        pygame.display.update()
    return WIDTH, HEIGHT, screen, starrx, starry, bgr_list


def credits(screen):
    global WIDTH, HEIGHT
    credits_list_up = HEIGHT
    running = True
    while running:
        screen.fill((3, 3, 15))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        back_main_menu = pygame.draw.rect(screen, (255, 0, 0), (WIDTH // 1.17, HEIGHT // 1.1, WIDTH // 8, HEIGHT // 15))
        back_text = font_start_menu.render("BACK", True, (25, 25, 25))

        designer = font_start_menu.render(" GAME DESIGNER", True, (255, 255, 255))
        mert_ulas = font_start_menu.render("MERT ULAS", True, (255, 255, 255))
        musics = font_start_menu.render("SOUND EFFECTS & MUSIC", True, (255, 255, 255))
        contacts = font_start_menu.render("CONTACT", True, (255, 255, 255))
        e_mail = font_start_menu.render("h.mert.ulas@gmail.com", True, (255, 255, 255))

        screen.blit(designer, (WIDTH // 2 - WIDTH // 7.25, credits_list_up))
        screen.blit(mert_ulas, (WIDTH // 2 - WIDTH // 11.5, credits_list_up + HEIGHT // 12))
        screen.blit(musics, (WIDTH // 2 - WIDTH // 5, credits_list_up + HEIGHT // 4))
        screen.blit(mert_ulas, (WIDTH // 2 - WIDTH // 11.5, credits_list_up + HEIGHT // 3))
        screen.blit(contacts, (WIDTH // 2 - WIDTH // 13, credits_list_up + HEIGHT // 2))
        screen.blit(e_mail, (WIDTH // 2 - WIDTH // 6, credits_list_up + (7 * HEIGHT) // 12))

        credits_list_up -= HEIGHT / 2000

        stars.append([random.randint(0, WIDTH), random.randint(0, HEIGHT)])
        x, y = pygame.mouse.get_pos()
        if WIDTH // 1.17 < x < WIDTH // 1.17 + WIDTH // 8 and HEIGHT // 1.1 < y < HEIGHT // 1.1 + HEIGHT // 15:
            pygame.draw.rect(screen, (0, 255, 0), (WIDTH // 1.17, HEIGHT // 1.1, WIDTH // 8, HEIGHT // 15))
            click = pygame.mouse.get_pressed()
            if click == (1, 0, 0):
                break


        background_stars(stars)
        if len(stars) > 100:
            stars.pop(len(stars) - 1)
        global falling_star_loop_time
        if time.time() >= falling_star_loop_time + 2:
            global starrx, star_y_temp, x_dif, y_dif_temp, star_y_index
            starrx, star_y_temp, x_dif, y_dif_temp = falling_star(starrx, star_y_temp, x_dif, y_dif_temp)
            if starrx == WIDTH + 50:
                falling_star_loop_time = time.time()
                x_dif = 1
                star_y_index += 1
                if star_y_index == 4:
                    star_y_index = 0
                global starry, y_dif
                star_y_temp = starry[star_y_index]
                y_dif_temp = y_dif[star_y_index]

        screen.blit(back_text, (WIDTH // 1.14, HEIGHT // 1.08))
        pygame.display.update()
def quit_game():
    pygame.quit()
    quit()

def background_stars(stars):
    for star in stars:
        background_stars_list.append([[star[0], star[1]], [random.randint(0, 10) - 5, random.randint(0, 10) - 5],
                              random.randint(1, 2)])
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

def falling_star(xstar, ystar, x_dif, y_dif):
    falling_star_list.append([[xstar, ystar], [random.randint(0, 10), random.randint(0, 2) - 1],
                          random.randint(4, 6)])
    for particle in falling_star_list:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.2
        pygame.draw.circle(screen, (220, 220, 255), [int(particle[0][0]), int(particle[0][1])],
                           int(particle[2]))
        if particle[2] <= 0:
            falling_star_list.remove(particle)
    xstar -= x_dif
    ystar += y_dif
    if xstar < -125:
        xstar = WIDTH + 50
        ystar = 400
        x_dif = 0
        y_dif = 0
    return xstar, ystar, x_dif, y_dif

global WIDTH, HEIGHT
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

stars = []
background_stars_list = []
falling_star_list = []
falling_star_loop_time = time.time()
falling_star_status = False
x_dif = 1
y_dif = [0.5, -0.8, 0.2, -0.6]
star_y_index = 0
y_dif_temp = y_dif[star_y_index]
starrx, starry = WIDTH + 50, [HEIGHT // 4, HEIGHT - HEIGHT // 24, HEIGHT //2, HEIGHT - HEIGHT // 3]
star_y_temp = starry[star_y_index]
running = True
while running:
    screen.fill((3, 3, 15))

    #screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    stars.append([random.randint(0, WIDTH), random.randint(0, HEIGHT)])

    background_stars(stars)
    if len(stars) > 100:
        stars.pop(len(stars) - 1)

    if time.time() >= falling_star_loop_time + 2:
        starrx, star_y_temp, x_dif, y_dif_temp = falling_star(starrx, star_y_temp, x_dif, y_dif_temp)
        if starrx == WIDTH + 50:
            falling_star_loop_time = time.time()
            x_dif = 1
            star_y_index += 1
            if star_y_index == 4:
                star_y_index = 0
            star_y_temp = starry[star_y_index]
            y_dif_temp = y_dif[star_y_index]

    font_start_header = pygame.font.Font("data\skyridgegradital.ttf", (WIDTH // 15))
    font_start_menu = pygame.font.Font("data\skyridgesuperital.ttf", WIDTH // 46)
    font_fight_panel = pygame.font.Font("data\skyridgesuperital.ttf", HEIGHT // 25)
    font_score_panel = pygame.font.Font("data\skyridgesuperital.ttf", HEIGHT // 35)

    start_game_button = pygame.draw.rect(screen, (255, 0, 0), (WIDTH//2 - WIDTH//8, HEIGHT//3.5,
                                                               WIDTH//4, HEIGHT//10))
    settings_button = pygame.draw.rect(screen, (255, 0, 0), (WIDTH//2 - WIDTH//8, HEIGHT//3.5 + (11 * HEIGHT)//60,
                                                             WIDTH//4, HEIGHT//10))
    credits_button = pygame.draw.rect(screen, (255, 0, 0), (WIDTH//2 - WIDTH//8, HEIGHT//3.5 + (22 * HEIGHT)//60,
                                                               WIDTH//4, HEIGHT//10))
    quit_game_button = pygame.draw.rect(screen, (255, 0, 0),(WIDTH // 2 - WIDTH // 8, HEIGHT // 3.5 + (33 * HEIGHT) // 60,
                                                             WIDTH // 4, HEIGHT // 10))
    header = font_start_header.render("WAR IN SPACE", True, (255, 0, 0))
    start_game = font_start_menu.render("START GAME", True, (25, 25, 25))
    settings = font_start_menu.render("SETTINGS", True, (25, 25, 25))
    credit = font_start_menu.render("CREDITS", True, (25, 25, 25))
    quit_game = font_start_menu.render("QUIT GAME", True, (25, 25, 25))

    x, y = pygame.mouse.get_pos()
    #print("[{},{}]".format(x, y))
    if WIDTH//2 - WIDTH//8 < x < WIDTH//2 + WIDTH//8 and HEIGHT//3.5 < y < HEIGHT//3.5 + HEIGHT//10:
        pygame.draw.rect(screen, (0, 255, 0), (WIDTH//2 - WIDTH//8, HEIGHT//3.5, WIDTH//4, HEIGHT//10))
        click = pygame.mouse.get_pressed()
        if click == (1, 0, 0):
            the_game(event)
    if WIDTH//2 - WIDTH//8 < x < WIDTH//2 + WIDTH//8 and HEIGHT//3.5 + (11 * HEIGHT)//60 < y < HEIGHT//3.5 + (11 * HEIGHT)//60 + HEIGHT//10:
        pygame.draw.rect(screen, (0, 255, 0), (WIDTH//2 - WIDTH//8, HEIGHT//3.5 + (11 * HEIGHT)//60, WIDTH//4, HEIGHT//10))
        click = pygame.mouse.get_pressed()
        if click == (1, 0, 0):
            WIDTH, HEIGHT, screen, starrx, starry, stars = settings_menu(screen)
    if WIDTH//2 - WIDTH//8 < x < WIDTH//2 + WIDTH//8 and HEIGHT//3.5 + (22 * HEIGHT)//60 < y < HEIGHT//3.5 + (22 * HEIGHT)//60 + HEIGHT//10:
        pygame.draw.rect(screen, (0, 255, 0), (WIDTH//2 - WIDTH//8, HEIGHT//3.5 + (22 * HEIGHT)//60, WIDTH//4, HEIGHT//10))
        click = pygame.mouse.get_pressed()
        if click == (1, 0, 0):
            credits(screen)
    if WIDTH//2 - WIDTH//8 < x < WIDTH//2 + WIDTH//8 and HEIGHT // 3.5 + (33 * HEIGHT) // 60 < y < HEIGHT // 3.5 + (33 * HEIGHT) // 60 + HEIGHT // 10:
        pygame.draw.rect(screen, (0, 255, 0), (WIDTH // 2 - WIDTH // 8, HEIGHT // 3.5 + (33 * HEIGHT) // 60, WIDTH // 4, HEIGHT // 10))
        click = pygame.mouse.get_pressed()
        if click == (1, 0, 0):
            quit_game()
    screen.blit(header, (WIDTH // 2 - HEIGHT // 2, WIDTH // 10))
    screen.blit(start_game, (WIDTH // 2 - WIDTH // 10, HEIGHT // 3.15))
    screen.blit(settings, (WIDTH // 2 - WIDTH // 12.5, HEIGHT // 2))
    screen.blit(credit, (WIDTH // 2 - WIDTH // 14, HEIGHT // 1.46))
    screen.blit(quit_game, (WIDTH // 2 - WIDTH // 11.5, HEIGHT // 1.15))
    pygame.display.update()
