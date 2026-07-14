# This file will house all the algorithms for generating questions

## Imports 
import random 

## Adding the base (formatting)
SUBSCRIPTS = {
    "0": "₀", "1": "₁", "2": "₂", "3": "₃", "4": "₄",
    "5": "₅", "6": "₆", "7": "₇", "8": "₈", "9": "₉"
}

def to_subscript(string):
    return "".join(SUBSCRIPTS.get(char, char) for char in string)

def format_with_base(number, base):
    return f"{number}{to_subscript(str(base))}"

print(format_with_base(67, 8))

## The number generators:

### The interger number generators 
def p_integer_number_generator(): # positive integer number generator
    return random.randint(0, 256) # includes 0 and 256

def n_integer_number_generator(): # negative integer number generator
    return random.randint(-256, -1) # includes -256 and -1

### The floating point number generators
def p_float_number_generator(): # positive float number generator
    return round(random.uniform(0, 256), 3) # includes 0 and 256

def n_float_number_generator(): # negative float number generator
    return round(random.uniform(-256, -1), 3) # includes -256 and -1

# Positive conversion algorithms:

## The denary to binary conversion algorithm (positive numbers)
def den_to_bin():
    denary = p_integer_number_generator() # generate a random positive integer
    binary = bin(denary)[2:] # convert to binary (python has a built in function) and remove the '0b' prefix
    return denary, binary

print(den_to_bin()) # testing the function

## The binary to denary conversion algorithm (positive numbers)
def bin_to_den():
    denary = p_integer_number_generator() # generate a random positive integer
    binary = bin(denary)[2:] # convert to binary (python has a built in function) and remove the '0b' prefix
    return binary, denary

print(bin_to_den()) # testing the function

## The denary to octal conversion algorithm (positive numbers)
def den_to_oct():
    denary = p_integer_number_generator() # generate a random positive integer
    octal = oct(denary)[2:] # convert to octal (python has a built in function) and remove the '0o' prefix
    return denary, octal

print(den_to_oct()) # testing the function