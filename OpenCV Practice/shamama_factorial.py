
def factorial(x):
    x_factorial = 1
    for i in range(1,x+1):
        x_factorial = x_factorial * i
    return x_factorial

def factorial_recursive(x):
    if x < 2:
        return 1
    return x * factorial_recursive(x-1)

def fibonacci(n): 
    if n < 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def index_the_grid(elements_per_row, list_of_elements, row_number, column_number):
    return list_of_elements[row_number * elements_per_row + column_number]

print(factorial(6))