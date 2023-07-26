from math import factorial

def encode_string(string, base):
    base_36 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encoded_string = ""
    hash_sum = 0

    for character in string:
        factorial_utf8 = factorial(ord(character))
        factorial_reduction = 1/(len(string)**(1/2))
        hash_sum += int(factorial_utf8**factorial_reduction)

    while hash_sum > 0:
        encoded_string += base_36[hash_sum%base]
        hash_sum = hash_sum//base

    encoded_string = encoded_string[::-1]

    return encoded_string