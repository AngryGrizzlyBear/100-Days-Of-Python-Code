# print(150 * 1.12) / 5)

print("Welcome to the tip calculator!")

total_bill = float(input("How much was the bill? "))
total_tip = int(input("How much tip would you like to give? 10, 12, 15? "))
total_people = int(input("How many people want to split the bill? "))
end_result = (total_bill * (1 + total_tip / 100)) / total_people
print(f"Each person should pay: ${end_result:.2f}")