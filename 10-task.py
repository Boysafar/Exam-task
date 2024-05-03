"""
Implement a Python program to handle an Error exception that might occur. - A
"""


def divide_numbers():
    try:
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))

        result = numerator / denominator

        print(f"The result of {numerator} / {denominator} is: {result}")
    except :
        # Handling division by zero error
        print("Error: Division by zero is not allowed.")

    finally:
        print("Menga barbr !!!")


# Run the division function
divide_numbers()
