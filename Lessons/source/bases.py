#!python
import math
import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    #Key strings and their value
    #Jamie helped me with this
    characters = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "A":10, "B":11, "C":12, "D":13, "E":14, "F":15, "G":16, "H":17, "I":18, "J":19, "K":20, "L":21, "M":22, "N":23, "O":24, "P":25, "Q":26, "R":27, "S":28, "T":29, "U":30, "V":31, "W":32, "X":33, "Y":34, "Z":35}

    #Digits changed to uppercase string
    digits = str(digits).upper()
    basee_10 = 0
    
    #Binds tuple produced by enumerate to power, and num
    for power, num in enumerate(digits[::-1]):
        # finds the value for the digit 
        selected_digit = characters[num]
                #adding the result of base *  power tim base_10
        basee_10 += selected_digit * math.pow(base, power)
    return basee_10


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    #we want the number we get to make it a string if necessary
    characters = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f', 16:'g', 17:'h', 18:'i', 19:'j', 20:'k', 21:'l', 22:'m', 23:'n', 24:'o', 25:'p', 26:'q', 27:'r', 28:'s', 29:'t', 30:'u', 31:'v', 32:'w', 33:'x', 34:'y', 35:'z'}
    number_basee = ''
    
    while number is not 0:
        # The modulo assigns the remainder of number / base
        remainderr = number % base
        #Assigned the indices value to its place in the digit dictionary
        indices_value = characters[remainderr]
        
        #Adds the number base value to the indice value
        # number_base_value = 0
        number_basee = indices_value + number_basee
        
        #Assigns the number minus the remainer to the variable
        number_minus_remainder = number - remainderr
        
        number = int(number_minus_remainder/base)

    return number_basee


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)

    decoded_number = decode(digits, base1)
    encoded_number = encode(decoded_number, base2)

    return encoded_number

def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignores the script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()