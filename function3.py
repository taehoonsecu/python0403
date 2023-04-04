# function3.py
lst=[1,2,3,4,5,6,7,8,9,10]

for i in lst:
    if i>5:
        break   
    print("Item:{0}".format(i))


print("---contitnue---")

for i in lst:
    if i%2==0:
        continue   
    print("Item:{0}".format(i))


print("---수열---")

print(list(range(10)))
print(list(range(10,0,-1)))
print(list(range(2000,2024)))

for i in range(5):
    print(i)

print("---리스트컴프리헨션---")
lst = list(range(1,11))
print( [i**2 for i in lst if i>5])

tp = ("apple", "ornage", "kiwi")
print([len(i) for i in tp])

d = {100:"apple", 200:"kiwi", 300:"banana"}
print( [v.upper() for v in d.values()])


print("---filter()함수---")
lst=[10,25,30]

def getBiggerThan20(i):
    return i>20

iterL = filter(getBiggerThan20,lst)
for i in iterL:
    print(i)

print("---람다함수사용---")
iterL = filter(lambda x:x>20, lst)
for i in iterL:
    print(i)

print([ i for i in lst if i>20])

