a=int(input("Please enter a number to chose a door\n1 for the left door and 2 for the right door.\n"))
if a==1:
    print("Great!Chose the door again.")
    b=int(input())
    if b==1:
        print("You win the game.Congratulations!")
    else:
        print("Oh no!You are blocked.")
else:
    print("Oh no!You are blocked.")
