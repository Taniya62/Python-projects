import random
top_of_range = input ("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int (top_of_range )

    if top_of_range <=0:
        print ('please enter a number larger than 0 next time')
        quit()
else:
    print ("Please enter a number next time.")
    quit()

r = random.randrange(0,top_of_range) #generate random number 1 to 10
guess = 0
while True:
    guess +=1
    user_guess = input ("make a guess: ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("please type a number next time.")
        continue
    if user_guess ==r:
        print("you got it!")
        break
    else:
        print("you got it wrong!")

    
print ("you got it in", guess, "guess")
