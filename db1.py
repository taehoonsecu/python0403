#db1.py

import sqlite3

#메모리에 임시로 작업
#con = sqlite3.connect(":memory:")

#실제 파일에저장
con = sqlite3.connect("c:\\work\\temp.db")
cur = con.cursor()
cur.execute("create table if not exists PhoneBook"
            + "(id integer primary key autoincrement,"
            + "name text, phoneNum text);")

#1건 입력
cur.execute("insert into PhoneBook (name, phoneNum) values"
            + "('홍길동','010-1111');")
#외부에서 입력파라메터로 받기
name="이순신"
phoneNumber = "010-222"
cur.execute("insert into PhoneBook (name, phoneNum) values"
            + "(?,?);", (name,phoneNumber))

#다중의 행을 입력
datalist= (("박수민", "010-333"), ("최보미", "010-4444"))
cur.executemany("insert into PhoneBook (name, phoneNum) values"
            + "(?,?);", datalist)
#검색
cur.execute("select * from PhoneBook;")
for row in cur:
    #print(row)
    print("{0}, {1}, {2}".format(row[0],row[1],row[2]))

#정상적으로 완료
