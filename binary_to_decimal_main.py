# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from binary_to_decimal import binary_to_decimal

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    while True:
        try:
            binary = input("Type binary that you want to convert into a decimal: ")
            decimal = binary_to_decimal(binary)
            print(decimal)
            break
        except ValueError:
            print("Please enter a binary number")

