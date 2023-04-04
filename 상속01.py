
#부모클래스 정의(Super class)
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))
    def working(self):
        print("현재작업중")
    def sleeping(self):
        print("현재휴식중")

#자식 클래스 정의(Sub class):대학생
class Student(Person):
    #재정의
    def __init__(self, name, phoneNumber, subject, studentID):
        Person.__init__(self,name,phoneNumber)
        self.subject = subject
        self.studentID = studentID
    #상속받고 덮어쓰기(재정의)
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, 
            self.phoneNumber))
        print("Info(Name:{0}, Phone Number: {1})".format(self.subject, 
            self.studentID))

p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")

p.printInfo()
s.printInfo()
s.working()
s.sleeping()


