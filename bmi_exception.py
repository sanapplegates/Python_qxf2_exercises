"""
# calculate the bmi of user


# user height in kg
print("Enter the user's weight(kg):")
weight  =   int(input())


# user height in metres
print("Enter the user's height(metre) :")
height  =   int(input())


# Body Mass Index of user
bmi =  float(weight/(height*height))
print("bmi of user:",bmi)

if  bmi < 18:
    print("Underweight")10
elif    bmi > 18.5 and bmi < 24.9:
    print("Normal")
elif    bmi >25  and bmi    <   29.9:
    print("overweight")
else:
    print("obesity")

"""


def user_input(weight):
    while True:    
        try:
            weight = float(input("Enter weight: "))
            break
        except ValueError:
            print("wrong values ")   
            
        return weight




# Program starts here
if __name__ == "__main__":
    """ It takes users  weight and height"""
    weight,height = 0,0
    weight = user_input(weight)
