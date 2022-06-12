
print("Welcome to Basic Calculator")


while True:

    print("Starting up Calculator")
    operation = input("Enter an Operation you'd like to perform: [+,-,/, *]")

    
    try:
        no1 = float(input("Enter the first number: "))
        no2 = float(input("Enter the second number: "))

    except:
        print("Please enter a valid number!")
        continue


    if operation == "+" :
        print(no1 + no2)


    elif operation == "-" :
        print(no1 - no2)
    
    
    elif operation == "*" :
        print(no1 * no2)
    
    
    elif operation == "/" :
        print(no1 / no2)
   
   
    else:
   
        print("please enter a valid Operator!!!")

    choice = input("Would you like to perform another Operation? [yes,no]: ").lower()
    if choice != "yes":
        break
    

print("Thanks for Using the Calcualtor")
