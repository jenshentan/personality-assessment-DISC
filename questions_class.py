from colorama import Fore, Back, Style

class Person:



    def __init__(self):
        self.score_list = None
        

        

    def new_personality_assessment(self):


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

        score_list = [d_score,i_score,s_score,c_score]
        #sort large to small list

        print(score_list)
        print("=================\n")

        lowest = min(score_list)
        highest = max(score_list)
        print(f"Lowest{lowest}")
        print("=================\n")
        print(f"Highest{highest}")

        print("=================\n")

        print("Your Results")
        print("Your main personality is ........")

        new_dictionary = {
            "Controller" : d_score,
            "Promoter" : i_score,
            "Analyzer" : c_score,
            "Supporter" : s_score
        }

        #Smallest to Largest
        sorted_new_dict = dict(sorted(new_dictionary.items(),key=lambda item:item[1]))

        #Largest to smallest
        sorted_new_dict_2 = {k:v for k,v in sorted(new_dictionary.items(),key=lambda item: item[1], reverse=True)}
        print(new_dictionary)
        print("=================\n")
        print(sorted_new_dict)
        print("=================\n")
        print(sorted_new_dict_2)

        self.score_list = sorted_new_dict_2
        

        # print(Fore.YELLOW +"Rate Yourself Between 1-5 on the following statement")
        # print(Fore.GREEN +"I am a good listener")
        # while True:
        #     try:
        #         d1 = int(input(self))
        #     except ValueError:
        #         print("Only Numbers between 1 - 5 are allowed")
        #         continue
        #     if d1 < 1:
        #         print("Your value must be between 1 -5")
        #         continue
        #     elif d1 >5:
        #         print("Your value must be between 1 -5")
        #         continue
        #     else:
        #         break
        # return d1

person = Person()
person.new_personality_assessment()