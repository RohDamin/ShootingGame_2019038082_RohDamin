stu = [] # 학생들의 정보를 저장

# 1번 : 데이터 추가
def menu1():
    global stu
    s =[]
    s.append(str(input("학과:")))
    s.append(str(input("학번:")))
    s.append(str(input("이름:")))
    s.append(int(input("국어 점수:")))
    s.append(int(input("영어 점수:")))
    s.append(int(input("수학 점수:")))
    s.append(s[3] + s[4] + s[5])  # 총점
    s.append(s[6] / 3)  # 평균
    if s[7] >= 95:
        s.append('A+')
    elif s[7] >= 90:
        s.append('A')
    elif s[7] >= 85:
        s.append('B+')
    elif s[7] >= 80:
        s.append('B')
    elif s[7] >= 75:
        s.append('C+')
    elif s[7] >= 70:
        s.append('C')
    elif s[7] >= 65:
        s.append('D+')
    elif s[7] >= 60:
        s.append('D')
    else:
        s.append('F')
    stu.append(s)
    print("추가되었습니다")

# 2번 : 데이터 검색
def menu2():
    search = str(input("검색하려는 학번 또는 이름: "))
    for i in range(0, len(stu)):
        for j in range(1, 3):
            if search in stu[i][j]:
                print("       학과      학번      이름     국어     영어    수학    총점       평균      학점")
                for k in range(0, 3):
                    print("%10s" % stu[i][k], end="")
                for k in range(3, 7):
                    print("%8d" % stu[i][k], end="")
                print("%10.2f" % stu[i][7], end="")
                print("%10s" % stu[i][8])
                break

# 3번 : 데이터 삭제
def menu3():
    global stu
    remove = str(input("삭제하려는 학번 또는 이름: "))
    for i in range(0, len(stu)):
        if remove in stu[i]:
            del(stu[i])
            print("삭제되었습니다")
            break

# 4번 : 데이터 정렬
def menu4():
    sort = str(input("정렬기준을 입력하십시오(학과/학번): "))
    if sort == '학과':
        stu_sort(0)
    if sort == '학번':
        stu_sort(1)
    print("정렬되었습니다")

def stu_sort(num):
    global stu
    for i in range(0, len(stu) - 1):
        min_index = i
        for j in range(i, len(stu)):
            if stu[min_index][num] > stu[j][num]:
                min_index = j
        stu[i], stu[min_index] = stu[min_index], stu[i]


# 5번 : 데이터 출력
def menu5():
    print("       학과      학번      이름     국어     영어    수학    총점       평균      학점")
    for i in range(0, len(stu)):
        for k in range(0, 3):
            print("%10s" % stu[i][k], end="")
        for k in range(3, 7):
            print("%8d" % stu[i][k], end="")
        print("%10.2f" % stu[i][7], end="")
        print("%10s" % stu[i][8])

# main
while True:
    print("\n1. 데이터 추가")
    print("2. 데이터 검색")
    print("3. 데이터 삭제")
    print("4. 데이터 정렬")
    print("5. 데이터 출력")
    print("0. 종료")

    menu = int(input("메뉴를 선택하세요: "))
    if menu == 1:
        menu1()

    if menu == 2:
        menu2()

    if menu == 3:
        menu3()

    if menu == 4:
        menu4()

    if menu == 5:
        menu5()

    if menu == 0:
        print("프로그램이 종료되었습니다")
        break
