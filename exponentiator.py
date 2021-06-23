#Takes the base and exponent and evaluates
def exponentiate(base, exponent):
    product = base ** exponent
    print(product)

#Asks for an integer, raises to the fourth power
def raised_to_fourth_power(base2):
    product2 = exponentiate(base2,4)

#Squares a number
square = lambda x : exponentiate(x,2)

#Cubes a number
cube = lambda y : exponentiate(y,3)

#Outputs
square(2)
cube(2)
raised_to_fourth_power(2)
