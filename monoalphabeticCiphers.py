from helpfulFunctions import text_clean, text_block

def caesar(text, key, decrypt = False, LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    message = ""
    text = text_clean(text)
    if decrypt == True:
        for char in text:
            number = LETTERS.find(char)
            keyNumber = (number - key) % len(LETTERS)
            message += LETTERS[keyNumber]
        message = message.lower()
    elif decrypt == False:
        text = text.upper()
        for char in text:
            number = LETTERS.find(char)
            keyNumber = (number + key) % len(LETTERS)
            message += LETTERS[keyNumber]
        message = text_block(message)
    return(message)

def multiplicative_cipher(text, key, decrypt = False, LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    text = text_clean(text)  
    ciphertext = ""
    plaintext = ""
    message = ""
    key_inv = pow(key, -1, len(LETTERS))

    if decrypt == False:
        for char in text:
            number = LETTERS.find(char)
            keyNumber = (number * key) % len(LETTERS)
            message += LETTERS[keyNumber]
            ciphertext = text_block(message)
        return(ciphertext)
    elif decrypt == True:
        for char in text:
            number = LETTERS.find(char)
            keyNumber = (number * key_inv) % len(LETTERS)
            plaintext += LETTERS[keyNumber]
        return(plaintext.lower())

def affine_cipher(text, mKey, aKey, decrypt = False, LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    """ For decryption purposes set mKey to either a known used key or a list with your assumptions on letters
        List Format: [CipherTextLetter1, PlainTextLetter1, CipherTextLetter2, PlainTextLetter2]
        Also, set aKey to any value and the text to the ciphertext (Can be left blank if you're just looking for
        keys)

        When using for encryption, mKey = multiplicative key as an integer and aKey = additive key as an integer.
        Text is the plaintext being used for encryption purposes.
    """
    message = ""
    multiplicativeKey = False
    text = text_clean(text)
    modulus = len(LETTERS)
    
    if decrypt == False:
        for i in range(1, modulus):
            if mKey * i % modulus == 1:
                multiplicativeKey = True
                mKeyInv = i
                break
            else:
                multiplicativeKey = False
        if multiplicativeKey == True:
            for char in text:
                number = LETTERS.find(char)
                keyNumber = (number * mKey + aKey) % modulus
                message += LETTERS[keyNumber]
        else:
            return("Invalid Multiplicative Key: " + str(mKey))
        return("Multiplicative Key: " + str(mKey) + "\n" + "Additive Key: " + str(aKey) + "\n" +"Ciphertext: " + "\n" + text_block(message))
    elif decrypt == True:
        if type(mKey) == int:
            km = mKey
            ka = aKey
            if km >= modulus:
                km = km % modulus
            if ka >= modulus:
                ka = ka % modulus
        if type(mKey) != int:
            if len(mKey) == 4:
                CTL1 = LETTERS.find(mKey[0].upper()) #Finding associated value for letters given CTL = Ciphertext letter; PTL = Plaintext Letter
                PTL1 = LETTERS.find(mKey[1].upper())
                CTL2 = LETTERS.find(mKey[2].upper())
                PTL2 = LETTERS.find(mKey[3].upper())
                PTV = (PTL1 - PTL2) % modulus #Finding value for Plaintext after the equations are subtracted
                CTV = (CTL1 - CTL2) % modulus #Finding value for Ciphertext after the equations are subtracted
                for x in range(1, modulus + 1):
                    if (x * PTV) % modulus == CTV:
                        km = x
                        break
                    elif x == modulus:
                        return("Letter Combination Doesn't Reveal a Valid Multiplicative Key: " + str(mKey)) + "\n" + "Try a Different Combination"
                for j in range(1, modulus):
                    if (km * PTL1 + j) % modulus == CTL1:
                        ka = j
                        break
            else:
                return("Invalid Letter Combination: " + str(mKey))
        for i in range(1, modulus + 1):
            if km * i % modulus == 1:
                mKeyInv = i
                break
            elif i == modulus:
                return("Letter Combination Doesn't Reveal a Valid Inverse Key: " + str(mKey)) + "\n" + "Try a Different Combination"
        if len(text) > 0:
            for char in text:
                number = LETTERS.find(char)
                keyNumber = ((number - ka) * mKeyInv) % modulus
                message += LETTERS[keyNumber]
            return("Multiplicative Key: " + str(km) + "\n" + "Additive Key: " + str(ka) + "\n" + "Plaintext: " + "\n" + message.lower())
        else:
            return("Multiplicative Key: " + str(km) + "\n" + "Additive Key: " + str(ka))