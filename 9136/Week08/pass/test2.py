""""
Activity 2:

Write a Python program to find sequences of lowercase letters joined with an underscore.
"""
import re
def text_find(text):
    patterns = '^[a-z]+_[a-z]+$'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return ('Not matched!')
    #matchList = re.search(patterns, text)
    #print(matchList)


# testing
text_find("aab_cbbbcaab_AbbbcAaab_abbbcssss_ddddd")
text_find("aab_Abbbc")
text_find("Aaab_abbbc")