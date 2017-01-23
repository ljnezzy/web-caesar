def alphabet_position(letter):
    letterLower=(letter.lower())
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letterPos = alphabet.index(letterLower)
    return (letterPos)

def rotate_character(char, rot):
    char = str(char)
    if char.isalpha():
        rotate=(alphabet_position(char)+rot)
        rotate = rotate % 26
        if char != char.upper():
            alphabet = 'abcdefghijklmnopqrstuvwxyz'
            return (alphabet[rotate])
        else:
            alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            return (alphabet[rotate])
    else:
        return (char)

def encrypt(text, rot):
    encrypt_lib=[]
    for char in text:
        encrypt_lib.append(rotate_character(char,rot))
    return(''.join(encrypt_lib))
