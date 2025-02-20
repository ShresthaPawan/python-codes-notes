import random
while True:
    print("Welcome to the Number Guessing Game, design by SPACE X")
    ask=input("Do you want to play now:")
    if ask=="yes":
        com=random.randint(1,5)
        ask_1=int(input("Enter the number from 1 to 5:"))
        if ask_1<=5 and ask_1>=1:
            print("The number of computer is ",com)
            if ask_1==com:
                print("You made it!")
            elif ask_1>com:
                print("Your number is high")
            elif ask_1<com:
                print("Your number is low")
        else:
                print("Invalid, You tried to break the rule, so you are disqualified!")
                break
    else:
        print("Bye, have a Good day")  
        break; 
