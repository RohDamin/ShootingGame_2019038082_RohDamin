# def draw_inventory 작성자: 노다민
def draw_inventory(p1_inventory_key, p2_inventory_key):
    inventoryWIDTH = shieldWIDHT / 3
    for i in range(0, 3):
        if i == p2_inventory_key - 1:  # 지정된 키의 색과 두께를 다르게 함
            color = RED
            size = 4
        else:
            color = BLACK
            size = 2
        outline_rect2 = pygame.Rect(15 + inventoryWIDTH * i, HEIGHT - 55, inventoryWIDTH, inventoryWIDTH)  # 인벤토리 3칸 그리기
        pygame.draw.rect(screen, color, outline_rect2, size)

    for i in range(0, 3):
        if i == p1_inventory_key - 4:
            color = RED
            size = 4
        else:
            color = BLACK
            size = 2
        outline_rect2 = pygame.Rect(865 + inventoryWIDTH * i, HEIGHT - 55, inventoryWIDTH,
                                    inventoryWIDTH)  # 인벤토리 3칸 그리기
        pygame.draw.rect(screen, color, outline_rect2, size)
