import random
while True:
    ComputerChoice = random.choice([-1, 0, 1])
    YourStr = input("Enter Your Choice in terms of 'SNAKE', 'WATER' or 'GUN' (or 'QUIT' to exit): ").lower()

    if YourStr == "quit":
        print("Thanks for playing... Goodbye!");
        break

    YourDictionary = {"snake": -1, "water": 0, "gun": 1}
    YourReverseDictionary = {-1: "snake", 0: "water", 1: "gun"}

    YourChoice = YourDictionary.get(YourStr)

    if YourChoice is None:
        print("Invalid Input! Please choose from 'snake', 'water', or 'gun'.");
        continue 
    
    print(f"Your Choice is {YourReverseDictionary[YourChoice]} \nComputer choice is {YourReverseDictionary[ComputerChoice]}")

    if YourChoice == ComputerChoice:
        print("Tie! Both have chosen the same.");
        
    elif (ComputerChoice == 0 and YourChoice == 1):
        print("You Win!");
    elif (ComputerChoice == 0 and YourChoice == -1):
        print("You Lose!");
    elif (ComputerChoice == 1 and YourChoice == -1):
        print("You Win!");
    elif (ComputerChoice == 1 and YourChoice == 0):
        print("You Lose!");
    elif (ComputerChoice == -1 and YourChoice == 0):
        print("You Win!");
    elif (ComputerChoice == -1 and YourChoice == 1):
        print("You Lose!");
