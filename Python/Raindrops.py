def convert(number):
    returnString=""
    if number % 3 == 0:
        returnString = returnString + "Pling"
    if number % 5 == 0:
        returnString = returnString + "Plang"
    if number % 7 == 0:
        returnString = returnString + "Plong"
    if returnString != "":
        return returnString
    return str(number)