import Math
def calculate_square_root(number):
    return Math.sqrt(number)
number = float(input("Enter a number to find its square root: "))
result = calculate_square_root(number)
print(f"The square root of {number} is {result}")
