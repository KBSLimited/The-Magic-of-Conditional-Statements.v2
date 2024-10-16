#Task 1: Identify the Greatest
def find_largest_number(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        num3 = float(input("Enter the third number: "))
        
        largest_number = find_largest_number(num1, num2, num3)
        print("The largest number is:", largest_number)
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()

#Task 2: Identify the Smallest
def find_largest_number(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

def find_smallest_number(num1, num2, num3):
    if num1 <= num2 and num1 <= num3:
        return num1
    elif num2 <= num1 and num2 <= num3:
        return num2
    else:
        return num3

def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        num3 = float(input("Enter the third number: "))
        
        largest_number = find_largest_number(num1, num2, num3)
        smallest_number = find_smallest_number(num1, num2, num3)
        
        print("The largest number is:", largest_number)
        print("The smallest number is:", smallest_number)
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()

# Task 3: Equality Check
def find_largest_number(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

def find_smallest_number(num1, num2, num3):
    if num1 <= num2 and num1 <= num3:
        return num1
    elif num2 <= num1 and num2 <= num3:
        return num2
    else:
        return num3

def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        num3 = float(input("Enter the third number: "))
        
        if num1 == num2 == num3:
            print("All numbers are equal.")
        elif num1 == num2:
            print("The first and second numbers are equal.")
            print("The third number is different.")
        elif num1 == num3:
            print("The first and third numbers are equal.")
            print("The second number is different.")
        elif num2 == num3:
            print("The second and third numbers are equal.")
            print("The first number is different.")
        else:
            largest_number = find_largest_number(num1, num2, num3)
            smallest_number = find_smallest_number(num1, num2, num3)
        
            print("The largest number is:", largest_number)
            print("The smallest number is:", smallest_number)
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()