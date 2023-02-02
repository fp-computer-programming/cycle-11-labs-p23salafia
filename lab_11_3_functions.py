#Author JS Lab 11-3 2/1/2023

#1
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

#2
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

#3
    def indexed_names(names_list):
        return [str(index) + ": " + name for index, name in enumerate(names_list)]

#4 
def add_numbers(num1, num2):
    sum = num1 + num2
    return sum