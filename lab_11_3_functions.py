#Author JS Lab 11-3 2/1/2023

#1                                                                                              #15+ Lines
def food_info(foods):
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

#2                                                                                              #While Loop + Input + List
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

#3                                                                                              #Dictionary + Enumerate
    def indexed_names(names_list):
        [str(index) + ": " + name for index, name in enumerate(names_list)]
    return

#4                                                                                              #Inputs
def add_numbers():
    num1 = input("Please input a number: ")
    num2 = input("Please input another number: ")
    sum = int(num1) + int(num2)
    return sum

#5                                                                                              #For Loop + List
def double_stuff (stuff):
    for index, var in enumerate(stuff):
            stuff[index] = var*2
    return(stuff)

#6                                                                                              #List
def indexed_names (names):
    for index, vars in enumerate(names):
        namex = [*vars] 
        #recombining the lists into a string
        namex.insert(0, str(index)+": ")
        names[index] = "".join(namex)
    return (names)

#7                                                                                              #15+ lines + Built in functions
def find_missing_number(sequence):
    try:
        numbers = set(map(int, sequence.split()))
    except ValueError:
        answer = 1
    else:
        answer = 0
        if numbers:
            top = max(numbers)
            for n in range(1, top):
                if n not in numbers:
                    answer = n
                    break
    
    return answer

#8 
def solution(number):                                       # 15+ lines
    sum=0
    if number%3==0:
        nearest_three=number-3
    else:
        nearest_three=number-(number%3)
    if number%5==0:
        nearest_five=number-5
    else:
        nearest_five=number-(number%5)
    for x in range(nearest_three, 0, -3):
        sum+=x
    for y in range(nearest_five, 0, -5):
        if y%3==0:
            continue
        else:
            sum+=y
    return sum

#9                                                         #15+ Lines
def hamming_distance(a, b):
    count = 0
    bin_a = str(bin(a))
    bin_b = str(bin(b))
    list_a = [i for i in bin_a]
    list_b = [i for i in bin_b]
    while len(list_a) != len(list_b):
        if len(list_a) > len(list_b):
            list_b.insert(2, "0")
        if len(list_b) > len(list_a):
            list_a.insert(2, "0")
    for i in range(2, len(list_a)):
        if list_a[i] != list_b[i]:
            count += 1
    return count

#10                                                         #15+ Lines + Enumerate + Build in functions
def sum_of_integers_in_string(s):
    result = 0
    current = ""
    for i,char in enumerate(s):
        if i != len(s) - 1:
            if char.isnumeric():
                current += char
            else:
                if len(current) >= 1:
                    result += int(current)
                    current = ""
        else:
            if char.isnumeric():
                if current:
                    current += char
                    result += int(current)
                else:
                    result += int(char)
            else:
                if current:
                    result += int(current)
    return result