import random as r

random_number = r.randint(1,100)
tries = 0 
maximum_tries = 10

print ("====================Number Guessing Game========================")

def guess_game(maximum_tries,tries,random_number):
    while(tries < 10):
        number = input("Please enter the number between 1 to 100: ")
        if number == random_number:
            return "You have guessed the number, You won 😍🙌"
        elif number < random_number:
            maximum_tries -=  1
            print("Go Higher   -------",maximum_tries," chances are left")
            tries += 1
        elif number > random_number:
            maximum_tries -=  1
            print("Go Lower    -------",maximum_tries," chances are left")
            tries += 1
        else :
            print("You lost, You loooooooooooooserrrrrrrrrrrrrrrrrr 🤙")

print(guess_game(maximum_tries,tries,random_number))