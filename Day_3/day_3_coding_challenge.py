# Write a Pizza Delifery Program
# Congratulations, you've got a job a Python Pizza!
# Your first job is to build an automatic pizza order
# program.

# Based on a user's order, work out their first bill. 
# Use the input() function to get a user's preference and then# add up the total
# for their order and tell the how much they have to pay.

# Small pizza (S) $15
# Medium Pizza (M) 20
# Large Pizza (L) 25

# Add pepperoni for small pizza (Y or N) +$2
# Add pepperoni for medium or large pizza (Y or N) +$3
# Add extra cheese for any size pizza (Y or N) + $1

bill = 0

print("Welcome to Python Pizza Deliveries!")
order = input("Do you want a pizza? Y / N ").lower()

if order == "y":
 size = input("What size do you want? S, M, or L: ").lower()


 if size == "s":
    bill = 15
 elif size == "m":
    bill = 20 
 elif size == "l":
    bill = 25

 pepperoni = input("Do you want Pepperoni on your pizza? Y or N: ").lower()
 if pepperoni == "y" and size == "s":
    bill += 2
 else:
    bill += 3

 extra_cheese = input("Do you want extra cheese? Y or N: ").lower() 
 if extra_cheese == "y":
    bill += 1
    
 print(f"Your total is ${bill}")

else:
    print("You didn't order a pizza!")








