# - this comment
print("Hello, word!")

# ** - exponentiation
# // - integer division with decimals discarded
# % - division for module (remainder of the division)
# / - division
# * - multiplication
# - - subtraction
# + - addition
print(23 % 7)
print(2**5)
print(25//4)

# int() - conversion to integer
# '' - string
# float() - conversion to floating point number
# variable declaration:
my_name = 'DANIIL'
my_surname = 'NIKIFOROV'
my_age = 20
print(my_name + ' ' + my_surname)
print(my_name + ' ' + my_surname + ' ' + str(my_age))
# easier:
print(f"{my_name} {my_surname} {my_age}")
print((my_name + " ") * 5)

# Variable is an area memory at computer, which can storing single value
color = 'green'

print(color)
_ = my_age
print(_)
# len() - length
print(len(my_name))

my_name = input('Input name:')
print(f"Hello, {my_name}!")