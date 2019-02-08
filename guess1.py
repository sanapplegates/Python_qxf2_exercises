import random
secret_number = random.randint(1,100)

print(secret_number)
guessed_number = int(input("enter guess number: "))

if(guessed_number == secret_number):
    print("yes,you are right")

elif(guessed_number <   secret_number):
    print("you are wrong, It is lesser than the secret number")

else:
    print(" you are wrong, guess number is greater than secret number")
