# Sample Coding Questions 01 Week 01
# Jamshaid Mirpour

# Defining Variables
numbers = [1, 4, 7, 9]

# Order of Operations
a, b, c, d = 1, 2, 3, 4

# Fully-bracketed version of:
# e = a - b ** c // d + a % c
e = (a - ((b ** c) // d)) + (a % c)

# Formatting (1 line, no hard-coded extra zeros)
temperature = 32.6
print("The temperature today is: {:.3f} degrees Celsius".format(temperature))

# Common Functions
userAge = int(input("Enter your age: "))
userAge = userAge + 22
print("Now showing the shop items filtered by age: {}".format(userAge))
