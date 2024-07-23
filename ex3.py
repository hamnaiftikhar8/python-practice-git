import random


numbers = input("ENter number")
numbers_list = []

for i in range(int(numbers)):
    numbers_list.append(random.randint(20,50))

print(f"The number is : {numbers_list} \nso lets check if its even or odd.")

for num in numbers_list:
    if num % 2 == 0:
        print(f"The number {num} is even.")
    else:
        print(f"THe number {num} is odd.")
