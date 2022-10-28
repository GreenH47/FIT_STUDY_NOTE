#Activity 1
import re
def text_match(text):
        patterns = '[A-Z]+[a-z]'
        if re.search(patterns, text):
                return 'Found a match!'
        else:
                return('Not matched!')
#testing
print(text_match("AaBbGg"))
print(text_match("Python"))
print(text_match("python"))
print(text_match("PYTHON"))
print(text_match("aA"))
print(text_match("Aa"))