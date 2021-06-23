#Asks the user for their name, inputs as string variable
def name_input():
    print("Please enter your name. ")
    provided_name = input()
    return provided_name

#Inserts the name into the greeting
def greet(name):
    print("Hello! How are you, ", name, "?")

greet(name_input())


