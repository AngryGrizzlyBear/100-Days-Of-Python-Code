print('''
      
                                   /\
                              /\  //\\
                       /\    //\\///\\\        /\
                      //\\  ///\////\\\\  /\  //\\
         /\          /  ^ \/^ ^/^  ^  ^ \/^ \/  ^ \
        / ^\    /\  / ^   /  ^/ ^ ^ ^   ^\ ^/  ^^  \
       /^   \  / ^\/ ^ ^   ^ / ^  ^    ^  \/ ^   ^  \       *
      /  ^ ^ \/^  ^\ ^ ^ ^   ^  ^   ^   ____  ^   ^  \     /|\
     / ^ ^  ^ \ ^  _\___________________|  |_____^ ^  \   /||o\
    / ^^  ^ ^ ^\  /______________________________\ ^ ^ \ /|o|||\
   /  ^  ^^ ^ ^  /________________________________\  ^  /|||||o|\
  /^ ^  ^ ^^  ^    ||___|___||||||||||||___|__|||      /||o||||||\       |
 / ^   ^   ^    ^  ||___|___||||||||||||___|__|||          | |           |
/ ^ ^ ^  ^  ^  ^   ||||||||||||||||||||||||||||||oooooooooo| |ooooooo  |
ooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
      
'''
)

print("Welcome to Treasure Mountain!")
print("Your mission is to find the treasure.")

choices = input("Do you want to go left or right? ").lower()
if choices == "right":
    print("You fell into a hole and died! Game Over!")
elif choices == "left":
    print("You've gone left and you see a pool of water!")
    choice2 = input("Do you choose to swim or wait? ").lower()
    if choice2 =="swim":
        print("You swam in the water, but an weird water creature eats you! You died! Game Over!")
    elif choice2 =="wait":
        print("Because you waited, three magical doors appeared!")
        choice3 = input("The color of the doors are Red, Blue, and Yellow. Which color door do you pick? ").lower()
        if choice3 =="red":
            print("Flames burst from the door and set you on fire. You burned to death! You DIED! Game Over!")
        elif choice3=="blue":
            print("Beast Spring out from the blue door and rip you apart! You died as dinner for them! Game Over!")
        elif choice3=="yellow":
            print("The yellow door spits out a mountain of treasure! You win!")
else:
    print("You died!")
   
   



