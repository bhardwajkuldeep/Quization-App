import mysql.connector as mysql
import xlrd

loc=("..\Quiz_App\Resources/Questions.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
n = sheet.nrows

conn = mysql.connect(host='localhost', user='root', password='12345')
cursor = conn.cursor()
cursor.execute("drop database if exists quizdb")
cursor.execute("create database quizdb")
cursor.execute("use quizdb")
cursor.execute("drop table if exists Questions")
q = "create table questions(QID int, qstn text, opA text, opB text, opC text, opD text, ans int)"
cursor.execute(q)
cursor.execute("drop table if exists reg")
rr = "create table reg(name text(15) NOT NULL, lname text(15) NOT NULL, email text(30) NOT NULL, uname text(15) NOT NULL, p text NOT NULL, score int(2) NOT NULL)"
cursor.execute(rr)

print("Congratulation, Database and Tables are created Successfully.")


#Code to add rows
for i in range(1,n):
    lst = sheet.row_values(i)
    q2 = "insert into questions(QID, qstn, opA, opB, opC, opD, ans) values('%d','%s','%s','%s','%s','%s','%d')"
    val = (int(lst[0]), lst[1], lst[2], lst[3], lst[4], lst[5], lst[6])
    cursor.execute(q2 % val)
    conn.commit()
print("Congratulation, Questions are Added into the Database Successfully.")

cursor.close()
conn.close()
