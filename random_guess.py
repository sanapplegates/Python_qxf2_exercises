import random

def random_generator():
    random_number   = random.randrange(1,10)
    return random_number

def user_guess(user_number):
    user_number =   int(input("Enter user number:"))
    return user_number


def validate_guess(random_number):
    


if __name__ == "__main__":
    "find the correct guess of random number"
    random_number   =   random_generator()
    user_number  =   user_guess()
    validate_guess(random_number)
