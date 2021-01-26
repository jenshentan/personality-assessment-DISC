import os
import csv
from colorama import Fore, Back, Style

class Person:

    data = {}

    def __init__(self):
        self.record = None
        self.key = None
        self.read_file_data()
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
            print(f"Your account has been registered with the following details :-")
            print(f"Name : {first_name_upper} {last_name_upper} ")
            print(f"Age : {user_age} ")
            print(f"Email Address : {email_add} ")
            print(f"Your may enjoy our personality assessment application :)")



    #THIS IS A USER AND ADMIN FUNCTION
    def login_account(self, account_id = None,password=None):
        self.key = account_id

        if Person.data.get(account_id):
            self.record = Person.data.get(account_id)
            #print("account found")
            #print(self.record)
            if self.record[3] == password:
                #username_welcome = (f"{self.record[0]} {self.record[1]}")
                #print(f"Welcome {username_welcome.upper()}")
                print("Welcome")
                return True
            else:
                self.record = None
                print("Incorrect User ID/Password") 
                return None       
        else:
            print("account not found")
            return False        

    #THIS IS A USER FUNCTION
    def print_info(self):
        self.read_file_data()

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

        #IF first key value is none, output = "not determined yet, please view again after your assessment."

        print(f"Hi {upper_username}")
        print(f"Your age is {int(self.record[4])} and your dominant personality type is {str(first_key_value)}")
        print(f'Your Current Personality Profile Score is : ')        
        for key,value in sorted_temp_dict.items():
            print(key,' : ',value)


    #THIS IS AN ADMIN FUNCTION
    def view_all_users(self):
        pass

    #USER CAN COMPLETE THEIR PERSONALITY ASSESSMENT AND IT WILL BE UPDATED IN THE CSV DATABASE        
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

        list_to_combine = [self.key,self.record[0],self.record[1],self.record[2],self.record[3],self.record[4],self.record[5]]
        score_list = [d_score,i_score,s_score,c_score]
        list_to_combine.extend(score_list)
        #print(list_to_combine)
        
        file_name = 'database_disc.csv'
        
        current_folder = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_folder,file_name)
        file = open(file_path,'r')

        with open(file_path,'a+', newline='') as main_data:
            new_data = csv.writer(main_data,delimiter=",",quoting=csv.QUOTE_MINIMAL)
            
            new_data.writerow(list_to_combine)

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

    def view_d_score(self):
        print(f"D stands for Extrovert & Task Oriented, which means you have the personality of a Controller!")

    def view_i_score(self):
        print(f"I stands for Extrovert & People Oriented, which means you have the personality of a Promoter!")

    def view_c_score(self):
        print(f"C stands for Introvert & Task Oriented, which means you have the personality of a Analyser!")

    def view_s_score(self):
        print(f"S stands for Introvert & People Oriented, which means you have the personality of a Analyser!")

    def menu(self):
        print(f"Welcome JS's DISC Personality Assessment Application.")
        print("[1] - View My Profile Information")
        print("[2] - Perform My Personality Assessment")
        print("[3] - Read My Own Personality Traits")
        print("[4] - Read About Others Personality Traits")
        print("[5] - Check My Compatibility")
        print("[0] - Exit")

        
        option = int(input("What would you like to do today : "))
        
        while option != 0:
            
            if option == 1:
                self.print_info()

            elif option == 2:             
                self.personality_assessment()

            elif option == 3:
                print("Read Own Personality Traits")
                
            elif option == 4:
                print("Read about others Personality Traits")
                
                
            elif option == 5:
                print("Check my compatibility")

            else:
                print("Please Choose Available Options on Screen")

            print()
            self.menu()
            option = int(input("What would you like to do today : "))
        
        
        main()
        print("See you again soon!")


def main():
    person  = Person()
    print("Welcome to JS's DISC Application Beta - (Version 1)")
    print("[1] Sign Up For A New Account")
    print("[2] Login to Existing Account")
    print("[0] Exit")
    option = int(input("Hi, what would you like to do today? "))
    while option !=0:
        if option == 1:
            print("Creating New Account with JS's DISC Application!")
            person.create_new_account()

        elif option ==2:
            print("User Login")
            login = person.login_account(account_id=int(input("Key-In Your ID ")),password=input("Enter Your Password "))
            print(login)
            if login == True:
                person.menu()
                print("Getting to the menu")
            elif login == False:
                main()
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