# fuction1.py
#1) 함수를 정의

retValue=0

def setValue(newValue):
    x=newValue
    print("내부:", x)

#2) 함수를 호출
retValue = setValue(5)
print(retValue)


def swap(x,y):
    return y,x

#호출
retValue = swap(4,5)
print( retValue)
print(type(retValue))
print( retValue[0], retValue[1])

#디버깅을 위한 함수(교집합)
def intersect(prelist, postlist):
    result=[]
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result

#호출
print( intersect("HAM","SPAM"))