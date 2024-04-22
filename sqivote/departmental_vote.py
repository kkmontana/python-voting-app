import mysql.connector as connection
comm= connection.connect (host = "127.0.0.1", user = "root", password = "Kkmontana1@", database = "sqi_vote")
import time
cursor=comm.cursor()




def voters():
    
    student_id = int(input("enter your student id: "))
    querry= "select * from voting_status where student_id = %s"
    val = (student_id,)
    cursor.execute(querry, val)
    result = cursor.fetchone()

    print("Enter 1 to vote for President and 2 to vote for financial secretary")
    user_resp = input(">> ")
    if user_resp == "1":
        if result[2] == "Not Voted":
            print("""presidential canditate are 1: olusegun obasanjo , 2: goodluck johnatan """)
            decision = input("Enter candidate's name ").strip().lower()
            if decision == "goodluck johnatan":
                query = "SELECT * from presidential where candidate_name = %s"
                val = (decision,)
                cursor.execute(query, val)
                result = cursor.fetchone()
                new_vote = result[1] +  1
                query2 = "UPDATE presidential SET total_vote = %s where candidate_name = %s"
                val2 = (new_vote, decision)
                cursor.execute(query2, val2)
                comm.commit()
                query3 = "UPDATE voting_status set pres_status = %s where student_id = %s"
                val3 = ("Voted", student_id)
                cursor.execute(query3, val3)
                comm.commit()
                print("You have successfully voted")
            elif decision == "olusegun obasanjo":
                query = "SELECT * from presidential where candidate_name = %s"
                val = (decision,)
                cursor.execute(query, val)
                result = cursor.fetchone()
                new_vote = result[1] +  1
                query2 = "UPDATE presidential SET total_vote = %s where candidate_name = %s"
                val2 = (new_vote, decision)
                cursor.execute(query2, val2)
                comm.commit()
                query3 = "UPDATE voting_status set pres_status = %s where student_id = %s"
                val3 = ("Voted", student_id)
                cursor.execute(query3, val3)
                comm.commit()
                print("You have successfully voted")
            else: 
                print("wrong input")
                voters()
            voters()    
        else:
            print("You have already voted. Go home")
            
    elif user_resp == "2":
        if result[3] == "Not Voted":
            print("""financial secetary are  1: nelson wike, 2: bukola saraki """)
            decision = input("Enter candidate's name ").strip().lower()
            if decision == "bukola saraki":
                query = "SELECT * from secretary where candidate_name = %s"
                val = (decision,)
                cursor.execute(query, val)
                result = cursor.fetchone()
                new_vote = result[1] +  1
                query2 = "UPDATE secretary SET total_vote = %s where candidate_name = %s"
                val2 = (new_vote, decision)
                cursor.execute(query2, val2)
                comm.commit()
                query3 = "UPDATE voting_status set fin_status = %s where student_id = %s"
                val3 = ("Voted", student_id)
                cursor.execute(query3, val3)
                comm.commit()
                print("You have successfully voted")
            elif decision == "nelson wike":
                query = "SELECT * from secretary where candidate_name = %s"
                val = (decision,)
                cursor.execute(query, val)
                result = cursor.fetchone()
                new_vote = result[1] +  1
                query2 = "UPDATE secretary SET total_vote = %s where candidate_name = %s"
                val2 = (new_vote, decision)
                cursor.execute(query2, val2)
                comm.commit()
                query3 = "UPDATE voting_status set fin_status = %s where student_id = %s"
                val3 = ("Voted", student_id)
                cursor.execute(query3, val3)
                comm.commit()
                print("You have successfully voted")
            else: 
                print("wrong input")
                voters()
            voters()    
            
        else:
            print("You have already voted. Go home")

def winner():
    print("do you still have voters that wants to vote or you want to count the general vote , \npress 1 to keep voing or \npress 2 to count the general vote ")
    response = input(">>>: ")
    if response == "1":
        voters()
    elif response == "2":
        query1 = "select * from presidential where candidate_name = %s"
        val1= ("olusegun obasanjo" ,)
        cursor.execute(query1, val1)
        result1 = cursor.fetchone()
        # score = result1[1]
        comm.commit()
        query2 = "select * from presidential where candidate_name = %s"
        val2= ("goodluck johnatan" ,) 
        cursor.execute(query2, val2)
        result2= cursor.fetchone()
        comm.commit()
        query3 = "select * from secretary where candidate_name = %s"
        val3= ("bukola saraki" ,)
        cursor.execute(query3, val3)
        result3= cursor.fetchone()
        comm.commit()
        query4 = "select * from secretary where candidate_name = %s"
        val4= ("nelson wike" ,) 
        cursor.execute(query4, val4)
        result4= cursor.fetchone()
        comm.commit()
        if result1[1] > result2[1] and result3[1] > result4[1]:
            print(F"congratulations {result1[0]} and  {result3[0]}   you have the total vote of {result1[1]} and {result3[1]} respectively ")
        elif result1[1] > result2[1] and result3[1] < result4[1]:
            print(F"congratulations {result1[0]} and  {result4[0]}   you have the total vote of {result1[1]} and {result4[1]} respectively ")
        elif result1[1] < result2[1] and result3[1] < result4[1]:
            print(F"congratulations {result2[0]} and  {result4[0]}   you have the total vote of {result2[1]} and {result4[1]} respectively ")
        elif result1[1] < result2[1] and result3[1] > result4[1]:
            print(F"congratulations {result2[0]} and  {result3[0]}   you have the total vote of {result2[1]} and {result3[1]} respectively ")
        elif  result1[1] == result2[1] and result3[1] > result4[1]:
            print( F" the presidential vote is a draw and congrstulations {result3[0]}   you have the total vote of {result3[1]} ")
        elif result1[1] == result2[1] and result3[1] < result4[1]:
            print( F" the presidential vote is a draw and congratulations {result4[0]}   you have the total vote of {result4[1]} ")
        elif result1[1] > result2[1] and result3[1] == result4[1]:
            print( F" the  secretary vote is a draw and congratulations {result1[0]}   you have the total vote of {result1[1]} ")
        elif result1[1] < result2[1] and result3[1] == result4[1]:
            print( F" the  secretary vote is a draw and congratulations {result2[0]}   you have the total vote of {result2[1]} ")
        else:
            print("the election is a draw , we will annouce another day for another election ")


