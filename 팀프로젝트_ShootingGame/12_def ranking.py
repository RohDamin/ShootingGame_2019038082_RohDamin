# def ranking 작성자: 노다민
def ranking():
    global screen
    screen.blit(ranking_img, (0, 0))
    draw_button(b_main, 0, 600)
    b_main_rect = b_main.get_rect()

    DB_check()

    pygame.display.update()

    while True:
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            if collide(mouse_pos[0], mouse_pos[1], b_main_rect, 600) == True:
                return 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()