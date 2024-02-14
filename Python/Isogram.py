import re
def is_isogram(word):
    scrubbed = re.compile('[^a-zA-Z]').sub('', word).lower()
    return len(set(scrubbed)) == len(scrubbed)