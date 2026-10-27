import random as r

target_number = r.randint(1,100)
maximum_chances = 10

def GuessNumber(maximum_chances,target_number):
    guesses = []
    while (maximum_chances > 0):
        seen = False
        choosenNumber = int(input("Please enter the number between 1 to 100:  "))
        for i in range(len(guesses)):
            if choosenNumber == guesses[i]:
                seen = True
        if seen == False:
            guesses.append(choosenNumber)
            maximum_chances -= 1
        if target_number == choosenNumber:
            return (f"Winner Winner Chicken Dinner. {choosenNumber} was right. Genius! 🥳")
        elif seen == True:
            print (f"{choosenNumber} is already choosen before. No chances gone ⚠️")
            print (f"{maximum_chances} are remaining") 
        elif target_number > choosenNumber:
            print (f"Go Higher . {choosenNumber} is small. Choose wisely! noob. 🤣")
            print (f"{maximum_chances} are remaining ❌")
        elif target_number < choosenNumber:
            print (f"Go Lower . {choosenNumber} is big. Choose wisely! noob 🤣")
            print (f"{maximum_chances} are remaining ❌")
    return (f"Game Over!. You lost noooooooob!.The number was {target_number} ❌")

print(GuessNumber(maximum_chances,target_number))