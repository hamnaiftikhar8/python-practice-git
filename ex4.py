try:
    number = int(input("Enter a number to check if its even or odd."))
    assert number % 2 == 0

except ValueError:
    print("THe value must be an integer.")
    
except AssertionError:
    print("It is not an even number")

else:
    square = number ** 2
    print(square)