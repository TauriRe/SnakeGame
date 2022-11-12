import pygame, sys, random

from settings import frame_size_x, frame_size_y, game_window, canvas, VELOCITY
from design import small_font, medium_font, large_font, yellow, red, black, green, clock, apple_img, blue, snake_img, tail_img, lyellow, fgreen, TOP_WIDTH, APPLE_SIZE

# Checks for errors encountered
check_errors = pygame.init()
# pygame.init() example output -> (6, 0)
# second number in tuple gives number of errors
if check_errors[1] > 0:
    print(f'[!] Had {check_errors[1]} errors when initialising game, exiting...')
    sys.exit(-1)
else:
    print('[+] Game successfully initialised')


score = 0


# Score
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (frame_size_x / 10, 15)
    else:
        score_rect.midtop = (frame_size_x / 2, frame_size_y / 1.25)
    game_window.blit(score_surface, score_rect)
    # pygame.display.flip()


SNAKE_WIDTH = 15
# Game variables
snake_pos = [100, 50]
snake_body = [[100, 50], [100 - 10, 50], [100 - (2 * 10), 50]]

food_pos = [random.randrange(1, (frame_size_x // 10)) * 10, random.randrange(1, (frame_size_y // 10)) * 10]
food_spawn = True

direction = 'RIGHT'
change_to = direction


RUNNING, PAUSE = 0, 1


# uss
def snake(snakelist, direction):

    if direction == 'right':
        head = pygame.transform.rotate(snake_img, 270)
        tail = pygame.transform.rotate(tail_img, 270)
    if direction == 'left':
        head = pygame.transform.rotate(snake_img, 90)
        tail = pygame.transform.rotate(tail_img, 90)
    if direction == 'up':
        head = pygame.transform.rotate(snake_img, 0)
        tail = pygame.transform.rotate(tail_img, 0)
    if direction == 'down':
        head = pygame.transform.rotate(snake_img, 180)
        tail = pygame.transform.rotate(tail_img, 180)

    canvas.blit(head, snakelist[-1])
    canvas.blit(tail, snakelist[0])

    for XnY in snakelist[1:-1]:
        pygame.draw.rect(canvas, blue, (XnY[0], XnY[1], SNAKE_WIDTH, SNAKE_WIDTH))


def start_game():

    canvas.fill(lyellow)
    start_font1 = large_font.render("Ussikas", True, fgreen)
    start_font2 = medium_font.render("Start", True, fgreen, lyellow)
    start_font4 = medium_font.render("Exit", True, fgreen, lyellow)
    start_font5 = medium_font.render("Difficulty", True, fgreen, lyellow)
    start_font6 = medium_font.render("Settings", True, fgreen, lyellow)
    start_font7 = medium_font.render("Levels", True, fgreen, lyellow)

    start_font1_rect = start_font1.get_rect()
    start_font2_rect = start_font2.get_rect()
    start_font4_rect = start_font4.get_rect()
    start_font5_rect = start_font5.get_rect()
    start_font6_rect = start_font6.get_rect()
    start_font7_rect = start_font7.get_rect()

    start_font1_rect.center = (frame_size_x/2, frame_size_y/2 - 100)
    start_font2_rect.center = (frame_size_x/2 + 100, frame_size_y/2)
    start_font7_rect.center = (frame_size_x/2 + 100, frame_size_y/2 + 50)
    start_font6_rect.center = (frame_size_x/2 + 100, frame_size_y / 2 + 100)
    start_font5_rect.center = (frame_size_x/2 + 100, frame_size_y / 2 + 150)
    start_font4_rect.center = (frame_size_x/2 + 100, frame_size_y/2 + 200)

    canvas.blit(start_font1, start_font1_rect)
    canvas.blit(start_font2, start_font2_rect)
    canvas.blit(start_font4, start_font4_rect)
    canvas.blit(start_font5, start_font5_rect)
    canvas.blit(start_font6, start_font6_rect)
    canvas.blit(start_font7, start_font7_rect)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_paused()
                if event.key == pygame.K_s:
                    gameloop()
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                '''#if x > start_font3_rect.left and x < start_font3_rect.right:
                 #   if y > start_font3_rect.top and y < start_font3_rect.bottom:
                  #      start_inst(start_font1, start_font1_rect)'''
                if x > start_font5_rect.left and x < start_font5_rect.right:
                    if y > start_font5_rect.top and y < start_font5_rect.bottom:
                        raskustase()
                if x > start_font6_rect.left and x < start_font6_rect.right:
                    if y > start_font6_rect.top and y < start_font6_rect.bottom:
                        options()
                if x > start_font2_rect.left and x < start_font2_rect.right:
                    if y > start_font2_rect.top and y < start_font2_rect.bottom:
                        gameloop()

                if x > start_font4_rect.left and x < start_font4_rect.right:
                    if y > start_font4_rect.top and y < start_font4_rect.bottom:
                        pygame.quit()
                        sys.exit()

        pygame.display.update()


'''
def start_inst(start_font1, start_font1_rect):
    canvas.fill(lyellow)
    canvas.blit(start_font1, start_font1_rect)
    start_inst1 = small_font.render("--> Ära puuduta ääri, muidu sa sured", True, fgreen)
    start_inst2 = small_font.render("--> Söö punaseid õunu, et suuremaks saada", True, fgreen)
    start_inst3 = small_font.render("--> Ära mine enda pihta", True, fgreen)


    start_inst5_rect = start_inst5.get_rect()
    start_inst5_rect.center = (frame_size_x - start_inst5_rect.width / 2 - 30, frame_size_y - start_inst5_rect.height / 2 - 30)

    canvas.blit(start_inst1, (frame_size_x/8, frame_size_y/2))
    canvas.blit(start_inst2, (frame_size_x/8, frame_size_y/2 + 30))
    canvas.blit(start_inst3, (frame_size_x/8, frame_size_y/2 + 60))

    canvas.blit(start_inst5, start_inst5_rect)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x > start_inst5_rect.left and x < start_inst5_rect.right:
                    if y > start_inst5_rect.top and y < start_inst5_rect.bottom:
                        start_game()
        pygame.display.update()'''


#seaded
def options():

    canvas.fill(lyellow)
    options1 = large_font.render("Settings", True, black)
    #easy option

    options1_rect = options1.get_rect()
    options1_rect.center = (frame_size_x / 2, 80)
    canvas.blit(options1, options1_rect)
    canvas.blit(start_inst5, start_inst5_rect)

    options_true = True
    while options_true == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                if x > start_inst5_rect.left and x < start_inst5_rect.right:
                    if y > start_inst5_rect.top and y < start_inst5_rect.bottom:
                        start_game()

        pygame.display.update()




def raskustase():


    canvas.fill(lyellow)
    start_inst1 = large_font.render("Raskustasemed", True, black)
    start_inst1_rect = start_inst1.get_rect()
    start_inst1_rect.center = (frame_size_x / 2, 80)
    canvas.blit(start_inst1, start_inst1_rect)


    #canvas.blit(start_inst5, (10, 170))
    canvas.blit(start_inst5, start_inst5_rect)

    # Difficulty settings
    # Easy      ->  4
    # Medium    ->  6
    # Hard      ->  8
    # Harder    ->  60
    # Impossible->  120


    start_inst6 = medium_font.render("Lihtne", True, black)
    start_inst7 = medium_font.render("Keskmine", True, black)
    start_inst8 = medium_font.render("Raske", True, black)

    start_inst6_rect = start_inst6.get_rect()
    start_inst7_rect = start_inst7.get_rect()
    start_inst8_rect = start_inst8.get_rect()

    start_inst6_rect.center = (frame_size_x / 2 - 200, 180)
    start_inst7_rect.center = (frame_size_x / 2 - 180, 220)
    start_inst8_rect.center = (frame_size_x / 2 - 200, 260)



    canvas.blit(start_inst6, start_inst6_rect)
    canvas.blit(start_inst7, start_inst7_rect)
    canvas.blit(start_inst8, start_inst8_rect)

    start_inst6_valimine = pygame.draw.circle(game_window, blue, [frame_size_x / 2 - 260, 180], 7, 0)
    start_inst7_valimine = pygame.draw.circle(game_window, black, [frame_size_x / 2 - 260, 220], 7, 0)
    start_inst8_valimine = pygame.draw.circle(game_window, black, [frame_size_x / 2 - 260, 260], 7, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                #Lihtne
                if x > start_inst6_rect.left and x < start_inst6_rect.right:
                    if y > start_inst6_rect.top and y < start_inst6_rect.bottom:
                        VELOCITY = 4
                        start_inst6_valimine = pygame.draw.circle(game_window, blue, [frame_size_x / 2 - 260, 180], 7, 0)
                        start_inst7_valimine = pygame.draw.circle(game_window, black, [frame_size_x / 2 - 260, 220], 7, 0)
                        start_inst8_valimine = pygame.draw.circle(game_window, black, [frame_size_x / 2 - 260, 260], 7, 0)
                # keskmine
                if x > start_inst7_rect.left and x < start_inst7_rect.right:
                    if y > start_inst7_rect.top and x < start_inst7_rect.bottom:
                        VELOCITY = 6
                        start_inst6_valimine = pygame.draw.circle(game_window, black, [frame_size_x / 2 - 260, 180], 7, 0)
                        start_inst7_valimine = pygame.draw.circle(game_window, blue, [frame_size_x / 2 - 260, 220], 7, 0)
                        start_inst8_valimine = pygame.draw.circle(game_window, black, [frame_size_x / 2 - 260, 260], 7, 0)
                # raske
                if x > start_inst8_rect.left and x < start_inst8_rect.right:
                    if y > start_inst8_rect.top and y < start_inst8_rect.bottom:
                        VELOCITY = 60
                        start_inst6_valimine = pygame.draw.circle(game_window, black, [frame_size_x / 2 - 260, 180], 7, 0)
                        start_inst7_valimine = pygame.draw.circle(game_window, black, [frame_size_x / 2 - 260, 220], 7, 0)
                        start_inst8_valimine = pygame.draw.circle(game_window, blue, [frame_size_x / 2 - 260, 260], 7, 0)

                # tagasi
                if x > start_inst5_rect.left and x < start_inst5_rect.right:
                    if y > start_inst5_rect.top and y < start_inst5_rect.bottom:
                        start_game()
        pygame.display.update()
#gameloop mäng


def gameloop():

    while True:

        LEAD_X = 0
        LEAD_Y = 100
        direction = 'right'
        score = small_font.render("Score:0", True, yellow)
        APPLE_X = random.randrange(0, frame_size_x - 10, 10)
        APPLE_Y = random.randrange(TOP_WIDTH, frame_size_y - 10, 10)
        snakelist = []
        snakelength = 10
        pause_font = medium_font.render('II', True, red)
        tester = 1

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_LEFT:
                        if direction == 'right':
                            pass
                        else:
                            direction = 'left'
                    if event.key == pygame.K_RIGHT:
                        if direction == 'left':
                            pass
                        else:
                            direction = 'right'
                    if event.key == pygame.K_UP:
                        if direction == 'down':
                            pass
                        else:
                            direction = 'up'
                    if event.key == pygame.K_DOWN:
                        if direction == 'up':
                            pass
                        else:
                            direction = 'down'
                    if event.key == pygame.K_ESCAPE:
                        game_paused()

                '''if event.key == pygame.K_ESCAPE:
                    game_paused()'''
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pause_xy = event.pos
                    if pause_xy[0] > (frame_size_x - 50) and pause_xy[0] < frame_size_x:
                        if pause_xy[1] > 0 and pause_xy[1] < 50:
                            game_paused()
            if direction == 'up':
                LEAD_Y -= VELOCITY
                if LEAD_Y < TOP_WIDTH:
                    gameover()
            if direction == 'down':
                LEAD_Y += VELOCITY
                if LEAD_Y > frame_size_y - SNAKE_WIDTH:
                    gameover()
            if direction == 'right':
                LEAD_X += VELOCITY
                if LEAD_X > frame_size_x - SNAKE_WIDTH:
                    gameover()
            if direction == 'left':
                LEAD_X -= VELOCITY
                if LEAD_X < 0:
                    gameover()

            snakehead = []
            snakehead.append(LEAD_X)
            snakehead.append(LEAD_Y)
            snakelist.append(snakehead)

            snake_head_rect = pygame.Rect(LEAD_X, LEAD_Y, SNAKE_WIDTH, SNAKE_WIDTH)
            apple_rect = pygame.Rect(APPLE_X, APPLE_Y, APPLE_SIZE, APPLE_SIZE)

            if len(snakelist) > snakelength:
                del snakelist[0]
            for point in snakelist[:-1]:
                if point == snakehead:
                    gameover()

            canvas.fill(black)

            snake(snakelist, direction)
            # õunaga kokkupõrge

            if snake_head_rect.colliderect(apple_rect):
                APPLE_X = random.randrange(0, frame_size_x - 10, 10)
                APPLE_Y = random.randrange(TOP_WIDTH, frame_size_y - 10, 10)
                snakelength += 10
                tester += 1
                score = small_font.render("Score:" + str(snakelength - 19), True, yellow)
                pygame.mixer.find_channel().play(pygame.mixer.Sound("sound/collect.wav"))
            if score != tester:
                score = small_font.render("Score:" + str(tester), True, yellow)

            canvas.blit(score, (20, 10))
            pygame.draw.line(canvas, green, (0, TOP_WIDTH), (frame_size_x, TOP_WIDTH))
            pygame.draw.line(canvas, yellow, (frame_size_x - 60, 0), (frame_size_x - 60, TOP_WIDTH))
            pygame.draw.rect(canvas, yellow, (frame_size_x - 60, 0, 60, TOP_WIDTH))
            canvas.blit(pause_font, (frame_size_x - 45, 1))
            canvas.blit(apple_img, (APPLE_X, APPLE_Y))
            pygame.display.update()

            clock.tick(60)


def gameover():

    canvas.fill(black)

    #gameover text
    gameover_text1 = large_font.render("You Died", True, red)
    gameover_text1_rect = gameover_text1.get_rect()
    gameover_text1_rect.center = (frame_size_x / 2, 80)
    canvas.blit(gameover_text1, gameover_text1_rect)

    #restart text
    gameover_restart_text = medium_font.render("Restart", True, red)
    gameover_restart_text_rect = gameover_restart_text.get_rect()
    gameover_restart_text_rect.center = (frame_size_x / 2 - 200, 390)
    canvas.blit(gameover_restart_text, gameover_restart_text_rect)

    # mainmenu text
    gameover_main_menu = medium_font.render("Main Menu", True, red)
    gameover_main_menu_rect = gameover_main_menu.get_rect()
    gameover_main_menu_rect.center = (frame_size_x / 2 - 200, 440)
    canvas.blit(gameover_main_menu, gameover_main_menu_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                # Restart button
                if x > gameover_restart_text_rect.left and x < gameover_restart_text_rect.right:
                    if y > gameover_restart_text_rect.top and y < gameover_restart_text_rect.bottom:
                        gameloop()

                # Main Menu button
                if x > gameover_main_menu_rect.left and x < gameover_main_menu_rect.right:
                    if y > gameover_main_menu_rect.top and y < gameover_main_menu_rect.bottom:
                        start_game()
        pygame.display.update()


#defoneerib nupu tagasi

start_inst5 = medium_font.render("<<Tagasi", True, fgreen, lyellow)
start_inst5_rect = start_inst5.get_rect()
start_inst5_rect.center = (frame_size_x - start_inst5_rect.width / 2 - 30, frame_size_y - start_inst5_rect.height / 2 - 30)
canvas.blit(start_inst5, start_inst5_rect)
pygame.display.update()


def tagasi():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x > start_inst5_rect.left and x < start_inst5_rect.right:
                    if y > start_inst5_rect.top and y < start_inst5_rect.bottom:
                        return
        pygame.display.flip()


def tagasi2():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x > start_inst5_rect.left and x < start_inst5_rect.right:
                    if y > start_inst5_rect.top and y < start_inst5_rect.bottom:
                        gameloop()
        pygame.display.flip()


def game_paused():
    pygame.draw.rect(canvas, lyellow, pygame.Rect(0, 0, 300, 700))

    paused_font1 = medium_font.render("Game Paused", True, red)
    paused_font2 = medium_font.render("Resume", True, black)
    paused_font3 = medium_font.render("Settings", True, black)
    pause_font4 = medium_font.render("Main Menu", True, black)

    paused_font1_rect = paused_font1.get_rect()
    paused_font2_rect = paused_font2.get_rect()
    paused_font3_rect = paused_font3.get_rect()
    paused_font4_rect = pause_font4.get_rect()

    paused_font1_rect.center = (frame_size_x/5, frame_size_y/8.5)
    paused_font2_rect.center = (frame_size_x/5, frame_size_y/5)
    paused_font3_rect.center = (frame_size_x/5, frame_size_y/3.5)
    paused_font4_rect.center = (frame_size_x/5, frame_size_y/2.7)

    canvas.blit(paused_font1, paused_font1_rect)
    canvas.blit(paused_font2, paused_font2_rect)
    canvas.blit(paused_font3, paused_font3_rect)
    canvas.blit(pause_font4, paused_font4_rect)

    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                pause_xy = event.pos
                if pause_xy[0] > (frame_size_x - 50) and pause_xy[0] < frame_size_x:
                    if pause_xy[1] > 0 and pause_xy[1] < 50:
                        return
                if paused_font2_rect.left < x < paused_font2_rect.right:
                    if y > paused_font2_rect.top and y < paused_font2_rect.bottom:
                        return
                if x > paused_font3_rect.left and x < paused_font3_rect.right:
                    if y > paused_font3_rect.top and y < paused_font3_rect.bottom:
                        options()
                if x > paused_font4_rect.left and x < paused_font4_rect.right:
                    if y > paused_font4_rect.top and y < paused_font4_rect.bottom:
                        start_game()

            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    paused = False
        pygame.display.update()
        clock.tick(4)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    start_game()
    pygame.display.flip()
