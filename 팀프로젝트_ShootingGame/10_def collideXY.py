# def collideXY 작성자: 노다민
def collideXY(mouseX, mouseY, rect, x, y):  # 중앙에 위치하지 않은 버튼 클릭 확인용
    rectX = WIDTH / 2 - rect.width / 2

    if (mouseX >= x and mouseX <= x + rect.width and mouseY >= y and mouseY <= y + rect.height):
        return True
    else:
        return False