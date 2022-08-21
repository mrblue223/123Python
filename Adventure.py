name = input("Type your name: ")
print("welcome", name, "to my wild adventure")

anwser = input("you are on a dirt road, and yo are comming to an end go left or right? ").lower()
if anwser == "left":
    anwser = input("You come to a river do u wish to swim or walk ")
    
    if anwser == "swim":
        print("You swam across and were eaten by an alligator")
        
    elif anwser == "walk":
        print("You walk many miles and run out of water and die")
        
    else:
        print("Not a walid anwser, You lose")
    
elif anwser == "right":
    anwser = input("you came to a bridge it look wably do you want to cross or go back ")
    
    if anwser == "cross":
        anwser = input("You cross the bridge and meet a stranger do you wish to talk to them? ")
        
        if anwser =="yes":
            print("You have talked to the stranger you win")
        
        elif anwser =="no":
            print("You ignored the stranger and u lose")
            
        else:
            print("not a valid option you lose")
        
        
        
        
    elif anwser == "back":
        print("You go back to the main road")
        
    else:
        print("Not a walid anwser, You lose")


else:
    print("Not a valid anwser, You lose")
    


    
