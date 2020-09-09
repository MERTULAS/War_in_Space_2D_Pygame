 # War_in_Space_2D_Pygame
 Visually rich space combat game
 
 Hi, meet my game that I created by making additions on Space Invaders.
 
 This is Main Menu
 
 ![wis1](https://user-images.githubusercontent.com/67822910/91369924-aba69600-e815-11ea-9bf6-426c95405b50.PNG)
 
 The game starts first from the main menu. In this code, other written modules are imported.
 ```
 import pygame
 from TheGame import TheGame
 from random import randint
 from time import time
 from fonts import Fonts
 ```
 
 The module in which the fonts are loaded is as follows.
 ```
 import pygame


class Fonts:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def fight_panel_font(self):
        font_fight_panel = pygame.font.Font("data\\skyridgesuperital.ttf", self.height // 25)
        return font_fight_panel

    def score_panel_font(self):
        font_score_panel = pygame.font.Font("data\\skyridgesuperital.ttf", self.height // 35)
        return font_score_panel

    def start_header_font(self):
        font_start_header = pygame.font.Font("data\\skyridgegradital.ttf", (self.width // 15))
        return font_start_header

    def start_menu_font(self):
        font_start_menu = pygame.font.Font("data\\skyridgesuperital.ttf", self.width // 46)
        return font_start_menu
 ```
 
 In the background of the game, there are stars with a flashing effect that I created by forming particles. In addition to this, there are shooting stars that appear on the  screen every half second and have 4 different starting points. I created shooting stars with my particle array. Flashing star particles and shooting star particles in the background are defined by the following functions.
 
 ```
 ...
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
 ...
 ```
 
 Screen size can be changed by entering the settings menu.
 
 ![wis2](https://user-images.githubusercontent.com/67822910/91370159-47d09d00-e816-11ea-8f82-5c0407dea2fd.PNG)
 
 Options include 640x480, 800x600, 1024x768 and 1280x960.
 All game content is updated according to the screen setting.
 
 In the code below, you can find how the selection process is done in the settings menu. The size of the rectangle the mouse is clicked on is adjusted. All the codes of the settings section are available in the files
 
 ```
 ...
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
 ...
 ```
 
 
 This is the first in-game view. The game has no consequences (:D). You just shoot the enemy and the enemy shoots you. Of course you can dodge  enemy's laser beam  :)
 
 ![wis3](https://user-images.githubusercontent.com/67822910/91370316-af86e800-e816-11ea-9214-dd0ef024531a.PNG)
 
 A plasma beam's charging bar is located in the bottom left of the game.
 
 
 ![wis4](https://user-images.githubusercontent.com/67822910/91370497-2f14b700-e817-11ea-86cb-2b1894c2c055.PNG)
 
 When this bar is full, plasma beam particles land on the player.
 
 ![wis5](https://user-images.githubusercontent.com/67822910/91371265-3046e380-e819-11ea-8487-dc0b8b22136b.PNG)
 
 When located on the player's vehicle the plasma beam is ready to be launched. The normal fire hit 10 damage, while the plasma beam is hit 50 damage.
 
 ![wis6](https://user-images.githubusercontent.com/67822910/91371436-a64b4a80-e819-11ea-979e-586f942d1b14.PNG)
 
 The Credits screen, on the other hand, consists of scrolling text from bottom to top.
 
 ![wis7](https://user-images.githubusercontent.com/67822910/91371541-f0ccc700-e819-11ea-905d-d8b59a971ca2.PNG)

 # Okay, now let's talk a little bit about how it works.
 # Classes and Game Structure
 
 We have 5 different classes. These are "Player", "Enemy", "Bullet", "EnemyBullet", "Particles". The "Player" class contains the visual, location, and health of the player. The enemy class contains the visual, location, and health of the enemy. It includes a movement function that puts random limits on the enemy.
 
```
...
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
...
```
There is a limitation on bullet movement. A new bullet cannot be fired before the bullet reaches the limits of the screen or hits the enemy! The same is true for the enemy's bullet. Before explaining this situation, let's take a look at the "Bullet" class.
```
...
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
...
```
You remember that the "fire_status" variable defined at the beginning is "ready". When the space key is pressed, it is checked whether the "fire_status" variable is "ready". İf  the "fire_status" is "ready", The position of the shooting vehicle is thrown into an array. The first element of this sequence is preserved because the first element is the bullet position at the time of fire. If this was not done, the bullet would advance when it was fired, but it would move to the right and left at the same time as the vehicle. We don't want this. Until the bullet reaches the limits, this sequence is preserved and the "fire_status" variable takes the value "wait". When this happens, we cannot fire.

# Collision Situation

The distance is calculated based on the positions of the bullet and the target vehicle. If the value found by this calculation is less than a certain distance, it is accepted that there is a collision here. Particles are used to create an explosion effect at the time of collision. The defined particle function becomes active for "0.25 seconds" and is active in the explosion and then disappears.


The collision functions is given below.
```
...
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
...
```
When the plasma beam is active and until this plasma beam reaches the limits, the bullet cannot be fired.


```
...
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
...
```
# The Plasma Beam

The charge of the Plasma beam starts to charge from the moment the game starts. It fills up step by step, at a speed adjusted to the game size. As soon as the rod is full, the plasma beam particles float on the player and wait for the shot. When fired, the plasma beam of particles glides towards the enemy, dealing 5x shell damage. Three different visuals have been defined for this array of particles, these are small, medium and large pieces of fire. 
```
...
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
...
```
# All python scripts and data file are included in the files. Thanks for reading...
 
