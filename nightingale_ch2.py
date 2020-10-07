a = ("A. Weekly net pay calculation")
b = ("B. Decimal Numbers Comparison")
q = ("Q. Quit")

print(a)
print(b)
print(q)
#Net pay calculation
selection = str(input("Please enter your selection: ")).lower()

while selection != "q":

    if selection == "a":
        my_name = input("Please enter your name: ")
        pay = input("Please enter your pay rate: ")
        dependents = input("Please enter the number of your dependents: ")

        print("**** Weekly Tax and Net Pay ****")
        print("================================")

# These are the conversions
        dependents_float = float(dependents)
        pay_float = float(pay)
        gross_pay = pay_float * 40

# These are the calculations
        fed_tax = 0.2 * (gross_pay - dependents_float * 0.35)
        state_tax = (0.025 * gross_pay)
        net_pay = (gross_pay - fed_tax - state_tax)

# These are the print statements
        print("Name : " + my_name)
        print("Gross pay : " + str(gross_pay))
        print("Federal Tax : " + str(fed_tax))
        print("State Tax : " + str(state_tax))
        print("Net Pay : " + str(net_pay))
        break
#Decimal numbers comparison
    elif selection == "b":
        number1 = input("Please enter the first decimal number: ")
        number2 = input("Please enter the second decimal number: ")
        if number1 > number2:
            print(float(number1))
        elif number2> number1:
            print(float(number2))
        elif number1 == number2:
            print("Two numbers are equal")
        break
    else:
        print("You have a wrong selection, please try again.")
    selection = str(input("Please enter your selection: ")).lower()
print("Thank you for using the program. Good-bye!!")
input("press enter to close the program !!!")
