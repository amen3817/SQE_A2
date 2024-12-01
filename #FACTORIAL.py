#FACTORIAL

def function_factorial(n):
    if n == 0:
        result = 1
    else: result = n * function_factorial(n-1)
    
    return result

num = int(input("Please enter a number"))
#num = int(num)
print(function_factorial(num))