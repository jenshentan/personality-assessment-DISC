import os 
import csv
from colorama import Fore, Back, Style

class Person:

    def __init__(self):
        pass

        def new_personality_assessment(self):
        print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        print(Fore.GREEN +"I am a good listener")
        while True:
            try:
                s1 = int(input(self))
            except ValueError:
                print("Only Numbers between 1 - 5 are allowed")
                continue
            if s1 < 1:
                print("Your value must be between 1 -5")
                continue
            elif s1 >5:
                print("Your value must be between 1 -5")
                continue
            else:
                break
        return s1

    def read_file_data(self):
        pass

    def new_account_creation(self):
        pass

    def login(self):
        pass

    def interface_menu(self):
        pass



class Admin(Person):
    def __init__(self):
        pass

    def view_all_users(self):
        pass

    def view_one_user(self):
        pass

    def delete_one_user(self):
        pass

    def create_new_user(self):
        pass

    def view_quadrants_statistics(self):
        pass


class User(Person):

    def __init__(self):
        pass



    def view_own_personlity(self):
        pass

    def read_others_quadrants(self):
        pass

    def compatibility_check(self):
        pass

    def save_files(self):
        pass

    def family_assessment(self):
        pass



# def main():
#     pass

# if __name__ == '__main__':
#     main()
