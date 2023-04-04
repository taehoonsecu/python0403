#DemoForamt.py

# strURL = "www.credu.com/?page" +1
# print(strURL)

strURL = "www.credu.com/?page" +str(1)
print(strURL)

for x in range(1,6):
    print(x, "*",x, "=", x*x)

print("---정렬지정---")
for x in range(1,6):
    print(x, "*",x, "=", str(x*x).rjust(3))


for x in range(1,6):
    print(x, "*",x, "=", str(x*x).zfill(5))

print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))
print("{0:,}".format(1500000))

#파일에 쓰기
f=open("c:\\work\\demo.txt","wt",encoding="utf-8")

f.write("처음에는 \n두번째라인\n세번째라인 \n")
f.close()

#파일읽기
f=open("c:\\work\\demo.txt","rt",encoding="utf-8")

result = f.read()

print(result)

print(f.tell())
#다시 처음으로 파일포인터를 이동
f.seek(0)
lst = f.readlines()
print(lst)
f.seek(0)

#코드로 보정 (엔터 없기)
print(f.readline(), end="")
print(f.tell())
print(f.readline(), end="")
print(f.tell())

f.close()