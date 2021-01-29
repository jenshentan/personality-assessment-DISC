import os
import csv
from colorama import Fore, Back, Style
import datetime

class Person:

    data = {}

    def __init__(self):
        self.record = None
        self.key = None
        self.read_file_data()
        self.newlist = None
        self.user_validation = None
        #self.create_new_account()
        
    def read_file_data(self):
        file_name = 'database_disc.csv'
        
        current_folder = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_folder,file_name)
        file = open(file_path,'r')

        for line in file:
            #print(line)
            line = line.strip("\n")
            column = line.split(',')
            #print(column)

            Person.data[int(column[0])] = [column[1],column[2],column[3],column[4],float(column[5]),column[6],float(column[7]),float(column[8]),float(column[9]),float(column[10])]
            
        file.close()

        self.record = Person.data.get(self.key)

    #THIS IS A USER AND ADMIN FUNCTION
    def login_account(self, account_id = None,password=None):
        self.key = account_id
        self.user_validation = Person.data.get(account_id)
        #print(self.user_validation)

        if Person.data.get(account_id):
            self.record = Person.data.get(account_id)
            #print("account found")
            #print(self.record)
            if self.user_validation[5] != "user":
                #print("Head to Admin Login")
                if self.user_validation[3] == password:
                    return "Welcome Back Admin!"
                else:
                    self.user_validation =None
                    print("Incorrect User ID/Password")
                    return None
            else:
                if self.record[3] == password:
                    #username_welcome = (f"{self.record[0]} {self.record[1]}")
                    #print(f"Welcome {username_welcome.upper()}")
                    #print("Welcome")
                    return True
                else:
                    self.record = None
                    print("Incorrect User ID/Password") 
                    return None       
        else:
            print("account not found")
            return False 

class User(Person):

    def __init__(self):
        Person.__init__(self)

        #THIS IS BOTH AN ADMIN AND USER FUNCTION

    def create_new_account(self):

        file_name = 'database_disc.csv'
        
        current_folder = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_folder,file_name)
        file = open(file_path,'r')

        with open(file_path,'a+', newline='') as main_data:
            new_data = csv.writer(main_data,delimiter=",",quoting=csv.QUOTE_MINIMAL)
            new_key = max(list(Person.data.keys())) + 1
            #print(new_key)
            print(f"You are creating a new personality assessment account with us and your reference number is {new_key}")

            reference_no = new_key
            first_name = input("Enter Your First Name : ")
            last_name = input("Enter Your Last Name : ")
            email_add = input("Enter Your Email Address : ")
            new_pass = input("Create a new Password : ")
            user_age = int(input("Enter Your Age : "))
            acc_type = "user"
            d_quadrant = 0
            i_quadrant = 0
            s_quadrant = 0
            c_quadrant = 0

            new_row = [reference_no,first_name,last_name,email_add,new_pass,user_age,acc_type,d_quadrant,i_quadrant,s_quadrant,c_quadrant]

            new_data.writerow(new_row)

            first_name_upper = first_name.upper()
            last_name_upper = last_name.upper()

            print(f"Welcome to our application {first_name_upper} {last_name_upper} ")
            print(f"Your login ID is {reference_no}")
            print(f"Your account has been registered with the following details :-")
            print(f"Name : {first_name_upper} {last_name_upper} ")
            print(f"Age : {user_age} ")
            print(f"Email Address : {email_add} ")
            print(f"Your may enjoy our personality assessment application :)")

        file.close()

    def print_info(self):
        self.read_file_data()
        # file_name = 'database_disc.csv'
        
        # current_folder = os.path.dirname(os.path.abspath(__file__))
        # file_path = os.path.join(current_folder,file_name)
        # file = open(file_path,'r')

        username_welcome = (f"{self.record[0]} {self.record[1]}")
        upper_username = username_welcome.upper()

        if self.record[6] == 0:
            d_personality = "No data yet, perform your assessment and view again later"
        else:
            d_personality = int(self.record[6])

        if self.record[7] == 0:
            i_personality = "No data yet, perform your assessment and view again later"
        else:
            i_personality = int(self.record[7])
        if self.record[8] == 0:
            s_personality = "No data yet, perform your assessment and view again later"
        else:
            s_personality = int(self.record[8])
        if self.record[9] == 0:
            c_personality = "No data yet, perform your assessment and view again later"
        else:
            c_personality = int(self.record[9])
    
        temp_dict = {
            "Controller" : d_personality,
            "Promoter" : i_personality,
            "Supporter" : s_personality,
            "Analyser" : c_personality 
        }
        sorted_temp_dict = dict(sorted(temp_dict.items(),key=lambda item:item[1],reverse=True))
        #print(sorted_temp_dict)

        #References : https://www.geeksforgeeks.org/python-get-the-first-key-in-dictionary/
        first_key_value = next(iter(sorted_temp_dict))

        # if sorted_temp_dict[f"{(first_key_value)}"] == 0:
        #     print("There is no record")
        # else:
        #     print(f"The record is {str(first_key_value)}")

        #IF first key value is none, output = "not determined yet, please view again after your assessment."

        if self.record[6] == 0 or self.record[7] == 0 or self.record[8] == 0 or self.record[9] == 0:
            to_print = "not determined yet, please try the assessment and view again later."
        else:
            to_print = str(first_key_value)

        print(f"Hi {upper_username}")
        print(f"Your age is {int(self.record[4])} and your dominant personality type is {to_print}")
        print(f'Your Current Personality Profile Score is : ')        
        for key,value in sorted_temp_dict.items():
            print(key,' : ',value)

        #file.close()

    def read_own_personality(self):
        self.read_file_data()
        
        # file_name = 'database_disc.csv'
        
        # current_folder = os.path.dirname(os.path.abspath(__file__))
        # file_path = os.path.join(current_folder,file_name)
        # file = open(file_path,'r')

        username_welcome = (f"{self.record[0]} {self.record[1]}")
        upper_username = username_welcome.upper()
    
        temp_dict = {
            "Controller" : int(self.record[6]),
            "Promoter" : int(self.record[7]),
            "Supporter" : int(self.record[8]),
            "Analyser" : int(self.record[9]) 
        }

        sorted_temp_dict = dict(sorted(temp_dict.items(),key=lambda item:item[1],reverse=True))
        #print(sorted_temp_dict)

        #References : https://www.geeksforgeeks.org/python-get-the-first-key-in-dictionary/
        first_key_value = next(iter(sorted_temp_dict))
        first_key_value_in_dict = str(first_key_value)

        if self.record[6] == 0 or self.record[7] == 0 or self.record[8] == 0 or self.record[9] == 0:
            print("You have not done your assessment yet, please try again after performing your personality test")
        else:
            if first_key_value_in_dict == "Controller":
                print(f"D stands for Extrovert & Task Oriented, which means you have the personality of a Controller!")
                self.view_d_score()
            elif first_key_value_in_dict == "Promoter":
                print(f"I stands for Extrovert & People Oriented, which means you have the personality of a Promoter!")
                self.view_i_score()
            elif first_key_value_in_dict =="Supporter":
                print(f"S stands for Introvert & People Oriented, which means you have the personality of a Supporter!")
                self.view_s_score()
            elif first_key_value_in_dict == "Analyser":
                print(f"C stands for Introvert & Task Oriented, which means you have the personality of a Analyser!")
                self.view_c_score()
            else:
                print("There is an error, please contact admin for support")

        #file.close()

        
    def personality_assessment(self):
        #reference :  https://www.geeksforgeeks.org/print-colors-python-terminal/
        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I am a good listener")
        while True:
            try:
                s1 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if s1 < 1:
                print("Your value must be between 1 -5")
                continue
            elif s1 >5:
                print("Your value must be less than 5")
                continue
            else:
                break

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I want to make the rules")
        while True:
            try:
                c1 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if c1 < 1:
                print("Your value must be between 1 -5")
                continue
            elif c1 >5:
                print("Your value must be less than 5")
                continue
            else:
                break   

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I like to do things accurately")
        while True:
            try:
                d1 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if d1 < 1:
                print("Your value must be between 1 -5")
                continue
            elif d1 >5:
                print("Your value must be less than 5")
                continue
            else:
                break

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I have wide variety of friends")
        while True:
            try:
                i1 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if i1 < 1:
                print("Your value must be between 1 -5")
                continue
            elif i1 >5:
                print("Your value must be less than 5")
                continue
            else:
                break

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I put up with things that I don't like")
        while True:
            try:
                s2 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if s2 < 1:
                print("Your value must be between 1 -5")
                continue
            elif s2 >5:
                print("Your value must be less than 5")
                continue
            else:
                break

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I go straight ahead with projects")
        while True:
            try:
                c2 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if c2 < 1:
                print("Your value must be between 1 -5")
                continue
            elif c2 >5:
                print("Your value must be less than 5")
                continue
            else:
                break

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I like to do things the right way")
        while True:
            try:
                d2 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if d2 < 1:
                print("Your value must be between 1 -5")
                continue
            elif d2 >5:
                print("Your value must be less than 5")
                continue
            else:
                break 

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I am usually liked by others")
        while True:
            try:
                i2 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if i2 < 1:
                print("Your value must be between 1 -5")
                continue
            elif i2 >5:
                print("Your value must be less than 5")
                continue
            else:
                break

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I am willing to follow orders")
        while True:
            try:
                s3 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if s3 < 1:
                print("Your value must be between 1 -5")
                continue
            elif s3 >5:
                print("Your value must be less than 5")
                continue
            else:
                break

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I act in a forceful way")
        while True:
            try:
                c3 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if c3 < 1:
                print("Your value must be between 1 -5")
                continue
            elif c3 >5:
                print("Your value must be less than 5")
                continue
            else:
                break 

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I do things right for the first time")
        while True:
            try:
                d3 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if d3 < 1:
                print("Your value must be between 1 -5")
                continue
            elif d3 >5:
                print("Your value must be less than 5")
                continue
            else:
                break

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I like to meet new people")
        while True:
            try:
                i3 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if i3 < 1:
                print("Your value must be between 1 -5")
                continue
            elif i3 >5:
                print("Your value must be less than 5")
                continue
            else:
                break

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I will go along with others")
        while True:
            try:
                s4 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if s4 < 1:
                print("Your value must be between 1 -5")
                continue
            elif s4 >5:
                print("Your value must be less than 5")
                continue
            else:
                break

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I want to win")
        while True:
            try:
                c4 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if c4 < 1:
                print("Your value must be between 1 -5")
                continue
            elif c4 >5:
                print("Your value must be less than 5")
                continue
            else:
                break 

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I think of what makes sense")
        while True:
            try:
                d4 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if d4 < 1:
                print("Your value must be between 1 -5")
                continue
            elif d4 >5:
                print("Your value must be less than 5")
                continue
            else:
                break

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I am fun to be with!")
        while True:
            try:
                i4 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if i4 < 1:
                print("Your value must be between 1 -5")
                continue
            elif i4 >5:
                print("Your value must be less than 5")
                continue
            else:
                break

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I will think of others before I make a decision")
        while True:
            try:
                s5 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if s5 < 1:
                print("Your value must be between 1 -5")
                continue
            elif s5 >5:
                print("Your value must be less than 5")
                continue
            else:
                break

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I will be the first to act")
        while True:
            try:
                c5 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if c5 < 1:
                print("Your value must be between 1 -5")
                continue
            elif c5 >5:
                print("Your value must be less than 5")
                continue
            else:
                break 

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I like to be precise")
        while True:
            try:
                d5 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if d5 < 1:
                print("Your value must be between 1 -5")
                continue
            elif d5 >5:
                print("Your value must be less than 5")
                continue
            else:
                break

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I always see things positively")
        while True:
            try:
                i5 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if i5 < 1:
                print("Your value must be between 1 -5")
                continue
            elif i5 >5:
                print("Your value must be less than 5")
                continue
            else:
                break

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I am willing to help others")
        while True:
            try:
                s6 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if s6 < 1:
                print("Your value must be between 1 -5")
                continue
            elif s6 >5:
                print("Your value must be less than 5")
                continue
            else:
                break

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I do not give in easily")
        while True:
            try:
                c6 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if c6 < 1:
                print("Your value must be between 1 -5")
                continue
            elif c6 >5:
                print("Your value must be less than 5")
                continue
            else:
                break

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I am shy with others")
        while True:
            try:
                d6 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if d6 < 1:
                print("Your value must be between 1 -5")
                continue
            elif d6 >5:
                print("Your value must be less than 5")
                continue
            else:
                break

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I feel contented with what I have all the time")
        while True:
            try:
                i6 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if i6 < 1:
                print("Your value must be between 1 -5")
                continue
            elif i6 >5:
                print("Your value must be less than 5")
                continue
            else:
                break

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I understand others' feelings")
        while True:
            try:
                s7 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if s7 < 1:
                print("Your value must be between 1 -5")
                continue
            elif s7 >5:
                print("Your value must be less than 5")
                continue
            else:
                break

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"People see me as powerful")
        while True:
            try:
                c7 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if c7 < 1:
                print("Your value must be between 1 -5")
                continue
            elif c7 >5:
                print("Your value must be less than 5")
                continue
            else:
                break

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I am good at analyzing things")
        while True:
            try:
                d7 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if d7 < 1:
                print("Your value must be between 1 -5")
                continue
            elif d7 >5:
                print("Your value must be less than 5")
                continue
            else:
                break

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I am pretty much happy and carefree")
        while True:
            try:
                i7 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if i7 < 1:
                print("Your value must be between 1 -5")
                continue
            elif i7 >5:
                print("Your value must be less than 5")
                continue
            else:
                break

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I am nice to other people")
        while True:
            try:
                s8 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if s8 < 1:
                print("Your value must be between 1 -5")
                continue
            elif s8 >5:
                print("Your value must be less than 5")
                continue
            else:
                break

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I am sure of myself")
        while True:
            try:
                c8 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if c8 < 1:
                print("Your value must be between 1 -5")
                continue
            elif c8 >5:
                print("Your value must be less than 5")
                continue
            else:
                break

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I think things through")
        while True:
            try:
                d8 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if d8 < 1:
                print("Your value must be between 1 -5")
                continue
            elif d8 >5:
                print("Your value must be less than 5")
                continue
            else:
                break

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I can liven things up")
        while True:
            try:
                i8 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if i8 < 1:
                print("Your value must be between 1 -5")
                continue
            elif i8 >5:
                print("Your value must be less than 5")
                continue
            else:
                break  

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I have warm feeling for people")
        while True:
            try:
                s9 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if s9 < 1:
                print("Your value must be between 1 -5")
                continue
            elif s9 >5:
                print("Your value must be less than 5")
                continue
            else:
                break

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I want to be in charge")
        while True:
            try:
                c9 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if c9 < 1:
                print("Your value must be between 1 -5")
                continue
            elif c9 >5:
                print("Your value must be less than 5")
                continue
            else:
                break

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I keep things to myself")
        while True:
            try:
                d9 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if d9 < 1:
                print("Your value must be between 1 -5")
                continue
            elif d9 >5:
                print("Your value must be less than 5")
                continue
            else:
                break

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I feel relaxed most of the time")
        while True:
            try:
                i9 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if i9 < 1:
                print("Your value must be between 1 -5")
                continue
            elif i9 >5:
                print("Your value must be less than 5")
                continue
            else:
                break

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I let others lead")
        while True:
            try:
                s10 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if s10 < 1:
                print("Your value must be between 1 -5")
                continue
            elif s10 >5:
                print("Your value must be less than 5")
                continue
            else:
                break

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I like to take action")
        while True:
            try:
                c10 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if c10 < 1:
                print("Your value must be between 1 -5")
                continue
            elif c10 >5:
                print("Your value must be less than 5")
                continue
            else:
                break

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I think things over carefully")
        while True:
            try:
                d10 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if d10 < 1:
                print("Your value must be between 1 -5")
                continue
            elif d10 >5:
                print("Your value must be less than 5")
                continue
            else:
                break 

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I am happy most of the time")
        while True:
            try:
                i10 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if i10 < 1:
                print("Your value must be between 1 -5")
                continue
            elif i10 >5:
                print("Your value must be less than 5")
                continue
            else:
                break

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I dont like to cause problems")
        while True:
            try:
                s11 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if s11 < 1:
                print("Your value must be between 1 -5")
                continue
            elif s11 >5:
                print("Your value must be less than 5")
                continue
            else:
                break

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I am quick to act")
        while True:
            try:
                c11 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if c11 < 1:
                print("Your value must be between 1 -5")
                continue
            elif c11 >5:
                print("Your value must be less than 5")
                continue
            else:
                break

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I don't like too much attention")
        while True:
            try:
                d11 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if d11 < 1:
                print("Your value must be between 1 -5")
                continue
            elif d11 >5:
                print("Your value must be less than 5")
                continue
            else:
                break 

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I find it easy to meet strangers")
        while True:
            try:
                i11 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if i11 < 1:
                print("Your value must be between 1 -5")
                continue
            elif i11 >5:
                print("Your value must be less than 5")
                continue
            else:
                break

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I dont make demands of people")
        while True:
            try:
                s12 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if s12 < 1:
                print("Your value must be between 1 -5")
                continue
            elif s12 >5:
                print("Your value must be less than 5")
                continue
            else:
                break

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I feel strong")
        while True:
            try:
                c12 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if c12 < 1:
                print("Your value must be between 1 -5")
                continue
            elif c12 >5:
                print("Your value must be less than 5")
                continue
            else:
                break 

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I don't say much in a group")
        while True:
            try:
                d12 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if d12 < 1:
                print("Your value must be between 1 -5")
                continue
            elif d12 >5:
                print("Your value must be less than 5")
                continue
            else:
                break

        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.WHITE +"I communicate in a lively manner")
        while True:
            try:
                i12 = int(input(Fore.WHITE+"Your Choice : "))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if i12 < 1:
                print("Your value must be between 1 -5")
                continue
            elif i12 >5:
                print("Your value must be less than 5")
                continue
            else:
                break 

        c_score = d1+d2+d3+d4+d5+d6+d7+d8+d9+d10+d11+d12
        i_score = i1+i2+i3+i4+i5+i6+i7+i8+i9+i10+i11+i12
        s_score = s1+s2+s3+s4+s5+s6+s7+s8+s9+s10+s11+s12
        d_score = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12

        #LIST TO COMBINE = LIST TO COMBINE + SCORE LIST
        list_to_combine = [self.key,self.record[0],self.record[1],self.record[2],self.record[3],self.record[4],self.record[5]]
        score_list = [d_score,i_score,s_score,c_score]
        list_to_combine.extend(score_list)
        #print(list_to_combine)
        
        self.new_list = list_to_combine

        new_dictionary = {
            "Controller" : d_score,
            "Promoter" : i_score,
            "Analyzer" : c_score,
            "Supporter" : s_score
        }
        
        sorted_new_dict = dict(sorted(new_dictionary.items(),key=lambda item:item[1],reverse=True))
        #print(sorted_new_dict)
        print(f'Your Current Personality Profile Score is : ')        
        for key,value in sorted_new_dict.items():
            print(key,' : ',value) 


        #OPEN FILE AND SAVE
        file_name = 'database_disc.csv'
        
        current_folder = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_folder,file_name)
        file = open(file_path,'r')

        with open(file_path,'a+', newline='') as main_data:
            new_data = csv.writer(main_data,delimiter=",",quoting=csv.QUOTE_MINIMAL)
            
            new_data.writerow(list_to_combine)

        file.close()
       
    def view_d_score(self):
        #Referenced "https://discinsights.com/personality-style-d"
        print(
        '''
The D Personality Style tends to be direct and decisive, sometimes described as dominant. 
They would prefer to lead than follow, and tend towards leadership and management positions. 
They tend to have high self-confidence, and are risk takers and problem solvers, 
which enables others to look to them for decisions and direction. They tend to be self-starters.


They think about big picture goals and tangible results. 
They are bottom-line organizers that can lead an entire group in one direction. 
They place great value on time frames and seeing results. 
The D may challenge the status quo and think in a very innovative way.

They tend to overstep authority, as they prefer to be in charge themselves.
At times they can be argumentative and not listen to the reasoning of others.
They tend to dislike repetition and routine, and may ignore the details and minutia of a situation, even if it's important.
They may attempt too much at one time, hoping to see quick results.

The D Personality Type craves to be in control of the situation, and therefore fears the idea of being taken advantage of by others.
        '''
        )

    def view_i_score(self):
        #Referenced : https://discinsights.com/personality-style-i
        
        print(
        '''
The I Personality Style is not afraid to be the center of attention. 
They are enthusiastic, optimistic, talkative, persuasive, impulsive and emotional. 
This personality type will trust others naturally, truly enjoys being around others, 
and functions best when around people and working in teams.

The I style are naturally creative problem solvers who can think outside of the box.
They are great encourages and motivators of others. 
They keep environments positive with their enthusiasm and positive sense of humor. 
They will go out of their way to keep things light, avoid and negotiate conflict and keep the peace.

The I Personality Style is likely not good with detail. 
They are more concerned with people and popularity than with tangible results and organization. 
It's also possible that they are not great listeners, and may give the impression of waiting to speak 
instead of truly listening to what someone else is saying. In some cases, gestures and facial expressions are overly used.

Since acceptance and approval by others is the main desire of I Personality Types, rejection is their biggest fear.
        '''
        )


    def view_c_score(self):
        #Referenced : https://discinsights.com/personality-style-c
        print(f"C stands for Introvert & Task Oriented, which means you have the personality of a Analyser!")
        print(
        '''
The C DISC Styles are accurate, precise, detail-oriented and conscientious. 
They think very analytically and systematically, and make decisions carefully 
with plenty of research and information to back it up.
The C has very high standards for both themselves and others. 
Because they focus on the details and see what many other styles do not, 
they tend to be good problem solvers and very creative people.

The C style brings perspective to groups and tend to be the "anchor of reality" in team thought. 
When something is proposed, it is the C who will think through every detail of how it works and the process. 
They will make realistic estimates and will voice the problems that they see with the plan or already existing system. 
The C is conscientious and even-tempered. They will complete tasks they've committed to and will be very thorough. 
They take great pride in doing their work accurately and are excellent people to analyze, research, or test information.

The C Personality Type is one of the passive styles, which results in avoiding conflict. 
They will avoid conflict rather than argue, and it is difficult to get them to verbalize their feelings. 
They need clear-cut boundaries in order to feel comfortable at work, in relationships, or to take action. 
Sometimes the C can be bound by procedures and methods, and find it difficult to stray from order. 
Sometimes they can get too bogged down in the small details, making it difficult to see the next steps or big picture.

Because C Personality Types take great pride in being accurate and correct, they fear criticism.
        '''
        )




    def view_s_score(self):
        print(
        '''
The S Personality Type is known for being steady, stable, and predictable. 
They are even-tempered, friendly, sympathetic with others, and very generous with loved ones. 
The S is understanding and listens well. Preferring close, personal relationships, 
the S is very opened with loved ones, but can also be possessive at times and hold them close.

The S style is reliant and dependable. 
They are patient, good listeners who want to work with teams in a harmonious way. 
They strive for consensus and will try hard to reconcile conflicts as they arise. 
They are compliant towards authority and a loyal team player. 
The S is also good at multi-tasking and seeing tasks through until completion.

The S are described as stable and predictable, this is because they like
to get into a routine and what feels secure and stick with it. 
This results in an opposition towards change. 
However, when change is occurring, they adjust best when given a long enough period of time
to adjust and an explanation of why the change is occurring. 
Because the S style is passive and avoids conflict, 
they may also hold grudges when they experience frustrations and resentments, 
instead of facing the issue head-on. They strive for positive environments and relationships, 
and can be especially sensitive when it comes to criticism. 
They want to please others, therefore may have a difficult time saying, "No" or establishing priorities.

Because the S strives for stability and a feeling of peace and safety, they fear the loss of security through change.


        '''
        )


    def menu(self):
        print(Fore.WHITE+ f"Welcome to JS's DISC Application Beta - (Version 1)")
        print("[1] - View My Profile Information")
        print("[2] - Perform My Personality Assessment")
        print("[3] - Read My Own Personality Traits")
        print("[4] - Read About Others Personality Traits")
        print("[5] - Check My Compatibility")
        print("[6] - What Job Suits Best for me?")
        print("[7] - Save My Assessment")
        print("[0] - Exit")

        
        option = int(input("What would you like to do today : "))
        
        while option != 0:
            
            if option == 1:
                self.print_info()

            elif option == 2:             
                self.personality_assessment()

            elif option == 3:
                self.read_own_personality()
                
                
            elif option == 4:
                
                self.menu_other_traits()
                
            elif option == 5:
                self.check_compatibility()

            elif option == 6:
                print("Job Suitability")
                self.my_suitable_job()
                

            elif option == 7:
                print("Save my assessment")
                self.save_new_personal_file()

            else:
                print("Please Choose Available Options on Screen")

            print()
            self.menu()
            option = int(input("What would you like to do today : "))
        
        
        main()
        print("See you again soon!")


    def menu_other_traits(self):
        print(f"Which other traits would you like to read today?")
        print("[1] - D Personality")
        print("[2] - I Personality")
        print("[3] - S Personality")
        print("[4] - C Personality")
        print("[0] - Exit")

        
        option = int(input("What would you like to do today : "))
        
        while option != 0:
            
            if option == 1:
                self.view_d_score()

            elif option == 2:             
                self.view_i_score()

            elif option == 3:
                self.view_s_score()
                #print("Read Own Personality Traits")
                
            elif option == 4:
                self.view_c_score()

            else:
                print("Please Choose Available Options on Screen")

            print()
            self.menu()
            option = int(input("What would you like to do today : "))
        
        main()
        #print("See you again soon!")

    def my_suitable_job(self):
        self.read_file_data()

        temp_dict = {
            "Controller" : int(self.record[6]),
            "Promoter" : int(self.record[7]),
            "Supporter" : int(self.record[8]),
            "Analyser" : int(self.record[9]) 
        }

        sorted_temp_dict = dict(sorted(temp_dict.items(),key=lambda item:item[1],reverse=True))
        #print(sorted_temp_dict)

        #References : https://www.geeksforgeeks.org/python-get-the-first-key-in-dictionary/
        first_key_value = next(iter(sorted_temp_dict))
        first_key_value_in_dict = str(first_key_value)

        if self.record[6] == 0 or self.record[7] == 0 or self.record[8] == 0 or self.record[9] == 0:
            print("You have not done your assessment yet, please try again after performing your personality test")
        else:
            if first_key_value_in_dict == "Controller":
                print(f"D stands for Extrovert & Task Oriented, which means you have the personality of a Controller!")
                self.view_d_jobs()    
            elif first_key_value_in_dict == "Promoter":
                print(f"I stands for Extrovert & People Oriented, which means you have the personality of a Promoter!")
                self.view_i_jobs()
            elif first_key_value_in_dict =="Supporter":
                print(f"S stands for Introvert & People Oriented, which means you have the personality of a Supporter!")
                self.view_s_jobs()
            elif first_key_value_in_dict == "Analyser":
                print(f"C stands for Introvert & Task Oriented, which means you have the personality of a Analyser!")
                self.view_c_jobs()
            else:
                print("There is an error, please contact admin for support")

    def view_d_jobs(self):
        print(Fore.WHITE +
            '''
The D personality, being one of the four primary types, has a strong drive for success. 
They focus on results by working quickly and making efficient, direct decisions. 
Typically straying away from the social scene, these people prefer to be independent and have control over a situation. 
They also tend to motivate and challenge their coworkers in an urgent manner. 

Aside from being top-notch leaders, they tend to struggle with teamwork, details, and planning.
D personalities can come off as critical, making conversation rather tough. 
Their forceful and impatient predispositions may be intimidating, especially since they forget to 
include others in the problem-solving process. They do this, however, because they want to achieve
their objective instantly without spending any additional time on the specifics.

DiSC D types feel most content in authoritative positions. When they set a goal, nothing stops them from achieving it.
They carefully choose their plan of action before meticulously executing each step along the way.
            '''
        )
        print(Fore.YELLOW +
        '''
==============================================
|                                            |
|    Presidents                              |
|    Founders                                |
|    CEOS                                    |
|    Police Officers                         |
|    Lawyers                                 |
|    Directors                               |
|    Other Professions that Display Power    |
|                                            |
==============================================

        '''
        )

    def view_i_jobs(Self):
        print(Fore.WHITE +
            '''
The i DiSC personality has strong socialization skills due to their outgoing, friendly nature. 
They love being around people and understand how to successfully engage in conversation while 
maintaining a relaxed, amicable persona. They connect well with others, allowing them to 
understand and motivate those around them. Their positive energy also encourages a healthy,
productive work environment.

The i type has trouble with a structured, predictable routine that many workers require. 
They spend most of their time conversing with others, leaving little room for task competition. 
These people generally have trouble making decisions in fear of disapproval or rejection. 
They also fail to pursue many of the great ideas they have.

These people need to let their creativity shine with the opportunity to learn and explore new things. 
They require regular interaction with others and usually prefer occupations that entail a great deal of teamwork and collaboration.
            '''
        )
        print(Fore.YELLOW +
        '''
==============================================
|                                            |
|    Writer                                  |
|    Artist                                  |
|    Graphic Artist                          |
|    Designer                                |
|    Musician                                |
|    Public Relations Professional           |
|    Marketing Professional                  |
|                                            |
==============================================

        '''
        )


    def view_s_jobs(self):
        print(Fore.WHITE +
            '''
S personalities have a knack for making others feel comfortable and at ease. 
They display a natural awareness for others, and this, in combination with their patient demeanor,
makes them excellent peacemakers. Some may consider them natural counselors or therapists, 
as they are highly empathetic and understanding. In the working world, they excel in producing 
long-lasting, healthy relationships built on trust and certainty. 
These types motivate those around them while calming stressful situations.

The kind-hearted practices of these humanitarians have its drawbacks. 
These people have a tough time being direct, providing negative feedback, 
and making decisions that affect others. They struggle when dealing with 
angry or unruly individuals and often fail to be productive in emotionally 
charged environments. Their desire to avoid conflict can also create indirect, 
unclear communication, leaving people around them feeling confused and led astray.

To feel most fulfilled, these individuals must work in a people-oriented job that 
allows them to display their compassionate side. They gain self-worth and motivation 
by helping others and building trusting relationships. Many also prefer to plan for 
the future and abide by those details.
            '''
        )
        print(Fore.YELLOW +
        '''
==============================================
|                                            |
|    Medicine                                |
|    Therapy                                 |
|    Customer Service                        |
|    Assistant Position                      |
|                                            |
==============================================

        '''
        )

    def view_c_jobs(self):
        print(Fore.WHITE +
            '''
The C personality type requires a large amount of independence, privacy, and isolation. 
They are hesitant to join social groups and take longer to become comfortable with others. 
Their analytical perception of life brings unique qualities to the work environment. 
These people know which questions to ask using a systematic approach, making them outstanding problem-solvers. 
By analyzing information and learning from previous data or outcomes, they display exemplary decision-making abilities.

These people are true perfectionists and have little patience for situations and people that do not align with these ideals. 
They spend too much time interpreting data and finding solutions in an attempt to find the perfect answer. 
Those who identify as a C type may appear hypocritical, as they tend to ask too many questions while criticizing those 
who fail to demonstrate innate precision and accuracy.

Careers for these people must include independent, analytical effort without a lot of collaboration or socialization. 
They need a highly structured environment with exact instructions and rules, as well.
            '''
        )
        print(Fore.YELLOW +
        '''
==============================================
|                                            |
|    Engineer                                |
|    Analyst                                 |
|    Scientist                               |
|    Developer                               |
|    Systems Administrator                   |
|    Data Scientist                          |
|    Investment Analyst                      |
|    Actuary                                 |
|                                            |
==============================================

        '''
        )

    def save_new_personal_file(self):
        self.read_file_data()
        record_ddmmyy = datetime.datetime.now()

        #LIST TO COMBINE = LIST TO COMBINE + SCORE LIST
        list_to_combine = [self.key,self.record[0],self.record[1],self.record[2],self.record[3],self.record[4],self.record[5],self.record[6],self.record[7],self.record[8],self.record[9],record_ddmmyy]

        file_name = f"{self.record[0]}_{self.record[1]}.csv"

        with open(file_name,'a+',newline='') as file:
            
            writer = csv.writer(file, delimiter=",",quoting=csv.QUOTE_MINIMAL)
            writer.writerow(list_to_combine)

        print(Fore.RED + "Your file has been successfully saved & updated")

    def check_compatibility(self):
        self.read_file_data()

        temp_dict = {
            "Controller" : int(self.record[6]),
            "Promoter" : int(self.record[7]),
            "Supporter" : int(self.record[8]),
            "Analyser" : int(self.record[9]) 
        }

        sorted_temp_dict = dict(sorted(temp_dict.items(),key=lambda item:item[1],reverse=True))
        #print(sorted_temp_dict)

        #References : https://www.geeksforgeeks.org/python-get-the-first-key-in-dictionary/
        first_key_value = next(iter(sorted_temp_dict))
        first_key_value_in_dict = str(first_key_value)

        if self.record[6] == 0 or self.record[7] == 0 or self.record[8] == 0 or self.record[9] == 0:
            print("You have not done your assessment yet, please try again after performing your personality test")
        else:
            if first_key_value_in_dict == "Controller":
                print(f"[1] I would like to check my compatibility with Promoter personality type")
                print(f"[2] I would like to check my compatibility with Supporter personality type")
                print(f"[3] I would like to check my compatibility with Analyzer personality type")
                   
            elif first_key_value_in_dict == "Promoter":
                print(f"[1] I would like to check my compatibility with Controller personality type")
                print(f"[2] I would like to check my compatibility with Supporter personality type")
                print(f"[3] I would like to check my compatibility with Analyzer personality type")

            elif first_key_value_in_dict =="Supporter":
                print(f"[1] I would like to check my compatibility with Controller personality type")
                print(f"[2] I would like to check my compatibility with Promoter personality type")
                print(f"[3] I would like to check my compatibility with Analyzer personality type")

            elif first_key_value_in_dict == "Analyser":
                print(f"[1] I would like to check my compatibility with Controller personality type")
                print(f"[2] I would like to check my compatibility with Promoter personality type")
                print(f"[3] I would like to check my compatibility with Supporter personality type")

            else:
                print("There is an error, please contact admin for support")

class Admin(Person):

    def __init__(self):
        Person.__init__(self)

    #THIS IS AN ADMIN FUNCTION
    def view_one_user(self):
        self.read_file_data()

        account_id = int(input("Key in User ID : "))
        if not Person.data.get(account_id):
            print("No such user in database")
        else:
            for user_id,details in Person.data.items():
                if user_id == account_id:
                    #print(details)  
                    print("User Profile : ")
                    print(f"First Name : {details[0]}")
                    print(f"Last Name : {details[1]}")
                    print(f"Email Add : {details[2]}")
                    print(f"Age : {details[4]}")
                    print(f"D_Info : {details[6]}")
                    print(f"I_Info : {details[7]}")
                    print(f"S_Info : {details[8]}")
                    print(f"C_Info : {details[9]}")

    def view_all_users(self):
        self.read_file_data()

        for key, value in Person.data.items():
            print(key,value)

    def delete_user(self):
        self.read_file_data()
        account_id = int(input("Key in User ID : "))

        self.record = Person.data.get(account_id)

        if not Person.data.get(account_id):
            print("No such user in database")
        elif self.record[5] == "admin":
            print("You are not allowed to delete admin account")        
        else:
            print(Person.data[account_id])
            del Person.data[account_id]
            print(f"{account_id} has been deleted")

    def oldest_user(self):
        self.read_file_data()
        print("Function coming soon")
        # print(Person.data.keys())
        # print(Person.data.items())

    def create_new_account_admin(self):

        
        file_name = 'database_disc.csv'
        
        current_folder = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_folder,file_name)
        file = open(file_path,'r')

        with open(file_path,'a+', newline='') as main_data:
            new_data = csv.writer(main_data,delimiter=",",quoting=csv.QUOTE_MINIMAL)
            new_key = max(list(Person.data.keys())) + 1
            #print(new_key)
            print(f"You are creating a new personality assessment account with us and your reference number is {new_key}")

            reference_no = new_key
            first_name = input("Enter Your First Name : ")
            last_name = input("Enter Your Last Name : ")
            email_add = input("Enter Your Email Address : ")
            new_pass = input("Create a new Password : ")
            user_age = int(input("Enter Your Age : "))
            acc_type = "user"
            d_quadrant = 0
            i_quadrant = 0
            s_quadrant = 0
            c_quadrant = 0

            new_row = [reference_no,first_name,last_name,email_add,new_pass,user_age,acc_type,d_quadrant,i_quadrant,s_quadrant,c_quadrant]

            new_data.writerow(new_row)

            first_name_upper = first_name.upper()
            last_name_upper = last_name.upper()

            print(f"Welcome to our application {first_name_upper} {last_name_upper} ")
            print(f"Your login ID is {reference_no}")
            print(f"Your account has been registered with the following details :-")
            print(f"Name : {first_name_upper} {last_name_upper} ")
            print(f"Age : {user_age} ")
            print(f"Email Address : {email_add} ")
            print(f"Your may enjoy our personality assessment application :)")

        file.close()
            

    def download_data(self):
        self.read_file_data()
        record_ddmmyy = datetime.datetime.now()

        #record_ddmmyy = datetime.datetime.now()
        for key, value in Person.data.items():
            print(key,value)

            file_to_write = (key,value,record_ddmmyy)

            new_name = input(Fore.WHITE + "What would you like to name your file? : ")

            file_name = f"{new_name}.csv"
            with open(file_name,'a+',newline='') as file:
            
                writer = csv.writer(file, delimiter=",",quoting=csv.QUOTE_MINIMAL)
                writer.writerow(file_to_write)
            #to_print = (key,value)
        #LIST TO COMBINE = LIST TO COMBINE + SCORE LIST
        #list_to_combine = [self.key,self.record[0],self.record[1],self.record[2],self.record[3],self.record[4],self.record[5],self.record[6],self.record[7],self.record[8],self.record[9],record_ddmmyy]




        print(Fore.RED + "Your file has been successfully saved & updated")


    def admin_menu(self):
        print(Fore.RED+ f"ADMIN PAGE")
        print("[1] - View Single Person Profile Information Based on User ID")
        print("[2] - View All Users in Database")
        print("[3] - Delete Single User in Database")
        print("[4] - Oldest Person Age in Database")
        print("[5] - Youngest Person Age in Database")
        print("[6] - Average Age in Database")
        print("[7] - Statistics - How many users in each quadrant DISC?")
        print("[8] - Manual Account Creation")
        print("[9] - Download Data with New File Name")
        print("[0] - Exit")

        
        option = int(input(Fore.GREEN + "What would you like to do today : "))
        
        while option != 0:
            
            if option == 1: 
                #print("[1] - View Single Person Profile Information Based on User ID")
                self.view_one_user()

            elif option == 2:             
                #print("[2] - View All Users in Database")
                self.view_all_users()

            elif option == 3:
                #print("[3] - Delete Single User in Database")
                self.delete_user()

            elif option == 4:
                #print("[4] - Oldest Person Age in Database")
                self.oldest_user()

            elif option == 5:
                print("[5] - Youngest Person Age in Database")
                print("Function coming soon")

            elif option == 6:
                print("[6] - Average Age in Database")
                print("Function coming soon")

            elif option == 7:
                print("[7] - Statistics - How many users in each quadrant DISC?")
                print("Function coming soon")

            elif option == 8:
                print("[8] - Manual Account Creation")
                self.create_new_account_admin()
                

            elif option == 9:
                print("[9] - Downloading Data with New File Name")
                self.download_data()

            else:
                print("Please Choose Available Options on Screen")

            print()
            self.admin_menu()
            option = int(input("What would you like to do today : "))
        
        
        main()
        print("See you again soon!")
    


def main():
    #person = Person()
    user = User()
    admin = Admin()
    print("Welcome to JS's DISC Application Beta - (Version 1)")
    print("[1] Sign Up For A New Account")
    print("[2] Login to Existing Account")
    print("[0] Exit")
    option = int(input("Hi, what would you like to do today? "))
    while option !=0:
        if option == 1:
            print("Creating New Account with JS's DISC Application!")
            user.create_new_account()

        elif option ==2:
            
            print("User Login")
            login = user.login_account(account_id=int(input("Key-In Your ID ")),password=input("Enter Your Password "))
            print(login)
            if login == True:
                user.menu()
                print("Getting to the menu")
            elif login == False:
                main()
            elif login == "Welcome Back Admin!":
                admin.admin_menu()
            elif login == None:
                main()
            else:
                pass

        else:
            print("Please Choose Available Options on Screen")
        print()
        main()
        option = int(input("Hi, what would you like to do today? "))
    quit()
    print("See you again")

    
    
 

if __name__ == '__main__':
    main()



###==========================================================================================================================================================
# person = Person()
# person.read_file_data()
# person.login_account(10001,'123')
#person.create_new_account()
# person.view_c_score()
#person.personality_assessment()
#person.print_info()