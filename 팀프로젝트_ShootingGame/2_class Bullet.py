# class Bullet 작성자: 노다민
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, type):
        pygame.sprite.Sprite.__init__(self)
        self.image = shot
        self.rect = self.image.get_rect()
        self.rect.centerx = x - 5
        if type == 1:  # 위쪽 총알
            self.rect.bottom = y
            self.speedy = -10
        if type == 2:  # 아래쪽 총알
            self.image = shot2
            self.rect = self.image.get_rect()
            self.rect.centerx = x + 5
            self.rect.top = y
            self.speedy = 6
        if type == 3:
            self.image = pygame.transform.scale(item3_shot, (100, 100))
            self.rect = self.image.get_rect()
            self.rect.bottom = y - 120
            self.rect.centerx = x - 20
            self.speedy = -2

    def update(self):
        self.rect.y += self.speedy
        if self.rect.y < -100 or self.rect.y > HEIGHT + 100:
            self.kill()