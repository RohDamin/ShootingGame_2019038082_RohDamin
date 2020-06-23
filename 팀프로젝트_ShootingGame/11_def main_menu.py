# def main_menu 작성자: 노다민
def main_menu():
    global screen

    screen.blit(background_img, (0, 0))
    draw_button(main_text, 0, 130)
    draw_button(b_start, 0, 300)
    draw_button(b_manual, 0, 380)
    draw_button(b_ranking, 0, 460)
    draw_button(b_end, 0, 540)

    b_start_rect = b_start.get_rect()
    b_manual_rect = b_manual.get_rect()
    b_ranking_rect = b_ranking.get_rect()
    b_end_rect = b_end.get_rect()

    pygame.display.update()

    while True:
        if pygame.mouse.get_pressed()[0]:  # 마우스 왼쪽 버튼 클릭
            mouse_pos = pygame.mouse.get_pos()
            if collide(mouse_pos[0], mouse_pos[1], b_start_rect, 300) == True:
                return 2
            elif collide(mouse_pos[0], mouse_pos[1], b_manual_rect, 380) == True:
                return 3
            elif collide(mouse_pos[0], mouse_pos[1], b_ranking_rect, 460) == True:
                return 4
            elif collide(mouse_pos[0], mouse_pos[1], b_end_rect, 540) == True:
                quit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()