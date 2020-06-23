# 게임 메인 루프 작성자: 심지연, 양희진, 노다민
##1. 변수 선언
running = True
menu = True
game = False
start = 0
score = 0

level = 1
level_time = 50000

p1_inventory_key = 4
p2_inventory_key = 1

level1_bgm = True
level2_bgm = True
level3_bgm = True
level4_bgm = True

## 2. 게임 메인 루프
while running:
    ##1. 메인 메뉴
    if menu:
        pygame.mixer.music.load('bnb_ocean.mp3')
        pygame.mixer.music.play(-1)

        while (1):
            if main_menu() == 2:  # 게임 시작 선택
                q = choose_character()
                d = q.queue
                p2_image = d[0]
                p1_image = d[1]
                break
            elif main_menu() == 3:  # 게임 방법 선택
                if manual() == 1:
                    pass
            elif main_menu() == 4:  # 랭킹 확인 선택
                if ranking() == 1:
                    pass
        game = True
        menu = False

        start_time = pygame.time.get_ticks()  # 게임 시작 시간

        all_sprites = pygame.sprite.Group()

        if p2_image == 1: player2 = Player(WIDTH / 2 - 80, HEIGHT - 20, player1_img)  # player2 이미지 선택
        if p2_image == 2: player2 = Player(WIDTH / 2 - 80, HEIGHT - 20, player2_img)
        if p2_image == 3: player2 = Player(WIDTH / 2 - 80, HEIGHT - 20, player3_img)
        if p2_image == 4: player2 = Player(WIDTH / 2 - 80, HEIGHT - 20, player4_img)
        if p2_image == 5: player2 = Player(WIDTH / 2 - 80, HEIGHT - 20, player5_img)

        if p1_image == 1: player = Player(WIDTH / 2 + 80, HEIGHT - 20, player1_img)  # player1 이미지 선택
        if p1_image == 2: player = Player(WIDTH / 2 + 80, HEIGHT - 20, player2_img)
        if p1_image == 3: player = Player(WIDTH / 2 + 80, HEIGHT - 20, player3_img)
        if p1_image == 4: player = Player(WIDTH / 2 + 80, HEIGHT - 20, player4_img)
        if p1_image == 5: player = Player(WIDTH / 2 + 80, HEIGHT - 20, player5_img)

        all_sprites.add(player)
        all_sprites.add(player2)

        enemys = pygame.sprite.Group()
        boss = Boss()
        for i in range(12):
            make_new_enemy(level)
        bullets = pygame.sprite.Group()
        enemy_bullets = pygame.sprite.Group()
        boss_bullets = pygame.sprite.Group()
        item3_bullets = pygame.sprite.Group()
        items = pygame.sprite.Group()

    clock.tick(FPS)
    ##2. 게임 루프
    if game:
        print(all_sprites)
        now = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_o:  # player1 공격
                    player.shot_top()
                    score += 1
                if event.key == pygame.K_p:
                    player.shot_bottom()
                    score += 1
                if event.key == pygame.K_LEFT:  # player1 이동
                    player.speedx = -5
                if event.key == pygame.K_RIGHT:
                    player.speedx = 5
                if event.key == pygame.K_UP:
                    player.speedy = -5
                if event.key == pygame.K_DOWN:
                    player.speedy = +5

                if event.key == pygame.K_r:  # player2 공격
                    player2.shot_top()
                    score += 1
                if event.key == pygame.K_t:
                    player2.shot_bottom()
                    score += 1
                if event.key == pygame.K_a:  # player2 이동
                    player2.speedx = -5
                if event.key == pygame.K_d:
                    player2.speedx = 5
                if event.key == pygame.K_w:
                    player2.speedy = -5
                if event.key == pygame.K_s:
                    player2.speedy = +5

                if event.key == pygame.K_k:  # player1 인벤토리 조작
                    p1_inventory_key += 1
                    if p1_inventory_key > 6:
                        p1_inventory_key = 4
                if event.key == pygame.K_f:  # player2 인벤토리 조작
                    p2_inventory_key += 1
                    if p2_inventory_key > 3:
                        p2_inventory_key = 1

                if event.key == pygame.K_l:  # player1 인벤토리 아이템 사용
                    player.item(p1_inventory_key - 3)
                if event.key == pygame.K_g:  # player2 인벤토리 아이템 사용
                    player2.item(p2_inventory_key)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.speedx = 0
                if event.key == pygame.K_RIGHT:
                    player.speedx = 0
                if event.key == pygame.K_UP:
                    player.speedy = 0
                if event.key == pygame.K_DOWN:
                    player.speedy = 0

                if event.key == pygame.K_a:
                    player2.speedx = 0
                if event.key == pygame.K_d:
                    player2.speedx = 0
                if event.key == pygame.K_w:
                    player2.speedy = 0
                if event.key == pygame.K_s:
                    player2.speedy = 0

        if level == 4:
            all_sprites.add(boss)

        # 레벨 변경
        if level < 4:
            if now - start_time > level_time:
                nextlevel(now, level)
                level += 1
                score += 500 + 200 * level
                start_time = now + 2000
                all_sprites.remove(enemy_bullets)
                all_sprites.remove(item3_bullets)
                all_sprites.remove(bullets)
                all_sprites.remove(boss_bullets)

        # 단계별로 다른 배경음악 재생
        if level1_bgm:
            if level == 1:
                pygame.mixer.init()
                pygame.mixer.music.load('kart_forest.mp3')
                pygame.mixer.music.play(-1)
                level1_bgm = False
        if level2_bgm:
            if level == 2:
                pygame.mixer.init()
                pygame.mixer.music.load('bnb_kfc.mp3')
                pygame.mixer.music.play(-1)
                level2_bgm = False
        if level3_bgm:
            if level == 3:
                pygame.mixer.init()
                pygame.mixer.music.load('bnb_bulla.mp3')
                pygame.mixer.music.play(-1)
                level3_bgm = False
        if level4_bgm:
            if level == 4:
                pygame.mixer.init()
                pygame.mixer.music.load('bnb_octopus.mp3')
                pygame.mixer.music.play(-1)
                level4_bgm = False

        # 업데이트
        all_sprites.update()

        # 충돌 체크
        hits = pygame.sprite.groupcollide(enemys, bullets, True, True)  # 1. 적 - 플레이어 총알
        for hit in hits:
            hit_sound.play()
            make_new_enemy(level)
            score += random.randrange(20, 50)
            if random.random() > 0.7:
                item = Item(hit.rect.center)
                all_sprites.add(item)
                items.add(item)
        hits = pygame.sprite.groupcollide(enemys, item3_bullets, True, False)  # 2. 적 - 아이템3
        for hit in hits:
            hit_sound.play()
            make_new_enemy(level)
            score += random.randrange(20, 50)
        hits = pygame.sprite.groupcollide(enemy_bullets, item3_bullets, True, False)  # 3. 적 총알 - 아이템3
        for hit in hits:
            pass
        hits = pygame.sprite.spritecollide(player, enemy_bullets, True)  # 4. 플레이어1 - 적 총알
        for hit in hits:
            player.HP -= 10
            if player.HP <= 0 and player.lives > 0:
                player.HP = 100
                player.lives -= 1
            elif player.HP <= 0 and player.lives == 0:
                player.HP = 0
                player.lives = 0
        hits = pygame.sprite.spritecollide(player2, enemy_bullets, True)  # 5. 플레이어2 - 적 총알
        for hit in hits:
            player2.HP -= 10
            if player2.HP <= 0 and player2.lives > 0:
                player2.HP = 100
                player2.lives -= 1
            elif player2.HP <= 0 and player2.lives == 0:
                player2.HP = 0
                player2.lives = 0
        hits = pygame.sprite.spritecollide(player, enemys, True)  # 6. 플레이어1 - 적
        for hit in hits:
            player.HP -= 50
            if player.HP <= 0 and player.lives > 0:
                player.HP = 100
                player.lives -= 1
            elif player.HP <= 0 and player.lives == 0:
                player.HP = 0
                player.lives = 0
            make_new_enemy(level)
        hits = pygame.sprite.spritecollide(player2, enemys, True)  # 7. 플레이어2 - 적
        for hit in hits:
            player2.HP -= 50
            player2.HP -= 20
            if player2.HP <= 0 and player2.lives > 0:
                player2.HP = 100
                player2.lives -= 1
            elif player2.HP <= 0 and player2.lives == 0:
                player2.HP = 0
                player2.lives = 0
            make_new_enemy(level)
        hits = pygame.sprite.spritecollide(player, items, True)  # 8. 플레이어1 - 아이템
        for hit in hits:
            score += random.randrange(20, 40)
            if hit.type == 'item1':
                player.item1 += 1
            if hit.type == 'item2':
                player.item2 += 1
            if hit.type == 'item3':
                player.item3 += 1
        hits = pygame.sprite.spritecollide(player2, items, True)  # 9. 플레이어2 - 아이템
        for hit in hits:
            score += random.randrange(20, 40)
            if hit.type == 'item1':
                player2.item1 += 1
            if hit.type == 'item2':
                player2.item2 += 1
            if hit.type == 'item3':
                player2.item3 += 1

        # 레벨 4에서의 추가적인 충돌 체크
        if level == 4:
            hits = pygame.sprite.spritecollide(boss, bullets, True)  # 9. 보스 - 플레이어 총알
            for hit in hits:
                score += 40
                boss.HP -= 6
            hits = pygame.sprite.spritecollide(player, boss_bullets, True)  # 10. 플레이어1 - 보스 총알
            for hit in hits:
                player.HP -= 15
                if player.HP <= 0 and player.lives > 0:
                    player.HP = 100
                    player.lives -= 1
                elif player.HP <= 0 and player.lives == 0:
                    player.HP = 0
                    player.lives = 0
            hits = pygame.sprite.spritecollide(player2, boss_bullets, True)  # 11. 플레이어2 - 보스 총알
            for hit in hits:
                player2.HP -= 15
                if player2.HP <= 0 and player2.lives > 0:
                    player2.HP = 100
                    player2.lives -= 1
                elif player2.HP <= 0 and player2.lives == 0:
                    player2.HP = 0
                    player2.lives = 0
            hits = pygame.sprite.spritecollide(boss, item3_bullets, True)  # 12. 보스 - 아이템3
            for hit in hits:
                boss.HP -= 20

            # 13. 보스 - 플레이어1, 플레이어2
            if player.rect.right >= boss.rect.left and player.rect.left <= boss.rect.right \
                    and player.rect.bottom >= boss.rect.top and player.rect.top <= boss.rect.bottom:
                player.rect.top = 270
            if player2.rect.right >= boss.rect.left and player2.rect.left <= boss.rect.right \
                    and player2.rect.bottom >= boss.rect.top and player2.rect.top <= boss.rect.bottom:
                player2.rect.top = 270

        # 플레이어 사망
        if player.lives == 0 and player.HP == 0:
            all_sprites.remove(player)
        if player2.lives == 0 and player2.HP == 0:
            all_sprites.remove(player2)

        # 레벨 1~3 게임 종료
        if (player.lives == 0 and player.HP == 0) and \
                (player2.lives <= 0 and player2.HP == 0):
            game = False
            gameover(now)
            saveranking(score)
            score = 0  # 점수, 레벨, 인벤토리 위치 표시 초기화
            level = 1
            p1_inventory_key = 4
            p2_inventory_key = 1

            level1_bgm = True
            level2_bgm = True
            level3_bgm = True
            level4_bgm = True

        # 보스전 게임 종료
        if level == 4 and boss.HP < 0:
            boss_die_sound.play()
            all_sprites.remove(player)
            all_sprites.remove(player2)
            all_sprites.remove(boss)

            game = False

            pygame.mixer.init()
            pygame.mixer.music.load('music.mp3')
            pygame.mixer.music.play(-1)

            endingCredit(now)
            saveranking(score)

            level1_bgm = True
            level2_bgm = True
            level3_bgm = True
            level4_bgm = True

            score = 0  # 점수, 레벨, 인벤토리 위치 표시 초기화
            level = 1
            p1_inventory_key = 4
            p2_inventory_key = 1

    ##3. 추가 기능
    # 게임 종료시 다시 메뉴 출력
    if game == False:
        menu = True

    # 레벨마다 다른 배경그림
    if level == 1:
        screen.blit(background_img1, background_rect)
    elif level == 2:
        screen.blit(background_img2, background_rect)
    elif level == 3:
        screen.blit(background_img3, background_rect)
    elif level == 4:
        screen.blit(background_img4, background_rect)

    ##4. 업데이트 & 그리기
    # 화면에 그리기
    all_sprites.draw(screen)

    draw_text(screen, "SCORE: ", 20, WIDTH / 2 - 30, 30, BLACK)
    draw_text(screen, str(score), 20, WIDTH / 2 + 30, 30, BLACK)
    draw_HP(screen, 15, 15, player2.HP, BLUE)
    draw_HP(screen, WIDTH - 135, 15, player.HP, RED)

    if level == 4:
        draw_HP(screen, boss.rect.x + 30, boss.rect.top - 20, boss.HP, YELLOW)

    draw_inventory(p1_inventory_key, p2_inventory_key)

    draw_item(player.item1, player.item2, player.item3, WIDTH - 15 - shieldWIDHT, HEIGHT - 55)  # player1 아이템 그리기
    draw_item(player2.item1, player2.item2, player2.item3, 15, HEIGHT - 55)  # player2 아이템 그리기
    draw_text(screen, str(player.item1), 15, WIDTH - 100, HEIGHT - 32, BLACK)  # player1 아이템 개수 표시
    draw_text(screen, str(player.item2), 15, WIDTH - 60, HEIGHT - 32, BLACK)
    draw_text(screen, str(player.item3), 15, WIDTH - 20, HEIGHT - 32, BLACK)
    draw_text(screen, str(player2.item1), 15, 50, HEIGHT - 32, BLACK)  # plyaer2 아이템 개수 표시
    draw_text(screen, str(player2.item2), 15, 90, HEIGHT - 32, BLACK)
    draw_text(screen, str(player2.item3), 15, 130, HEIGHT - 32, BLACK)

    draw_lives(screen, 20, player2.lives, min_player1)
    draw_lives(screen, WIDTH - 135, player.lives, min_player2)

    draw_text(screen, "LEVEL:  ", 20, WIDTH / 2 - 30, 5, BLACK)
    draw_text(screen, str(level), 20, WIDTH / 2 + 30, 5, BLACK)

    if level < 4:
        draw_text(screen, "TIME:    ", 20, WIDTH / 2 - 30, 55, BLACK)
        if level_time - (now - start_time) > 4000:  # 남은 시간이 4초 이상이면 검정색으로 시간 표시
            draw_text(screen, str("%0.2f" % float((level_time - (now - start_time)) / 1000)), 20, WIDTH / 2 + 30, 55,
                      BLACK)
        else:  # 남은 이간이 4초 이하라면 빨간색 굵은 글씨로 시간 표시
            draw_text(screen, str("%0.2f" % float((level_time - (now - start_time)) / 1000)), 20, WIDTH / 2 + 30, 55,
                      WHITE)
    if level == 4:
        draw_text(screen, "KILL THE BOSS", 22, WIDTH / 2 - 10, 55, BLACK)

    pygame.display.flip()