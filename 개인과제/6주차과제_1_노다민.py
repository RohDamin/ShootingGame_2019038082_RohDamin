# 클래스 정의 #
class Student:
    def __init__(self, major, number, name, kor, eng, math):
        self.major = major
        self.number = number
        self.name = name
        self.sub_kor = kor
        self.sub_eng = eng
        self.sub_math = math
        self.totalScore = self.sub_kor + self.sub_eng + self.sub_math
        self.aver = self.totalScore / 3
        if self.aver >= 95:
            self.Gpa = 'A+'
        elif self.aver >= 90:
            self.Gpa = 'A'
        elif self.aver >= 85:
            self.Gpa = 'B+'
        elif self.aver >= 80:
            self.Gpa = 'B'
        elif self.aver >= 75:
            self.Gpa = 'C+'
        elif self.aver >= 70:
            self.Gpa = 'C'
        elif self.aver >= 65:
            self.Gpa = 'D+'
        elif self.aver >= 60:
            self.Gpa = 'D'
        else:
            self.Gpa = 'F'

    def __lt__(self, other):
        return self.number < other.number

    def printdata(self): #출력 메서드
        print("%10s" % self.major, end="")
        print("%10s" % self.number, end="")
        print("%10s" % self.name, end="")
        print("%8d" % self.sub_kor, end="")
        print("%8d" % self.sub_eng, end="")
        print("%8d" % self.sub_math, end="")
        print("%10.2f" % self.totalScore, end="")
        print("%10.2f" % self.aver, end="")
        print("%8s" % self.Gpa)

    def searchdata(self, search): #검색 메서드 : 찾는 값이 존재하면 -1 리턴
        if search == self.number or search == self.name:
            return -1


# 전역변수 선언 #
stu = []


# 함수 선언 #
# 1번: 데이터 추가
def menu1():
    global stu
    major = str(input("학과:"))
    number = str(input("학번:"))
    name = str(input("이름:"))
    kor = int(input("국어 점수:"))
    eng = int(input("영어 점수:"))
    math = int(input("수학 점수:"))
    stu.append(Student(major, number, name, kor, eng, math))
    print("추가되었습니다")

# 2번: 데이터 검색
def menu2():
    search = str(input("검색하려는 학번 또는 이름: "))
    for i in range(0, len(stu)):
        if stu[i].searchdata(search) == -1: # -1이 리턴되면 값 출력
            print("       학과      학번      이름     국어     영어    수학    총점       평균      학점")
            stu[i].printdata()

# 3번: 데이터 삭제
def menu3():
    global stu
    search = str(input("삭제하려는 학번 또는 이름: "))
    for i in range(0, len(stu)):
        if stu[i].searchdata(search) == -1: # -1이 리턴되면 값 삭제
            del stu[i]
            print("삭제되었습니다")
            break

# 4번: 데이터 정렬
def menu4():
    global stu
    for i in range(0, len(stu) - 1):
        min_index = i
        for j in range(i, len(stu)):
            if stu[min_index] > stu[j]: #학번으로 정렬
                min_index = j
        stu[i], stu[min_index] = stu[min_index], stu[i]
    print("정렬되었습니다")

# 5번: 데이터 출력
def menu5():
    print("       학과      학번      이름     국어     영어    수학    총점       평균      학점")
    for i in range(0, len(stu)):
        stu[i].printdata()


# Main #
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