import mysql.connector as connection
import random
comm = connection.connect( host= "127.0.0.1", user = "root", password= "Kkmontana1@", database= "sqi_vote")
cursor=comm.cursor()

def data_science():
    
    student_id = random.randrange(1001, 1909)
    student_name = input("student_name: ")
    gender = input("gender: ")
    password = input("password: ")
    querry="insert into data_science(student_id , student_name , gender, password, voting_status, fin_voting_status ) values(%s, %s, %s, %s, %s, %s)"
    val=[student_id , student_name , gender, password, "Not Voted", "Not Voted" ]
    cursor.execute(querry, val)
    comm.commit()
    query2 = "insert into voting_status(student_id, student_name, pres_status, fin_status) values(%s, %s,%s, %s)"
    val2 = (student_id, student_name, "Not Voted", "Not Voted")
    cursor.execute(query2, val2)
    comm.commit()
    print(f"you have successfully registered and your student id is {student_id} ")
    

def web_development():
    
    student_id = random.randrange(1001, 1909)
    student_name = input("student_name: ")
    gender = input("gender: ")
    password = input("password: ")
    querry="insert into web_development(student_id , student_name , gender, password, voting_status, fin_voting_status ) values(%s, %s, %s, %s, %s, %s)"
    val=[student_id , student_name , gender, password, "Not Voted", "Not Voted"]
    cursor.execute(querry, val)
    comm.commit()
    query2 = "insert into voting_status(student_id, student_name, pres_status, fin_status) values(%s, %s,%s, %s)"
    val2 = (student_id, student_name, "Not Voted", "Not Voted")
    cursor.execute(query2, val2)
    comm.commit()
    print(f"you have successfully registered and your student id is {student_id} ")


def ui_ux():
    
    student_id = random.randrange(1001, 1909)
    student_name = input("student_name: ")
    gender = input("gender: ")
    password = input("password: ")
    querry="insert into ui_ux(student_id , student_name , gender, password, voting_status, fin_voting_status ) values(%s, %s, %s, %s, %s, %s)"
    val=[student_id , student_name , gender, password, "Not Voted", "Not Voted" ]
    cursor.execute(querry, val)
    comm.commit()
    query2 = "insert into voting_status(student_id, student_name, pres_status, fin_status) values(%s, %s,%s, %s)"
    val2 = (student_id, student_name, "Not Voted", "Not Voted")
    cursor.execute(query2, val2)
    comm.commit()
    print(f"you have successfully registered and your student id is {student_id} ")

def javascript():
    student_id = random.randrange(1001, 1909)
    student_name = input("student_name: ")
    gender = input("gender: ")
    password = input("password: ")
    querry="insert into ui_ux(student_id , student_name , gender, password, voting_status, fin_voting_status ) values(%s, %s, %s, %s, %s, %s)"
    val=[student_id , student_name , gender, password, "Not Voted", "Not Voted" ]
    cursor.execute(querry, val)
    comm.commit()
    query2 = "insert into voting_status(student_id, student_name, pres_status, fin_status) values(%s, %s,%s, %s)"
    val2 = (student_id, student_name, "Not Voted", "Not Voted")
    cursor.execute(query2, val2)
    comm.commit()
    print(f"you have successfully registered and your student id is {student_id} ")

def artificial_intelligence():
    student_id = random.randrange(1001, 1909)
    student_name = input("student_name: ")
    gender = input("gender: ")
    password = input("password: ")
    querry="insert into ui_ux(student_id , student_name , gender, password, voting_status, fin_voting_status ) values(%s, %s, %s, %s, %s, %s)"
    val=[student_id , student_name , gender, password, "Not Voted", "Not Voted"]
    cursor.execute(querry, val)
    comm.commit()
    query2 = "insert into voting_status(student_id, student_name, pres_status, fin_status) values(%s, %s,%s, %s)"
    val2 = (student_id, student_name, "Not Voted", "Not Voted")
    cursor.execute(query2, val2)
    comm.commit()
    print(f"you have successfully registered and your student id is {student_id} ")

def graphic_design():
    student_id = random.randrange(1001, 1909)
    student_name = input("student_name: ")
    gender = input("gender: ")
    password = input("password: ")
    querry="insert into ui_ux(student_id , student_name , gender, password, voting_status, fin_voting_status ) values(%s, %s, %s, %s, %s, %s)"
    val=[student_id , student_name , gender, password, "Not Voted", "Not Voted"]
    cursor.execute(querry, val)
    comm.commit()
    query2 = "insert into voting_status(student_id, student_name, pres_status, fin_status) values(%s, %s,%s, %s)"
    val2 = (student_id, student_name, "Not Voted", "Not Voted")
    cursor.execute(query2, val2)
    comm.commit()
    print(f"you have successfully registered and your student id is {student_id} ")

def data_analytics():
    student_id = random.randrange(1001, 1909)
    student_name = input("student_name: ")
    gender = input("gender: ")
    password = input("password: ")
    querry="insert into ui_ux(student_id , student_name , gender, password, voting_status, fin_voting_status ) values(%s, %s, %s, %s, %s, %s)"
    val=[student_id , student_name , gender, password, "Not Voted", "Not Voted"]
    cursor.execute(querry, val)
    comm.commit()
    query2 = "insert into voting_status(student_id, student_name, pres_status, fin_status) values(%s, %s,%s, %s)"
    val2 = (student_id, student_name, "Not Voted", "Not Voted")
    cursor.execute(query2, val2)
    comm.commit()
