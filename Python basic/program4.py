# simple calculator
# +, -, /, //, %, **, *

while(True):
    print(f"{'press q to quit':_^30}")
    response = input("Do you want to quit?")
    if(str(response) == 'q'):
        break
    else:
        operater_response = input("choose an operation: \n'+', '-', '*', '/', '//', '**', '%' : ")
        num1 = float(input("enter first no. : "))
        num2 = float(input("enter second no. : "))
        if(operater_response == '+'):
            print(f"{num1} {operater_response} {num2} is {num1 + num2}")
        elif(operater_response == '-'):
            print(f"{num1} {operater_response} {num2} is {num1 - num2}")
        elif(operater_response == '*'):
            print(f"{num1} {operater_response} {num2} is {num1 * num2}")
        elif(operater_response == '/'):
            print(f"{num1} {operater_response} {num2} is {num1 / num2}")
        elif(operater_response == '//'):
            print(f"{num1} {operater_response} {num2} is {num1 // num2}")
        elif(operater_response == '**'):
            print(f"{num1} {operater_response} {num2} is {num1 ** num2}")
        elif(operater_response == '%'):
            print(f"{num1} {operater_response} {num2} is {num1 % num2}")
        else:
            print("invalid operator")
        
    
