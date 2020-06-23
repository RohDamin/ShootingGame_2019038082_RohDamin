# def endingCredit 작성자: 노다민
def endingCredit(time):
    global screen

    screen.blit(background_img3, (0, 0))
    endingCredit_img_rect = endingCredit_img.get_rect()
    endingCredit_img_rect.y = HEIGHT - 10
    screen.blit(endingCredit_img, (WIDTH / 2 - endingCredit_img_rect.width / 2, endingCredit_img_rect.y))

    pygame.display.update()

    while True:
        screen.blit(background_img3, (0, 0))
        endingCredit_img_rect.y -= 3  # 엔딩크레딧이 올라가는 속도
        screen.blit(endingCredit_img, (WIDTH / 2 - endingCredit_img_rect.width / 2, endingCredit_img_rect.y))
        now = pygame.time.get_ticks()
        if time + 8000 <= now:
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.flip()
        clock.tick(60)