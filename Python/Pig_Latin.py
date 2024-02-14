
# Online Python - IDE, Editor, Compiler, Interpreter
def translate(text):
    newWordList=""
    wordList = text.split()
    size = len(wordList)
    print(size)
    if len(wordList) > 1:
        for word in wordList:
            newWordList = newWordList + " " + changeWord(word)
            print(newWordList)
        newWordList = newWordList[1:]
        print(newWordList)
        return newWordList
    else:
        print("hier")
        return changeWord(text)
      

def changeWord(text):
    text_low = text.lower()
    if isVowel(text_low[0]) or text_low[0:2] == "xr" or text_low[0:2] == "yt":
        text = text + "ay"
        return text
    if not isVowel(text_low[0]):
        
        if (text_low[0:2] == "ch" or text_low[0:2] == "st" or text_low[0:2] == "qu" or text_low[0:2] == "th" or text_low[0:2] == "rh") and not text_low[0:3] == "thr":
            x = text[0:2]
            text = text[2:] + x + "ay"
            return text
        elif text_low[0:3] == "sch" or text_low[0:3] == "squ" or text_low[0:3] == "thr":
            x = text[0:3]
            text = text[3:] + x + "ay"
            return text
        else:
            x = text[0]
            text = text[1:] + x + "ay"   
            return text
    
def isVowel(char):
    return char.lower() in 'aeiou'
    
