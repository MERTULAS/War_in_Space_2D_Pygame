 # War_in_Space_2D_Pygame
 Visually rich space combat game
 
 Hi, meet my game that I created by making additions on Space Invaders.
 
 This is Main Menu
 
 ![wis1](https://user-images.githubusercontent.com/67822910/91369924-aba69600-e815-11ea-9bf6-426c95405b50.PNG)
 
 This is main menu code:
 
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

 
 Screen size can be changed by entering the settings menu.
 
 ![wis2](https://user-images.githubusercontent.com/67822910/91370159-47d09d00-e816-11ea-8f82-5c0407dea2fd.PNG)
 
 Options include 640x480, 800x600, 1024x768 and 1280x960.
 All game content is updated according to the screen setting.
 
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
 
 
 This is the first in-game view. The game has no consequences. You just shoot the enemy and the enemy shoots you. Of course you can dodge  enemy's laser beam  :)
 
 In the background of the game, there are stars with a flashing effect that I created by forming particles. In addition to this, there are shooting stars that appear on the screen every half second and have 4 different starting points. I created shooting stars with my particle array. 
 
 ![wis3](https://user-images.githubusercontent.com/67822910/91370316-af86e800-e816-11ea-9214-dd0ef024531a.PNG)
 
 A plasma beam's charging bar is located in the bottom left of the game.
 
 ![wis4](https://user-images.githubusercontent.com/67822910/91370497-2f14b700-e817-11ea-86cb-2b1894c2c055.PNG)
 
 When this bar is full, plasma beam particles land on the player.
 
 ![wis5](https://user-images.githubusercontent.com/67822910/91371265-3046e380-e819-11ea-8487-dc0b8b22136b.PNG)
 
 When located on the player's vehicle the plasma beam is ready to be launched. The normal fire hit 10 damage, while the plasma beam is hit 50 damage.
 
 ![wis6](https://user-images.githubusercontent.com/67822910/91371436-a64b4a80-e819-11ea-979e-586f942d1b14.PNG)
 
 The Credits screen, on the other hand, consists of scrolling text from bottom to top.
 
 ![wis7](https://user-images.githubusercontent.com/67822910/91371541-f0ccc700-e819-11ea-905d-d8b59a971ca2.PNG)

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



 
