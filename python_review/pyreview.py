# Exercise 1.1
# Call the print function to say "Hello world!"
# Open this folder (python-review) in the terminal
# Use the python or python3 command to run this file and check the output
print("Hello world!")

# Exercise 1.2
# Create a variable: name
# Assign it a string value, the name of a friend
# Call the print function, pass it the variable you just made contcatenated with a string
# so that it prints a greeting to your friend
# Use the python or python3 command to run this file and check the output
name = "Nhat Do"
print(f"{name} is my friend")


# Exercise 1.3
# Define a function named greeting, with one parameter: friend
# Inside the function, call print, make it say Hello to your friend
# Call the function and pass it a string containing a friend's name
# Use the python or python3 command to run this file and check the output

def greeting(friend):
    print(f"Hello {friend}")


greeting(name)
