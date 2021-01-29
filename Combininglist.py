from prettytable import PrettyTable


https://www.youtube.com/watch?v=gryi-dcF_mY
x = PrettyTable()

mystring = x.get_string()

print(x.get_string(fields=["City name","Population"]))
print(x.get_string())



# from prettytable import from_csv

# with open("database_disc.csv") as fp:
#     mytable = from_csv(fp)

#     print(mytable)
#print(x.get_string(fields=["City name", "Population"]))



# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# new_list = list1.extend(list2)
# print(new_list)