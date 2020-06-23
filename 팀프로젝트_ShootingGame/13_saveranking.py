# def saveranking 작성자: 노다민
def saveranking(score):
    global screen
    screen.blit(saveranking_img, (0, 0))
    draw_button(b_main, 0, 600)
    b_main_rect = b_main.get_rect()
    word = DB_inputdata()
    draw_text(screen, "SAVED", 30, WIDTH / 2, 500, BLACK)

    DB_insert(word, str(score))

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