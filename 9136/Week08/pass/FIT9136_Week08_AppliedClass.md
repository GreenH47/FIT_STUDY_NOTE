# FIT9136 - Week 8 Applied Session

## Table of Contents:

1. [* Exercise 1: Introduction to RE](#exercise-1)
2. [* Exercise 2: TXT to CSV](#exercise-2)
3. [* Exercise 3: Body-Mass Index (BMI) Calculation?](#exercise-3)

### * Exercise 1:  Introduction to RE<a class="anchor" id="exercise-1"></a>
#re #regular-expression #regex

<div class="alert alert-block alert-success">

<blockquote>
This module provides regular expression matching operations ... -<a href='https://docs.python.org/3/library/re.html'>Python 3 Docs</a>
</blockquote>

So, now we know we need to import **`re`** library in order to use regular expressions. 

</div>


```python
# importing the regular expresion library
import re
```

<div class="alert alert-block alert-success">

### Commonly used methods
    
</div>

<div class="alert alert-block alert-success">

#### **A.** `re.search(pattern, string, flags=0)`

<blockquote>
Scan through string looking for the <b>first</b> location where the regular expression pattern produces a match, and return a corresponding match object. -Python 3 Doc
</blockquote>

</div>


```python
# searching 'abc' from '1234abc5678derg abc'
search_string = '1234abc5678derg abc'
pattern = 'abc'

result = re.search(pattern, search_string)

print("result:", result)
print("result.span():", result.span())
# the index location of 'abc' is from 4(inclusive) to 7(exclusive)
print("search_string[result.span()[0]: result.span()[1]] => search_string[4:7]:", 
      search_string[result.span()[0]: result.span()[1]]) 
```

    result: <re.Match object; span=(4, 7), match='abc'>
    result.span(): (4, 7)
    search_string[result.span()[0]: result.span()[1]] => search_string[4:7]: abc



```python
# searching '2bc' from '1234abc5678derg'
search_string = '1234abc5678derg'
pattern = '2bc'

# if pattern not found, None is returned from re.search
result = re.search(pattern, search_string)
print("result:", result) 
```

    result: None


<div class="alert alert-block alert-success">


#### **B.** `re.findall(pattern, string, flags=0)`
<blockquote>
Return all <b>non-overlapping matches</b> of pattern in string, as a list of strings or tuples. -Python 3 Doc
</blockquote>
    
</div>


```python
search_string = '1234abc5678 dergabc 30374 abcr3g'
pattern = 'abc'

result = re.findall(pattern, search_string)
print(result) # all 'abc's found in search_string as a list
```

    ['abc', 'abc', 'abc']


<div class="alert alert-block alert-success">

#### **C.** `re.sub(pattern, repl, string, count=0, flags=0)`

<blockquote>
Return the string obtained by replacing the <b>leftmost non-overlapping occurrences</b> of pattern in string by the replacement repl. If the pattern isn’t found, string is returned unchanged. -Python 3 Doc
</blockquote>

</div>


```python
search_string = '1234abc5678 dergabc 30374 abcr3g'

pattern = 'abc'
repl = '   '

result = re.sub(pattern, repl, search_string)
print(result) # the replaced string
```

    1234   5678 derg    30374    r3g


<div class="alert alert-block alert-success">

### Regular Expressions

Now we know some of the methods implemented in the re library. However, what actually are regular expressions?

<blockquote>
A regular expression (shortened as regex or regexp...) is a sequence of characters that specifies a search pattern. - Wikipedia
</blockquote>

Some useful tools to test/visualise the regex:
1. [regex101](https://regex101.com/): a webapp to test your regex
2. [Regexper](https://regexper.com/): regex visualisation tool

</div>

<div class="alert alert-block alert-success">
    
#### <b>Basic Syntax: A query string</b>

- e.g.: `r"abc"` if we want to search "abc" (Simply the string you want to search after you press *ctrl+F* or *Command+F*)
    
<font color='red'><b>Question:</b></font> What does the `r` before the quote specify?
    
</div>


```python
str1 = "abc\n"
print(str1)
```

    abc
    



```python
str2 = r"abc\n"
print(str2)
```

    abc\n


<div class="alert alert-block alert-success">

<font color='red'><b>Answer:</b></font> ??

</div>

<div class="alert alert-block alert-success">

#### <b>(Some) Special characters in regex</b>

- `.` (Dot): Wildcard. Can be any character except newline characters.
- `?`(Question Mark): Can match Zero or one occurrences of the character.
- `*` (Star): Causes the resulting RE to match 0 or more repetitions of the preceding RE, as many repetitions as are possible. The '\*' qualifier is *greedy*; it matches as much text as possible. 
    - Adding `?` after the `*` makes it *lazy*; as few characters as possible will be matched.
    - e.g. `r"ab*"` will match ‘a’, ‘ab’, or ‘a’ followed by any number of ‘b’s.

![image.png](data:image/png;base64,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)

</div>    


```python
# Dot
search_string = '11 1. Rand0M $trinG'

pattern = r'1.'

result = re.search(pattern, search_string)
print(result)

# Question: What if we want to search '1.' from "11 1. Rand0M $trinG" literally?
# Answer: put a \ before . to escape wildcard, same applies to escape all other special characters in regex
pattern = r'1\.'

result = re.search(pattern, search_string)
print(result)
```

    <re.Match object; span=(0, 2), match='11'>
    <re.Match object; span=(3, 5), match='1.'>



```python
# Question Mark (?)
txt = "AB1234 ABN ABC ABDC"

#Search for a sequence that starts with "AB", followed by 0 or 1  (N) character:

x = re.findall("ABN?", txt)

print(x)
```

    ['AB', 'ABN', 'AB', 'AB']



```python
# Star (*)
search_string = '11 1. Rand0M $trinG'

# searching for strings with 0 or more characters 
# using combination of .*
pattern = r'.*' 

result = re.findall(pattern, search_string)
print(result)
```

    ['11 1. Rand0M $trinG', '']



```python
# Let's see the greedy and Lazy expression work
search_string = '11 1. Rand0M $trinG Rand0M $trinG'
pattern1 = r'R.*M' # greedy
result1 = re.search(pattern1, search_string)

pattern2 = r'R.*?M' # lazy
result2 = re.search(pattern2, search_string)

print(result1, result2)
```

    <re.Match object; span=(6, 26), match='Rand0M $trinG Rand0M'> <re.Match object; span=(6, 12), match='Rand0M'>


<div class="alert alert-block alert-info">
    
#### Additional Characters for regex pattern:

| Character | description |
| --- | --- |
| `\d` | Matches any decimal digit; this is equivalent to `[0-9]` |
| `\s` | Matches characters considered whitespace in the ASCII character set; this is equivalent to `[ \t\n\r\f\v]` |
| `\w` | Matches characters considered alphanumeric in the ASCII character set; this is equivalent to `[a-zA-Z0-9_]` |
| `\D` | Matches any character which is not a decimal digit. This is the opposite of `\d`. This is equivalent to `[^0-9]` |
| `\S` | Matches any character which is not a whitespace character. This is the opposite of `\s`. This is equivalent to `[^ \t\n\r\f\v]` |
| `\W` | Matches any character which is not a word character. This is the opposite of `\w`. This is equivalent to `[^a-zA-Z0-9_]` |
    
</div>

### * Exercise 2:  TXT to CSV<a class="anchor" id="exercise-2"></a>

#File-operation #regex #file-read #file-write

<div class="alert alert-block alert-success">

In this exercise, we will read the data from the TXT file, extract the required information and the store in the CSV file.
   
<br>
    
The TXT file (*data.txt*) contains information about the books `id`, `author`, `title`, `genre`, `price`, `date`, and `description`. We want to extract the `id`, `title`, and `price` from it, and store the data into Comma-Separated Values formatted (CSV) file.

<br>    
To do this we need to perform the following steps:

- Read the data by opening the file    
- Extract the required data from the data using regex
- Formating the data into CSV
- Writing the data into CSV
    
**Write a Python Program to perform the extract from the file and store it into CSV file.**
    
    
<br>    
    
* Data file can be downloaded from here. [data.txt](https://drive.google.com/file/d/1PubQnzJR9lDm0RI38dLDmWAX167NnusQ/view?usp=sharing)
    
    
</div> 


```python
# Import re
import re
```


```python
# Read the data using open function from file 'data.txt'
```


```python
# Removing the '\n' & '\t' character
```




    '{"data": [{"id": 15246,"title": "Book data","description": "Contains infromation about the book\'s data"}],"data_0": [{"id": "bk101","author": "Gambardella, Matthew","title": "XML Developer\'s Guide","genre": "Computer","price": "44.95","publish_date": "2000-10-01","description": "An in-depth look at creating applications with XML."},{"id": "bk102","author": "Ralls, Kim","title": "Midnight Rain","genre": "Fantasy","price": "5.95","publish_date": "2000-12-16","description": "A former architect battles corporate zombies, an evil sorceress, and her own childhood to become queen of the world."},{"id": "bk103","author": "Corets, Eva","title": "Maeve Ascendant","genre": "Fantasy","price": "5.95","publish_date": "2000-11-17","description": "After the collapse of a nanotechnology society in England, the young survivors lay the foundation for a new society."},{"id": "bk104","author": "Corets, Eva","title": "Oberon\'s Legacy","genre": "Fantasy","price": "5.95","publish_date": "2001-03-10","description": "In post-apocalypse England, the mysterious agent known only as Oberon helps to create a new life for the inhabitants of London. Sequel to Maeve Ascendant."}],"data_1": [{"id": "bk201","author": "Jaku, Eddie","title": "The Happiest Man On Earth","genre": "Non-Fiction","price": "26.95","publish_date": "2020-07-28","description": " This is a powerful, heartbreaking and ultimately hopeful memoir of how happiness can be found even in the darkest of times."},{"id": "bk202","author": "Kishimi, Ichiro and Koga, Fumitake","title": "Courage to be Disliked","genre": "Non-Fiction","price": "19.99","publish_date": "2013-12-12","description": "The Japanese phenomenon that teaches us the simple yet profound lessons required to liberate our real selves and find lasting happiness."},{"id": "bk203","author": "Jordan, Robert","title": "The Eye of the World","genre": "Fantasy","price": "59.99","publish_date": "1990-01-15","description": "The Wheel of Time turns and Ages come and go, leaving memories that become legend. Legend fades to myth, and even myth is long forgotten when the Age that gave it birth returns again. In the Third Age, an Age of Prophecy, the World and Time themselves hang in the balance. What was, what will be, and what is, may yet fall under the Shadow."}]}'




```python
# creating the regex to get the data
```

<div class="alert alert-block alert-info">
    
#### Function: `eval()`
The `eval()` function evaluates the specified expression, if the expression is a legal Python statement, it will be executed.  
Syntax:  
eval(expression, globals, locals)

    
| | |
|--- | ---|
|<strong>expression</strong> | A String, that will be evaluated as Python code |
|<strong>globals</strong> | *Optional.* A dictionary containing global parameters |
|<strong>locals</strong> | *Optional.* A dictionary containing local parameters |

    
##### `eval()` is considered insecure because it allows you (or your users) to dynamically execute arbitrary Python code.

This is considered bad programming practice because the code that you’re reading (or writing) is not the code that you’ll execute. If you’re planning to use `eval()` to evaluate input from a user or any other external source, then you won’t know for sure what code is going to be executed. That’s a serious security risk if your application runs in the wrong hands.  
For this reason, good programming practices generally recommend against using `eval()`. But if you choose to use the function anyway, then the rule of thumb is to never ever use it with untrusted input    
    
</div>    


```python
# using loops and eval function to get into dict format
# and then finding the id, title, and price
```

    bk101 XML Developer's Guide 44.95
    bk102 Midnight Rain 5.95
    bk103 Maeve Ascendant 5.95
    bk104 Oberon's Legacy 5.95
    bk201 The Happiest Man On Earth 26.95
    bk202 Courage to be Disliked 19.99
    bk203 The Eye of the World 59.99



```python
# format the data for the CSV file, 
# think of pattern for CSV like "item 1","item 2"
```

    id,title,price
    "bk101","XML Developer's Guide","44.95"
    "bk102","Midnight Rain","5.95"
    "bk103","Maeve Ascendant","5.95"
    "bk104","Oberon's Legacy","5.95"
    "bk201","The Happiest Man On Earth","26.95"
    "bk202","Courage to be Disliked","19.99"
    "bk203","The Eye of the World","59.99"
    



```python
# Write the data to file name 'clean.csv'
```

### * Exercise 3:  Body-Mass Index (BMI) Calculation<a class="anchor" id="exercise-3"></a>

#Exception-Handling #try-except-finally #assert #raise

<div class="alert alert-block alert-success">

### What is BMI?
Body mass index, or BMI, is used to determine whether you are in a healthy weight range for your height.

It is useful to consider BMI alongside waist circumference, as waist measurement helps to assess risk by measuring the amount of fat carried around your middle.

BMI is a useful measurement for most people over 18 years old. But it is only an estimate and it doesn’t take into account age, ethnicity, gender and body composition.
    
We are not going to learn more than this as we just want to write a program that does this calculation. We will do the same task using two different variations.
    
1. Using `assert` and `raise` statements
2. Using `try`, `except`, and `finally`.   
    
</div>

<div class="alert alert-block alert-success">
    
#### Part 1: Using `assert` statement

write a Python function named `calc_bmi():` that asks user to input his/her weight(kg) and height(m) one by one and prints out the BMI of the user. The Body Mass Index(BMI) can be calculated by the following formula:

<small>$BMI = \frac{weight}{height^{2}}$</small>  
    
- The user input is expected to be a number. If not, then throws assertion error: "Entered value should be a float value"  
- If the height is 0, the function raises ZeroDivisionError: "Height cannot be zero."
</div>


```python
def calc_bmi():
    """
    Calculates BMI from user input of weight and height
    """
    pass

calc_bmi()
```

    Please enter weight in kg: 5
    Please enter height in m: 5





    0.2



<div class="alert alert-block alert-success">
  
#### Part 2: Using `try`, `except`, and `finally`
    
write a Python function named `calc_bmi():` that asks user to input his/her weight(kg) and height(m) one by one and prints out the BMI of the user. The Body Mass Index(BMI) can be calculated by the following formula:

<small>$BMI = \frac{weight}{height^{2}}$</small>

- The user input is expected to be a float number. 
- If the user input is not a float number, the function will print "Invalid input."
- If the height is 0, the function will print "Height cannot be zero."
- No matter the user inputs are valid or not, the function will print out "End." at last.    
    
</div>


```python
def calc_bmi():
    """
    Calculates BMI from user input of weight and height
    """
    pass
        
calc_bmi()
```

    Please enter weight in kg: 5
    Please enter height in m: 2
    Your bmi is 1.25
    End.



```python

```
