import random


def getdigits(number):
    li=[]
    for i in str(number):
        li.append(int(i))
    return li


def noduplicate(number):
    numli=getdigits(number)
    if len(numli)==len(set(numli)):
        return True
    else:
        return False

def generatenum():
    while True:
        number=random.randint(1000,9999)
        if noduplicate(number):
            return number




def noofbullscows(number, guess):
    if number==guess:
        return [0,4]
    bull,cow=0,0
    numli=getdigits(number)
    guessli=getdigits(guess)
    for i in range(0,len(guessli)):
        if numli[i]==guessli[i]:
            cow+=1
        else:
            if guessli[i] in numli:
                bull+=1
    return [bull,cow]


number=generatenum()
print(number)
while True:
    guess = int(input("enter your guess"))
    if not noduplicate(guess):
        print("Number should not have repeated digits. Try again.")
        continue
    if guess < 1000 or guess > 9999:
        print("Enter 4 digit number only. Try again.")
        continue
    bullcow=noofbullscows(number,guess)
    if bullcow[1]==4:
        print("Your Guess Is Correct")
        break
    else:
        print(f"{bullcow[0]} bulls ans {bullcow[1]} cows")



