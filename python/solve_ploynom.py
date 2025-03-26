from sympy import sympify

def solve():
    x, value = map(int, input().split())  # Read x and expected result
    expression = input().strip()  # Read polynomial expression

    # Securely parse and evaluate the expression
    result = sympify(expression).subs("x", x)  
    # result = eval(expression)


    return result == value  # Return True if it matches, False otherwise

print(solve())  # Run function and print result
