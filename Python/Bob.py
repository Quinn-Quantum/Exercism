def response(hey_bob):
    if hey_bob == "" or hey_bob.isspace():
        return "Fine. Be that way!"
    elif hey_bob.strip()[-1] == '?'  and not hey_bob.isupper() :
        return "Sure." 
    elif hey_bob[-1] == '?' and hey_bob.isupper() :
        return "Calm down, I know what I'm doing!" 
    elif hey_bob.isupper() :
        return "Whoa, chill out!" 
    else:
        return "Whatever."