# class1.py
#1) 클래스형식 정의
class Person:
    #초기화메소드
    def __init__(self):
        self.name = "default name"
    def print(self):
        print("My name is {0}".format(self.name))

#2)인스턴스 생성
p1 = Person()
p2 = Person()
#3)메서드 호출
p1.print()
p2.name="전우치"
p2.print()



