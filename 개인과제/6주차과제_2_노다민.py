import threading
import time

class sumNum:
    sumRange = 0
    sumResult = 0
    def __init__(self, number):
        self.sumRange = number
    def sumNumber(self):
        for i in range(0, self.sumRange+1):
            self.sumResult += i
        print("1+2+3+......+%d = " % self.sumRange, end = "")
        print(self.sumResult)
        time.sleep(0.1)

sum1 = sumNum(1000)
sum2 = sumNum(100000)
sum3 = sumNum(10000000)

th1 = threading.Thread(target=sum1.sumNumber)
th2 = threading.Thread(target=sum2.sumNumber)
th3 = threading.Thread(target=sum3.sumNumber)

th1.start()
th2.start()
th3.start()
