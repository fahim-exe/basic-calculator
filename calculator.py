def add(num1, num2):
    result = num1+num2

    return result

def sub(num1, num2):
    result = num1-num2
    return result

def mul(num1, num2):
    result = num1*num2
    return result

def div(num1, num2):
    if num2==0:
        print("Can not divide by zero!!!!")
        return
    
    else:
        result = num1/num2
        return result

