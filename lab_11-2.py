#Author JS Lab 11-2 1/31/2023

grades = {"Mid Year Project Presentation":93, "Mid Year Project Proposal": 100, "Mid Year Porject Code": 94, "Mid Year Project Reflection": 93}

print("Your grades are: " + str(grades.values()))                   #Print all grades

for k in grades:                                                    #Print the names of each assignment on different lines
    print(k)


print("Your grades of 70 and above are: ")                          #Print names and grades above 70
for k,v in grades.items():
    if v >= 70:
        print("Class: ", k, "Grade: ", v)


for k,v in grades.items():                                          #Print names and grades of 50 and below
    if v <= 50:
        print("Your grades of 50 and below are: ")
        print("Class: ", k, "Grade: ", v)