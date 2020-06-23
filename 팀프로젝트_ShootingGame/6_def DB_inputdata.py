# def DB_inputdata 작성자: 노다민
def DB_inputdata():
    global screen
    screen.blit(saveranking_img, (0, 0))
    pygame.display.update()
    id = ''
    input_box = pygame.Rect(WIDTH / 2 + 50, 400, 60, 40)
    font = pygame.font.Font(font_name, 30)
    color = BLACK
    active = False
    while True:
        if pygame.mouse.get_pressed()[0]:  # 마우스 왼쪽 버튼 클릭
            mouse_pos = pygame.mouse.get_pos()
            if collide(mouse_pos[0], mouse_pos[1], b_main_rect, 600) == True:
                return 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                    color = WHITE  # 네모칸을 클릭하면 색깔 바뀜
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return id
                    elif event.key == pygame.K_BACKSPACE:
                        id = id[:-1]
                    else:
                        id += event.unicode

        screen.blit(saveranking_img, (0, 0))
        draw_text(screen, "Click on the SQUARE and enter your ID", 25, WIDTH / 2, 170, BLACK)
        draw_text(screen, "press ENTER to SAVE", 25, WIDTH / 2, 220, BLACK)
        draw_text(screen, "YOUR SCORE: ", 30, WIDTH / 2 - 100, 330, BLACK)
        draw_text(screen, str(score), 30, WIDTH / 2 + 100, 330, BLACK)
        draw_text(screen, "ENTER YOUR ID: ", 30, WIDTH / 2 - 100, 400, BLACK)
        draw_button(b_main, 0, 600)
        txt_surface = font.render(id, True, BLACK)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)
        b_main_rect = b_main.get_rect()
        pygame.display.flip()
        clock.tick(30)