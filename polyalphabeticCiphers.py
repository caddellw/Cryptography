from helpfulFunctions import text_clean, text_block

import numpy as np

def tabula_recta(text, keyword, decrypt = False, LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    text = text_clean(text)
    keyword = text_clean(keyword)
    ciphertext = ""
    plaintext = ""
    if decrypt == False:
        for i in range(0, len(text)):
            plaintext_number = LETTERS.find(text[i])
            keyword_number = LETTERS.find(keyword[i])
            ciphertext_number = (plaintext_number + keyword_number) % len(LETTERS)
            ciphertext += LETTERS[ciphertext_number]

        return(text_block(ciphertext))
    elif decrypt == True:
        for i in range(0, len(text)):
            ciphertext_number = LETTERS.find(text[i])
            keyword_number = LETTERS.find(keyword[i])
            plaintext_number = (ciphertext_number - keyword_number) % len(LETTERS)
            plaintext += LETTERS[plaintext_number]
        return(plaintext.lower())
    
def vigenere_cipher(text, keyword, decrypt = False, LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    text = text_clean(text)
    keyword = text_clean(keyword)
    key = keyword
    ciphertext = ""
    plaintext = ""
    addchar = 0
    if len(keyword) < len(text):
        addchar = len(text) - len(keyword)
    for i in range(0, addchar):
        a = i % len(keyword)
        key += keyword[a]
    if decrypt == False:
        for i in range(0, len(text)):
            plaintext_number = LETTERS.find(text[i])
            keyword_number = LETTERS.find(key[i])
            ciphertext_number = (plaintext_number + keyword_number) % len(LETTERS)
            ciphertext += LETTERS[ciphertext_number]

        return("Ciphertext: " + text_block(ciphertext) + "\n" + "Keyword: " + keyword)
    elif decrypt == True:
        for i in range(0, len(text)):
            ciphertext_number = LETTERS.find(text[i])
            keyword_number = LETTERS.find(key[i])
            plaintext_number = (ciphertext_number - keyword_number) % len(LETTERS)
            plaintext += LETTERS[plaintext_number]
            
        return("Plaintext: " + plaintext.lower() + "\n" + "Full Key:  " + key + "\n" + "Keyword:   " + keyword)
    
def auto_key_cipher(text, primer, decrypt = False, LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    text = text_clean(text)
    primer = text_clean(primer)
    key = primer
    ciphertext = ""
    plaintext = ""
    addchar = 0
    counter = 0
    if decrypt == False:
        if len(primer) < len(text):
            addchar = len(text) - len(primer)
        for num in range(0, addchar):
            key += text[num]
        for i in range(0, len(text)):
            plaintext_number = LETTERS.find(text[i])
            keyword_number = LETTERS.find(key[i])
            ciphertext_number = (plaintext_number + keyword_number) % len(LETTERS)
            ciphertext += LETTERS[ciphertext_number]

        return("Ciphertext: " + text_block(ciphertext) + "\n" + "Key: " + key)
    elif decrypt == True:
        if len(primer) < len(text):
            addchar = len(text) - len(primer)
        while len(key) != len(text):
            plaintext = ""
            for i in range(0, len(key)):
                ciphertext_number = LETTERS.find(text[i])
                keyword_number = LETTERS.find(key[i])
                plaintext_number = (ciphertext_number - keyword_number) % len(LETTERS)
                plaintext += LETTERS[plaintext_number]
            if counter != addchar:
                if counter >= len(plaintext):
                    break
                else:
                    key += plaintext[counter]
                    counter += 1
        plaintext = ""
        for i in range(0, len(text)):
                ciphertext_number = LETTERS.find(text[i])
                keyword_number = LETTERS.find(key[i])
                plaintext_number = (ciphertext_number - keyword_number) % len(LETTERS)
                plaintext += LETTERS[plaintext_number]
        return("Plaintext: " + plaintext.lower() + "\n" + "Key: " + key)

#Code Related to Solving the Hill Cipher
def keygen(keyword, LETTERS='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    keyword = text_clean(keyword, LETTERS)
    length = len(keyword)
    grid_size = int(np.sqrt(length))
    array_numbers = []
    for i in range(length):
        array_numbers.append(LETTERS.find(keyword[i]))
    return(np.array(array_numbers).reshape(grid_size, grid_size))

def valid_key(A, LETTERS='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    if A.shape[0] == A.shape[1] and round(np.linalg.det(A)) != 0 and pow(round(np.linalg.det(A)), -1, len(LETTERS)) != False:
        return(True)
    else:
        return(False)

def hill_textclean(message, block_size, LETTERS='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    message = text_clean(message, LETTERS)
    while len(message) % block_size != 0:
        message += "X"
    return(message)

def hill_inverse(K, n):
    K_adj = np.linalg.det(K) * np.linalg.inv(K)
    K_adj = K_adj.round().astype(int)
    determinant = round(np.linalg.det(K))
    determinant_inverse = pow(determinant, -1, n)
    K_inv = (determinant_inverse * K_adj) % n
    return(K_inv)

def hill(keyword, block_size, message, decrypt=False, LETTERS='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    key = keygen(keyword, LETTERS)
    if valid_key(key, LETTERS) == False:
        return(False)
    message = hill_textclean(message, block_size, LETTERS)
    array_numbers = []
    block_counter = 0
    block = []
    ciphertext = ""
    plaintext = ""
    if decrypt == False:
        for i in range(len(message)):
            block.append(LETTERS.find(message[i]))
            block_counter += 1
            if block_counter == block_size:
                block_counter = 0
                array_numbers.append(block)
                block = []
                array_numbers = np.array(array_numbers).reshape(block_size, 1)
                ciphertext_block = np.dot(key, array_numbers) % len(LETTERS)
                ciphertext_block = ciphertext_block.tolist()
                for j in range(block_size):
                    ciphertext += LETTERS[ciphertext_block[j][0]]
                array_numbers = []
        return(text_block(ciphertext))
    else:
        key_inv = hill_inverse(key, len(LETTERS))
        for k in range(len(message)):
            block.append(LETTERS.find(message[k]))
            block_counter += 1
            if block_counter == block_size:
                block_counter = 0
                array_numbers.append(block)
                block = []
                array_numbers = np.array(array_numbers).reshape(block_size, 1)
                plaintext_block = np.dot(key_inv, array_numbers) % len(LETTERS)
                plaintext_block = plaintext_block.tolist()
                for l in range(block_size):
                    plaintext += LETTERS[plaintext_block[l][0]]
                array_numbers = []
        return(plaintext.lower())
