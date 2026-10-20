def functionOne():
    print("My student ID is jorkee0238")

def functionTwo():
    num1 = int(input("Please enter a number: "))
    num2 = int(input("Please enter a number: "))
    total = num1 + num2
    print(f"The sum of {num1} and {num2} is {total}")
    return total

def functionThree(total):
    if total > 5:
        print("The sum is greater than 5.")
    else:
        print("The sum is less than 5.")
    studentID = '0238'
    return studentID

def main():

    #This function displays the student ID
    functionOne()

    #This function will take the two numbers the user inputs and adds them together
    total = functionTwo()

    #This function determines if teh sum is greater than or less than 5 and let the user now plus stores the numbers from the student ID
    studentID = functionThree(total)

    print(f"functionThree returned the value of {studentID}")

main()
    


