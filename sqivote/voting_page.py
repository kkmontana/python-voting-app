import mysql.connector as connection
import time
import random
comm = connection.connect( host= "127.0.0.1", user= "root", password = "Kkmontana1@" ,database ="sqi_vote")
cursor = comm.cursor

class sqi_vote:

    def __init__(self):
        print("WELCOME to SQI POLLING CENTER ")
        time.sleep(2)
        
        print("what will you like to do, press 1 to register, press 2 to vote, 3 to count vote or 4 to quit the polling unit session")
        response = input(">>>: ")
        if response == "1":
            self.register()
        elif response == "2":
            self.vote()
        elif response == "3":
            from departmental_vote import winner
            winner()
            sqi_vote
        elif response == "4":
            "clear"
        else:
            print("wrong input ")
            time.sleep(2)
            sqi_vote()

    def register(self):
        print("""list of department \n1; data science \n2: web development \n3; data analytics \n4: javascript \n5: ui ux \n6: graphic design \n7: artificial intelligence""")
        department = input("what depeartment are you from ? ").lower().strip()
        if department == "data science" :
            from departmental_reg import data_science
            data_science()
            sqi_vote()
            
        elif department == "web development":
            from departmental_reg import web_development
            web_development()
            sqi_vote()

        elif department == "data analytics":
            from departmental_reg import data_analytics
            data_analytics()
            sqi_vote()
        elif department == "javascript":
            from departmental_reg import javascript
            javascript()
            sqi_vote()

        elif department == "ui ux":
            from departmental_reg import  ui_ux
            ui_ux()
            sqi_vote()

        elif department == "graphic design":
            from departmental_reg import graphic_design
            graphic_design()
            sqi_vote()

        elif department == "artificial intelligence":
            from departmental_reg import artificial_intelligence
            artificial_intelligence()
            sqi_vote()

        else:
            print("wrong input , try again ")
            sqi_vote()
            
        
            

    def vote(self):
        from departmental_vote import voters
        print("welcome to sqi pollimg unit.... you are to login and vote for the presidential and financial-secretary candidate of your choice ")
        voters()
        sqi_vote()

    


sqi_vote()
        




