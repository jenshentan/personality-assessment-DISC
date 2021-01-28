import pandas as pd

raw_data = {
    "name" : ["John", "Mike", "Melvin", "Suresh"],
    "python" : [45,100,100,45],
    "java" : [95,32,14,100],
    "c++" : [23,11,10,0],
    "asm" : [0,0,0,0]
    
}

student = pd.DataFrame(raw_data)

print(student)
