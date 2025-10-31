def text_clean(text, LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    message = ""
    for letter in text:
        letter = letter.upper()
        if letter in LETTERS:
            message += letter
    return(message.upper())

def text_block(text, n = 5):
    message = ""
    counter = 1
    for char in text:
        if counter % n == 0:
            message += char + " "
        else:
            message += char
        counter += 1
    return(message.strip())

def gcd(a, b):
    if a == 0 or b == 0:
        if a > b:
            b = a
        elif a < b:
            a = b
    elif a != b:
        while a != b:
            while a > b:
                a -= b
            while b > a:
                b -= a
    return(a)