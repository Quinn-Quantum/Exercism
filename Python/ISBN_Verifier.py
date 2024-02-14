import re
import string
def is_valid(isbn):
    number = 10 
    summe = 0
    alphabet = string.ascii_uppercase
    isX = False
    isbn = re.sub("\-", "", isbn)
    if len(isbn) < 10 or len(isbn) > 10:
        return False
    if isbn[-1] == 'X':
        isX = True
        isbn = isbn.replace("X", "10")
    for leter in isbn:
        if leter in alphabet:
            return False
    
    for i in isbn:
        x = 0
        if isX and number == 1:
            x = 10 * number
        elif number > 0:
            x = int(i)*number
        summe = summe + x
        number -= 1
    if summe % 11 == 0:
       return True
    else:
        return False