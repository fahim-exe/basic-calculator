import calculator as Cal

num1 = input("Enter the first number: ")

while True:
    
    num1 = float(num1)
    print("choose operations: +, -, *, /")
    op = input()
    num2 = input("Enter second number: ")
    num2 = float(num2)

    if op=="+":
        result = Cal.add(num1, num2)
        print(result)

    if op=="-":
        result = Cal.sub(num1, num2)
        print(result)

    if op=="*":
        result = Cal.mul(num1, num2)
        print(result)

    if op=="/":
        result = Cal.div(num1, num2)
        if result==None:
            break
        else:
            print(result)


    chk = input(f"Type 'y' to continue with {result}, or type 'n' to start a new calculation or 'q' to exit : ")

    if chk.lower()=="y":
        num1 = result

    if chk.lower()=="n":
        num1 = input("Enter the first number: ")

    if chk.lower()=="q":
        break

    else:
        chk = input("Enter a valid input: ")








    
    