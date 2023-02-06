#Author JS Lab 11-3 2/1/2023

#1                                                                                              #15+ Lines
def add_foods(foods):
    sixth_letter = []
    not_foods = []
    short_foods = []

    for food in foods:
        try:
            if len(food) >= 6:
                sixth_letter.append(food[5])
            else:
                short_foods.append(food)
        except TypeError:
            not_foods.append(food)

    print("Sixth Letter:", str(sixth_letter))
    print("Not Foods:", str(not_foods))
    print("Short Foods:", str(short_foods))

#2                                                                                              #While Loop + Input
def add_nums(numbers):
    while True:
        user_input = input("Enter a number: ")
        try:
            user_input = int(user_input)
            break
        except ValueError:
            print("Invalid input. Please enter a number on a keypad.")
            print("passed list: " + str(numbers) + " user input: " + str(user_input))
    result = [num + user_input for num in numbers]
    print("passed list: " + str(numbers) + " user input: " + str(user_input))
    print(result)

#3                                                                                              #Dictionary + Enumerate Loop
    def indexed_names(names_list):
        [str(index) + ": " + name for index, name in enumerate(names_list)]
    return

#4                                                                                              #Inputs
def add_numbers():
    num1 = input("Please input a number: ")
    num2 = input("Please input another number: ")
    sum = int(num1) + int(num2)
    return sum

#5                                                                                              #For Loop
def double_stuff (stuff):
    for index, var in enumerate(stuff):
            stuff[index] = var*2
    return(stuff)

#6                                                                                              #List
def indexed_names (names):
    for index, vars in enumerate(names):            #break each name into a list
        namex = [*vars] 
        #recombining the lists into a string
        namex.insert(0, str(index)+": ")
        names[index] = "".join(namex)
    return (names)