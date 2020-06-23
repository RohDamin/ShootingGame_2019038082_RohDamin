# class Player 작성자: 노다민
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.image = pygame.transform.scale(self.image, (70, 80))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedx = 0
        self.speedy = 0
        self.top_shot_delay = 200
        self.bottom_shot_delay = 300
        self.last_shot = pygame.time.get_ticks()
        self.lives = 4
        self.HP = 100
        self.power = 2
        self.power_time = pygame.time.get_ticks()
        self.item1 = 0  # 아이템 개수 저장
        self.item2 = 0
        self.item3 = 0

    def update(self):
        if self.item1 >= 5: self.item1 = 5  # 아이템 하나당 최대 5개까지 보관 가능
        if self.item2 >= 5: self.item2 = 5
        if self.item3 >= 5: self.item3 = 5
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        self.rect.x += self.speedx
        self.rect.y += self.speedy

    def shot_top(self):  # 위쪽으로 총알 발사
        if self.power >= 2 and now - self.power_time > 10000:
            self.power -= 1
            self.power_time = pygame.time.get_ticks()

        if self.HP != 0 or self.lives != 0:
            pnow = pygame.time.get_ticks()
            if pnow - self.last_shot > self.top_shot_delay:
                self.last_shot = pnow
                if self.power == 1:
                    bullet_top = Bullet(self.rect.centerx, self.rect.top, 1)
                    all_sprites.add(bullet_top)
                    bullets.add(bullet_top)
                    shooting_sound.play()
                if self.power == 2:
                    bullet_top1 = Bullet(self.rect.centerx - 6, self.rect.top, 1)
                    bullet_top2 = Bullet(self.rect.centerx + 6, self.rect.top, 1)
                    all_sprites.add(bullet_top1)
                    bullets.add(bullet_top1)
                    all_sprites.add(bullet_top2)
                    bullets.add(bullet_top2)
                    shooting_sound.play()
                if self.power == 3:
                    bullet_top1 = Bullet(self.rect.centerx - 15, self.rect.top, 1)
                    bullet_top2 = Bullet(self.rect.centerx, self.rect.top, 1)
                    bullet_top3 = Bullet(self.rect.centerx + 15, self.rect.top, 1)
                    all_sprites.add(bullet_top1)
                    bullets.add(bullet_top1)
                    all_sprites.add(bullet_top2)
                    bullets.add(bullet_top2)
                    all_sprites.add(bullet_top3)
                    bullets.add(bullet_top3)
                    shooting_sound.play()

    def shot_bottom(self):  # 아래쪽으로 총알 발사
        if self.power >= 2 and now - self.power_time > 10000:  # 10초 동안 아이템2 효과 지속
            self.power -= 1
            self.power_time = pygame.time.get_ticks()

        if self.HP != 0 or self.lives != 0:
            pnow = pygame.time.get_ticks()
            if pnow - self.last_shot > self.bottom_shot_delay:
                self.last_shot = pnow
                if self.power <= 2:
                    bullet_bottom = Bullet(self.rect.centerx, self.rect.bottom, 2)
                    all_sprites.add(bullet_bottom)
                    bullets.add(bullet_bottom)
                    shooting_sound.play()
                if self.power == 3:
                    bullet_bottom1 = Bullet(self.rect.centerx - 8, self.rect.bottom, 2)
                    bullet_bottom2 = Bullet(self.rect.centerx + 8, self.rect.bottom, 2)
                    all_sprites.add(bullet_bottom1)
                    bullets.add(bullet_bottom1)
                    all_sprites.add(bullet_bottom2)
                    bullets.add(bullet_bottom2)
                    shooting_sound.play()

    def item(self, inventory_key):
        if inventory_key == 1 and self.item1 != 0:
            self.item1 -= 1
            if self.HP >= 50:
                self.HP = 100
            else:
                self.HP += 50
        if inventory_key == 2 and self.item2 != 0:
            self.item2 -= 1
            if self.power < 3:
                self.power += 1
        if inventory_key == 3 and self.item3 != 0:
            self.item3 -= 1
            bullet_item3 = Bullet(self.rect.centerx, self.rect.bottom, 3)
            all_sprites.add(bullet_item3)
            item3_bullets.add(bullet_item3)
            item3_shooting_sound.play()