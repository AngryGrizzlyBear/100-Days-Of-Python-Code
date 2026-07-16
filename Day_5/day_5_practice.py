# fruits = ['Apple', 'Peach', 'Pear']

# for fruit in fruits:
#     print(fruit + " pie")

# student_scores = [45, 112, 78, 156, 23, 189, 67, 134, 91, 175, 38, 148, 82, 119, 56]

# current_highest = student_scores[0]

# print(current_highest)

# for student in student_scores:
#     if student > current_highest:
#         current_highest = student
#     else:
#         print(f"Student Number {current_highest} beats {student}")

# print(f"Student Number {current_highest} wins!")

# total = 0
# for number in range(1, 101):
#     total += number


# print(total)

for number in range (1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 5 == 0:
        print("buzz")
    elif number % 3 == 0 :
        print("fizz")
    else:
        print(number)