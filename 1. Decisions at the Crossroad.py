number = input("Enter a number: ")

# Convert the input to an integer or float for comparison
number = float(number)  # You can use int() if you want to restrict to integers

if number > 0:
    print("The number is positive.")
elif number == 0:  # Use '==' for equality comparison
    print("The number is zero.")
else:  # No condition needed here; it's implied that number < 0
    print("The number is negative.")