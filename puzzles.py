# This file will house all the algorithms for generating questions

## Imports 
import random 

## The number generators:

### The interger number generators 
def p_integer_number_generator(): # positive integer number generator
    return random.randint(0, 255) # includes 0 and 255 (the range of an 8-bit unsigned integer)

def twoscomp_integer_number_generator(): # Positive and negative integer number generator
    return random.randint(-128, 127) # includes -128 and 127 (the range of an 8-bit signed integer)

### The sign bit, exponent and mantissa generators
def sign_bit_generator(): # sign bit generator
    return random.randint(0, 1) # includes 0 and 1 (the range of a sign bit)
def exponent_generator(): # exponent generator
    return random.randint(1, 6) # includes 1 and 6 (the range of a 3-bit exponent)
def mantissa_generator(): # mantissa generator
    return random.randint(0, 15) # includes 0 and 15 (the range of a 4-bit mantissa)

## Adding the base (formatting)
SUBSCRIPTS = {
    "0": "₀", "1": "₁", "2": "₂", "3": "₃", "4": "₄",
    "5": "₅", "6": "₆", "7": "₇", "8": "₈", "9": "₉"
}

def to_subscript(string):
    return "".join(SUBSCRIPTS.get(char, char) for char in string)

def format_with_base(number, base):
    return f"{number}{to_subscript(str(base))}"

# Question functions:
# Denary to binary, binary to denary, denary to octal, octal to denary, denary to hexadecimal, hexadecimal to denary

## The denary to binary conversion questions 
def den_to_bin():
    # Back end calculations
    denary = p_integer_number_generator() # generate a random positive integer
    binary = bin(denary)[2:] # convert to binary (python has a built in function) and remove the '0b' prefix


    # Front end (formatting the question and response)
    ## Question
    def den_to_bin_question():
        question = f"Convert {format_with_base(denary, 10)} to binary."
        return question
    
    ## Response
    def den_to_bin_response():
        answer = format_with_base(binary, 2)
        response = f"The answer is {answer}"
        return response
    
    return den_to_bin_question(), den_to_bin_response()

# print(den_to_bin())

## The binary to denary conversion questions
def bin_to_den():
    # Back end calculations
    denary = p_integer_number_generator() # generate a random positive integer
    binary = bin(denary)[2:] # convert to binary (python has a built in function) and remove the '0b' prefix


    # Front end (formatting the question and response)
    ## Question
    def bin_to_den_question():
        question = f"Convert {format_with_base(binary, 2)} to denary."
        return question
    
    ## Response
    def bin_to_den_response():
        answer = format_with_base(denary, 10)
        response = f"The answer is {answer}"
        return response
    
    return bin_to_den_question(), bin_to_den_response()

# print(bin_to_den())

## The denary to octal conversion questions
def den_to_oct():
    # Back end calculations
    denary = p_integer_number_generator() # generate a random positive integer
    octal = oct(denary)[2:] # convert to octal (python has a built in function) and remove the '0o' prefix


    # Front end (formatting the question and response)
    ## Question
    def den_to_oct_question():
        question = f"Convert {format_with_base(denary, 10)} to octal."
        return question
    
    ## Response
    def den_to_oct_response():
        answer = format_with_base(octal, 8)
        response = f"The answer is {answer}"
        return response
    
    return den_to_oct_question(), den_to_oct_response()

# print(den_to_oct())

## The octal to denary conversion questions
def oct_to_den():
    # Back end calculations
    denary = p_integer_number_generator() # generate a random positive integer
    octal = oct(denary)[2:] # convert to octal (python has a built in function) and remove the '0o' prefix


    # Front end (formatting the question and response)
    ## Question
    def oct_to_den_question():
        question = f"Convert {format_with_base(octal, 8)} to denary."
        return question
    
    ## Response
    def oct_to_den_response():
        answer = format_with_base(denary, 10)
        response = f"The answer is {answer}"
        return response
    
    return oct_to_den_question(), oct_to_den_response()

# print(oct_to_den())

## The denary to hexadecimal conversion questions
def den_to_hex():
    # Back end calculations
    denary = p_integer_number_generator() # generate a random positive integer
    hexadecimal = hex(denary)[2:].upper() # convert to hexadecimal [uppercase] (python has a built in function) and remove the '0x' prefix


    # Front end (formatting the question and response)
    ## Question
    def den_to_hex_question():
        question = f"Convert {format_with_base(denary, 10)} to hexadecimal."
        return question
    
    ## Response
    def den_to_hex_response():
        answer = format_with_base(hexadecimal, 16)
        response = f"The answer is {answer}"
        return response
    
    return den_to_hex_question(), den_to_hex_response()

# print(den_to_hex())

## The hexadecimal to denary conversion questions
def hex_to_den():
    # Back end calculations
    denary = p_integer_number_generator() # generate a random positive integer
    hexadecimal = hex(denary)[2:].upper() # convert to hexadecimal (python has a built in function) and remove the '0x' prefix


    # Front end (formatting the question and response)
    ## Question
    def hex_to_den_question():
        question = f"Convert {format_with_base(hexadecimal, 16)} to denary."
        return question
    
    ## Response
    def hex_to_den_response():
        answer = format_with_base(denary, 10)
        response = f"The answer is {answer}"
        return response
    
    return hex_to_den_question(), hex_to_den_response()

# print(hex_to_den()) 

# Binary to octal, octal to binary, binary to hexadecimal, hexadecimal to binary

def bin_to_oct():
    # Back end calculations
    denary = p_integer_number_generator() # generate a random positive integer
    binary = bin(denary)[2:] # convert to binary (python has a built in function) and remove the '0b' prefix
    octal = oct(denary)[2:] # convert to octal (python has a built in function) and remove the '0o' prefix

    # Front end (formatting the question and response)
    ## Question
    def bin_to_oct_question():
        question = f"Convert {format_with_base(binary, 2)} to octal."
        return question
    
    ## Response
    def bin_to_oct_response():
        answer = format_with_base(octal, 8)
        response = f"The answer is {answer}"
        return response
    
    return bin_to_oct_question(), bin_to_oct_response()

# print(bin_to_oct())

def oct_to_bin():
    # Back end calculations
    denary = p_integer_number_generator() # generate a random positive integer
    binary = bin(denary)[2:] # convert to binary (python has a built in function) and remove the '0b' prefix
    octal = oct(denary)[2:] # convert to octal (python has a built in function) and remove the '0o' prefix

    # Front end (formatting the question and response)
    ## Question
    def oct_to_bin_question():
        question = f"Convert {format_with_base(octal, 8)} to binary."
        return question
    
    ## Response
    def oct_to_bin_response():
        answer = format_with_base(binary, 2)
        response = f"The answer is {answer}"
        return response
    
    return oct_to_bin_question(), oct_to_bin_response()

# print(oct_to_bin())

def bin_to_hex():
    # Back end calculations
    denary = p_integer_number_generator() # generate a random positive integer
    binary = bin(denary)[2:] # convert to binary (python has a built in function) and remove the '0b' prefix
    hexadecimal = hex(denary)[2:].upper() # convert to hexadecimal [uppercase] (python has a built in function) and remove the '0x' prefix

    # Front end (formatting the question and response)
    ## Question
    def bin_to_hex_question():
        question = f"Convert {format_with_base(binary, 2)} to hexadecimal."
        return question
    
    ## Response
    def bin_to_hex_response():
        answer = format_with_base(hexadecimal, 16)
        response = f"The answer is {answer}"
        return response
    
    return bin_to_hex_question(), bin_to_hex_response()

# print(bin_to_hex())

def hex_to_bin():
    # Back end calculations
    denary = p_integer_number_generator() # generate a random positive integer
    binary = bin(denary)[2:] # convert to binary (python has a built in function) and remove the '0b' prefix
    hexadecimal = hex(denary)[2:].upper() # convert to hexadecimal [uppercase] (python has a built in function) and remove the '0x' prefix

    # Front end (formatting the question and response)
    ## Question
    def hex_to_bin_question():
        question = f"Convert {format_with_base(hexadecimal, 16)} to binary."
        return question
    
    ## Response
    def hex_to_bin_response():
        answer = format_with_base(binary, 2)
        response = f"The answer is {answer}"
        return response
    
    return hex_to_bin_question(), hex_to_bin_response()

# print(hex_to_bin())

# Octal to hexadecimal, hexadecimal to octal

def oct_to_hex():
    # Back end calculations
    denary = p_integer_number_generator() # generate a random positive integer
    octal = oct(denary)[2:] # convert to octal (python has a built in function) and remove the '0o' prefix
    hexadecimal = hex(denary)[2:].upper() # convert to hexadecimal [uppercase] (python has a built in function) and remove the '0x' prefix

    # Front end (formatting the question and response)
    ## Question
    def oct_to_hex_question():
        question = f"Convert {format_with_base(octal, 8)} to hexadecimal."
        return question
    
    ## Response
    def oct_to_hex_response():
        answer = format_with_base(hexadecimal, 16)
        response = f"The answer is {answer}"
        return response
    
    return oct_to_hex_question(), oct_to_hex_response()

# print(oct_to_hex())

def hex_to_oct():
    # Back end calculations
    denary = p_integer_number_generator() # generate a random positive integer
    octal = oct(denary)[2:] # convert to octal (python has a built in function) and remove the '0o' prefix
    hexadecimal = hex(denary)[2:].upper() # convert to hexadecimal [uppercase] (python has a built in function) and remove the '0x' prefix

    # Front end (formatting the question and response)
    ## Question
    def hex_to_oct_question():
        question = f"Convert {format_with_base(hexadecimal, 16)} to octal."
        return question
    
    ## Response
    def hex_to_oct_response():
        answer = format_with_base(octal, 8)
        response = f"The answer is {answer}"
        return response
    
    return hex_to_oct_question(), hex_to_oct_response()

# print(hex_to_oct())

# Two's complement questions (8 bit signed integers)
def den_to_twoscomp():
    # Back end calculations
    denary = twoscomp_integer_number_generator() # generate a random positive or negative integer
    if denary >= 0:
        twoscomp = format(denary, '08b') # convert to binary (python has a built in function) and format to 8 bits
    else:
        twoscomp = format((1 << 8) + denary, '08b') # convert to two's complement binary (python has a built in function) and format to 8 bits

    # Front end (formatting the question and response)
    ## Question
    def den_to_twoscomp_question():
        question = f"Convert {format_with_base(denary, 10)} to two's complement."
        return question
    
    ## Response
    def den_to_twoscomp_response():
        answer = format_with_base(twoscomp, 2)
        response = f"The answer is {answer}"
        return response
    
    return den_to_twoscomp_question(), den_to_twoscomp_response()

# print(den_to_twoscomp())

# Two's complement to denary questions (8 bit signed integers)
def twoscomp_to_den():
    # Back end calculations
    denary = twoscomp_integer_number_generator() # generate a random positive or negative integer
    if denary >= 0:
        twoscomp = format(denary, '08b') # convert to binary (python has a built in function) and format to 8 bits
    else:
        twoscomp = format((1 << 8) + denary, '08b') # convert to two's complement binary (python has a built in function) and format to 8 bits

    # Front end (formatting the question and response)
    ## Question
    def twoscomp_to_den_question():
        question = f"Convert {format_with_base(twoscomp, 2)} to denary."
        return question
    
    ## Response
    def twoscomp_to_den_response():
        answer = format_with_base(denary, 10)
        response = f"The answer is {answer}"
        return response
    
    return twoscomp_to_den_question(), twoscomp_to_den_response()

# print(twoscomp_to_den())

# Floating point number questions (Mantissa and exponent representation)

## Simple floating point representation (8 bits total)

### The structure is: [sign bit] [Exponent] [Mantissa] 
### 1 sign bit, 3 bits for the exponent, 4 bits for the mantissa (8 bits total)
### The response should be in the form [sign bit] [Exponent] [Mantissa] (e.g. 0 011 1010, where [sign bit] is the first bit, [Exponent] is the next 3 bits, and [Mantissa] is the last 4 bits)

### Add the floating point representation question functions here: float to binary, binary to float

#####################################################################################################################

# Answer checker


