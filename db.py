import mysql.connector
a=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='mpbase'
)
cursor=a.cursor(buffered=True)

def login(data):
    print(data)
    try:
        cursor.execute("select * from adlogin where uname=%s and pas=%s",data)
        a.commit()
        return cursor.fetchone()
    except:
        return False
# # c='rohan'
# a.rollback()
# cursor.execute('DELETE FROM car_data WHERE customer_name = %s',(c,))
# a.commit()
# b=cursor.fetchall()
# print('YES')

def addusr(data):
    # print(data)
    # try:
        cursor.execute("insert into students(name,rollno,class,address) values(%s,%s,%s,%s)",data)
        print(0)
        cursor.execute("select sid from students where name=%s",(data[0],))
        print(0)
        a.commit()
        return cursor.fetchone()
    # except:
    #     return False
    
def getusr():
    # print(data)'
    try:
        cursor.execute("select * from students")
        a.commit()
        return cursor.fetchall()
    except:
        return False
    
def singleusr(data):
    # print(data)'
    try:
        cursor.execute("select * from students where sid=%s",(data,))
        a.commit()
        return cursor.fetchone()
    except:
        return False
    
def update(data):
    # print(data)
    # try:
        cursor.execute("update students set name=%s, rollno=%s, class=%s, address=%s where students.sid=%s",data)
        a.commit()
        return True
    # except:
    #     return False

def existing(data):
    # print(data)
    try:
        cursor.execute("select * from students",data)
        a.commit()
        return cursor.fetchall()
    except:
        return False
    
def delete(data):
    # print(data)
    try:
        cursor.execute("delete from students where sid=%s",data)
        a.commit()
        return True
    except:
        return False

def faceid(data):
    print(data)
    try:
        cursor.execute("insert into idss(sid,name,id) values(%s,%s,%s)",data)
        print("face id added")
        a.commit()
        return True
    except:
        return False
    
def fcusr(data):
    # print(data)'
    try:
        cursor.execute("select * from idss where sid=%s",(data,))
        a.commit()
        return cursor.fetchone()
    except:
        return False
    
    
def attn(data):

    # print(data)
    try:
        cursor.execute("select * from attendance",data)
        a.commit()
        return cursor.fetchall()
    except:
        return False
    
def attnid(data):
    # print(data)
    # try:
        cursor.execute("insert into attendance(sid,name,atten,date) values(%s,%s,%s,%s)",data)
        a.commit()
        return True
    # except:
    #     return False

def getatt(datag):
    print(datag)
    try:
        cursor.execute("select * from attendance where sid=%s",datag)
        a.commit()
        # print(cursor.fetchall())
        return cursor.fetchone()
    except:
        print(False)
   

def updattn(datau):
    print("sql data-",datau)
    try:
        cursor.execute("update attendance set atten=%s, date=%s where attendance.sid=%s",datau)
        a.commit()
        return True
    except:
        return False

