
#calculate the bmi of user


#user height in kg
def bmi_input():
    weight = int(input("Enter weight:"))
    height  =   int(input("Enter height:"))
    return(weight,height)



def bmi_calculate(weight,height):
    bmi = weight//(height *height)
    if(bmi < 18):
        print("bmi is:", bmi,"underweight")
    elif (bmi >18 and bmi < 25):
        print("bmi is:",bmi,"Normal")
    else:
        print("bmi is:",bmi,"overweight")




if __name__ == "__main__":
    #weight = int(input("Enter weight: "))
    #height  =   int(input("Enter height: "))
    weight,height   = bmi_input()
    print("height: ",height,"weight:",weight)
    bmi_calculate(weight,height)


