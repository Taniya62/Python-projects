print("Welcome to my Computer Quiz!!")
playing = input ("Do you want to Play? ")
print (playing)

if playing.lower() !="yes":
    quit()

print ("okey! lets start")

score = 0

answer = input ("What does CPU stands for? ").lower ()
if answer =="central Processing unit":
    print('Correct!')
    score +=1
else:
    print("Incorrect, lets try again")

answer = input ("What does GPU stands for? ").lower()
if answer == "graphic processing unit":
    print("Correct!")
    score +=1

else:
    print("Incorrect, lets try again")

Answer = input ("What does RAM stands for? ").lower()
if Answer == "random access myemory":
    print("Correct!")
else:
    print("Incorrect, lets try again")

print("you got " + str(score) + "questions correct!")

print("you got " + str((score/3)*100) + "%.")