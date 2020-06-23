# def collide 작성자: 노다민
def collide(mouseX, mouseY, rect, y):  # 중앙에 위치한 버튼 클릭 확인용
    rectX = WIDTH / 2 - rect.width / 2

    if (mouseX >= rectX and mouseX <= rectX + rect.width and mouseY >= y and mouseY <= y + rect.height):
        return True
    else:
        return False