# **Write a Python code to replace all emojis
# (starting with `"("` and ending with `")"`) with `"[emoji]"`
# in the following text record.**
import re
text_rec = """
A: Congratulations!(＾∇＾)(｡ì _ í｡) You've won a $1,000 Walmart gift card. Go to http://bit.ly/d3FJe1 to claim now.
B: I am good. Nice try!(^_^)
C: Your tax refund is pending acceptance.(>.<) Must accept within 24 hours: http://bit.ly/fIhE3W16432
B: Why is everyone trying to scam me!! (///▽///)
"""

pattern = r"\(.*?\)"
# search for characters after each '(' until reaching the first ')'
repl = ''
text = re.sub(pattern,repl,text_rec)
print(text)