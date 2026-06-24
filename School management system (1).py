import mysql.connector as a
conn=a.connect(host='localhost',user='root',passwd='1234')
mycur=conn.cursor()

#creating a database.

q1='create database if not exists SCHOOL_MANAGEMENT_SYS;'
mycur.execute(q1)

q2='show databases;'
mycur.execute(q2)

print('-------------------DATABASES------------------')

for i in mycur:
    print(i)

print("-----------------------------NO OF TABLES-----------------------")

q3='use SCHOOL_MANAGEMENT_SYS;'
mycur.execute(q3)
'''
#To create tables.


q4="create table if not exists students(AdmNo int primary key,Name char(20),Rollno int,Class char(20),address char(30));"
mycur.execute(q4)

q5='create table if not exists teacher(T_id int primary key,TName char(20),Subject char(20),phone int,salary float);'
mycur.execute(q5)

q6='create table if not exists cl_attendance(DATE date,sClass char(20),absent int);'
mycur.execute(q6)

q7='create table if not exists Fees(sName char(20),sClass char(20),srollno int,sMonth char(30), Amt_paid float);'
mycur.execute(q7)

q8='create table if not exists Salary(tName char(20),tMonth char(20),sal_paid float);'
mycur.execute(q8)

q9='show tables;'
mycur.execute(q9)

for i in mycur:
    print(i)

uq='Alter table teacher Modify phone varchar(20);'
mycur.execute(uq)
# examples of insertion of data in tables students,teacher,cl_attendance,Fees and salary.

q10='insert into students values(1001,"Aditya",2,"XII","Delhi");'
mycur.execute(q10)

q11='insert into teacher values(2,"Sudhir","Maths","1111111112",60000);'
mycur.execute(q11)

q12='insert into cl_attendance values("2023-12-17","XII",11);'
mycur.execute(q12)

q13='insert into Fees values("Aditya","XII",2,"December",18000);'
mycur.execute(q13)


q14='insert into Salary values("sudhir","December",60000);'
mycur.execute(q14)

conn.commit()
'''




def addstudents():
    AdmNo=int(input("Enter the admission no. of student:"))
    Name=input("Enter the name of student:")
    Rollno=int(input("Enter the Rollno of student:"))
    Class=input("Enter the class of student:")
    address=input("Enter the address of student:")
    data=(AdmNo,Name,Rollno,Class,address)
    sql1='insert into students values(%s,%s,%s,%s,%s);'
    mycur.execute(sql1,data)
    conn.commit()
    print("Data entered succesfully..........")
    schoolmain()

def cls_attendance():
    DATE=input("Enter date:")
    sClass=input("Enter the class of student:")
    absent=int(input("Enter the no.of students absent:"))
    data=(DATE,sClass,absent)
    sql2='insert into cl_attendance values(%s,%s,%s);'
    mycur.execute(sql2,data)
    conn.commit()
    print("Data succesfully entered.......")
    schoolmain()

def addteachers():
    T_id=int(input("Enter the teacher id:"))
    TName=input("Enter the name of teacher:")
    Subject=input("Enter the subject of teacher:")
    phone=int(input("Enter the phone no.:"))
    salary=int(input("Enter the salary:"))
    data=(T_id,TName,Subject,phone,salary)
    sql3='insert into teacher values(%s,%s,%s,%s,%s);'
    mycur.execute(sql3,data)
    conn.commit()
    print("Data entered successfully......")
    schoolmain()

def submfees():
    sName=input("Enter the name of students:")
    sClass=input("Enter the class of student:")
    srollno=int(input("Enter the rollno. of student:"))
    sMonth=input("Enter the month:")
    Amt_paid=int(input("Enter the fees paid by student:"))
    data=(sName,sClass,srollno,sMonth,Amt_paid)
    sql4='insert into Fees values(%s,%s,%s,%s,%s);'
    mycur.execute(sql4,data)
    conn.commit()
    print("Data entered successfully....")
    schoolmain()

def pysalary():
    tname=input("Enter the name of teacher:")
    tmonth=input("Enter the month:")
    sal_paid=input("Enter the salary paid to the taecher:")
    data=(tname,tmonth,sal_paid)
    sql5='insert into Salary values(%s,%s,%s);'
    mycur.execute(sql5,data)
    conn.commit()
    print("Data entered successfully....")
    schoolmain()

def diclass():
    cl=input("Enter the class:")
    data=(cl,)
    sql6="select * from students where Class=%s"
    mycur.execute(sql6,data)
    d=mycur.fetchall()
    for i in d:
        print("AdmNo:",i[0])
        print("Name:",i[1])
        print("Rollno:",i[2])
        print("Class:",i[3])
        print("Address:",i[4])
        print("DATA SUCCESSFULLY SHOWN")
    print("...............................")
    schoolmain()

def distudents():
    Class=input("class:")
    sql7="select * from students;"
    mycur.execute(sql7)
    m=mycur.fetchall()
    for i in m:
        print("AdmNo:",i[0],"Name:",i[1],"Rollno:",i[2],"Class:",i[3],"address:",i[4])
    schoolmain()

def diteachers():
    sql8="select * from teacher;"
    mycur.execute(sql8)
    z=mycur.fetchall()
    for i in z:
        print("T_id:",i[0],"TName:",i[1],"Subject:",i[2],"phone:",i[3],"salary:",i[4])
    schoolmain()

def remst():
    c=input("Enter the class")
    r=int(input("enter the roll no:"))
    data=(c,r)
    sql9='delete from students where Class=%s and Rollno=%s;'
    mycur.execute(sql9,data)
    conn.commit()
    print("data updated.......")
    schoolmain()

def remteach():
    n=input("enter the name of teacher:")
    tid=int(input("enter the teacher id:"))
    data=(n,tid)
    sql10='delete from teacher where TName=%s and T_id=%s;'
    mycur.execute(sql10,data)
    conn.commit()
    print("Data has been updated.....")
    schoolmain()
    

    

def schoolmain():
    print("""     ................KALKA PUBLIC SCHOOL...............

            1.ADD STUDENT           2.CLASS ATTENDANCE
            3.ADD TEACHER           4.SUBMIT FEES
            5.PAY SALARY            6.DISPLAY CLASS
            7.DISPLAY STUDENTS      8.DISPLAY TEACHERS
            9.REMOVE STUDENTS       10.REMOVE TEACHERS
         .....................................................................   
""")
    
    choice=input("ENTER THE TASK:")
    if(choice=='1'):
        addstudents()
    elif(choice=='2'):
        cls_attendance()
    elif(choice=='3'):
        addteachers()
    elif(choice=='4'):
        submfees()
    elif(choice=='5'):
        pysalary()
    elif(choice=='6'):
        diclass()
    elif(choice=='7'):
        distudents()
    elif(choice=='8'):
        diteachers()
    elif(choice=='9'):
        remst()
    elif(choice=='10'):
        remteach()
    else:
        print("Choice is wrong,try another...")



def pswd():
    passw=input("Enter the password:")
    if passw=="Abhishek":
        schoolmain()
    else:
        print("wrong pass.. try again")
pswd()
    



