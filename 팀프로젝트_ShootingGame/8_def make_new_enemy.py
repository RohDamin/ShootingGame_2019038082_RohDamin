# def make_new_enemy 작성자: 노다민
def make_new_enemy(level):
    enemy_element = Enemy(level)
    all_sprites.add(enemy_element)
    enemys.add(enemy_element)