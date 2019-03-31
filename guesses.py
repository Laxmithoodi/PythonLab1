import random
secret = random.randint(1,99)
print("Guess Secret number:", secret)
past_guesses ={}
guess = -1

while guess != secret:
    guess = int(input("make a guess:"))
    if guess in past_guesses:
        past_guesses[guess]==1
        print("You guessed that", past_guesses[guess], 'times')
    else:
        past_guesses[guess]=1
        if guess>secret:
            print("Guess is too high")
        elif guess < secret:
            print("Guess is low")
        else:
            print ("correct guess")