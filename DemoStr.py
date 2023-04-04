#DemoStr.py

#print(dir(str))

strA = "python is very powerful"
strB = "파이썬은 강력해"
print( len(strA))
print( len(strB))
print( strA.capitalize())
print( strA.count("p"))
print( strA.count("p",7))
print( strA.startswith("python"))
print( strA.endswith("ful"))

print("MBC2580".isalnum()) #숫자와 문자로만구성?
print("MBC:2580".isalnum()) #특수문자존재
print("2580".isalnum())

print("---문자열 공백제거---")
u= "<<< spam and ham >>>"
print(u)
result = u.strip("<> ")
print(result)

lst = result.split()
print(lst)
print("----하나로합치기 ---")
print(":)".join(lst))
