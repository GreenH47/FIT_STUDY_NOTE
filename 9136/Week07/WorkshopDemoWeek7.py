#!/usr/bin/env python
# coding: utf-8

# ### File operations

# In[ ]:


#open file for reading
file = open('example.txt', 'r')

#read one line at a time
print(file.readline())

#close the file
file.close()


# In[ ]:


#open file for reading
file = open('example.txt', 'r')

#iterate through each of the lines and print it
for line in file:
    print(line)
    
#close the file
file.close()


# In[ ]:


#open file for reading
file = open('example.txt', 'r')

#read the entire content as a list
print(file.readlines())

#close the file
file.close()


# In[ ]:


#Lets remove the \n at the end of line

#Way 1: using readlines()
#open file for reading
file = open('example.txt', 'r')

#read the entire content as a list
content = file.readlines()

#create an empty list
result = []

#Iterated through each item of the list
for line in content:
    line = line.strip('\n')   # remove the newline character
    #add the edited line to the new list
    result.append(line)
    
#display the new list    
print(result)

#close the file
file.close()


# In[ ]:


#Way 2: using loop for iterating through each line

#create an empty list
result = []

#open file for reading
with open('example.txt', 'r') as infile:
    
    #Iterated through each item of the list
    for line in infile:
        line = line.strip('\n') # remove the newline character
        #add the edited line to the new list
        result.append(line)
    
#display the new list    
print(result)


# In[ ]:


#open the file for writing
write_file = open("demo.txt", "w")

#iterate through each item in the list
for i in result:
    #write the item into the file 
    write_file.write(i + '\n')

# close the file   
write_file.close()


# In[ ]:


#open file for reading
file = open('example.txt', 'r')

#read the entire content as a string
print(file.read()) 


# ### Debugging

# In[10]:


#debugging using if-else statement
def myadd(x, y):
    if x<y: 
        return x+y
    else:
        print('x has to be smaller than y')
    print('program done')


# In[11]:


myadd(3,2)  # this is a form of error handling


# In[12]:


#debugging using assert statement
def myadd(x, y):
    assert x<y, 'x has to be smaller than y'
    return x+y
    print('program done')


# In[13]:


myadd(3,2)   # error handling using assert statement


# In[8]:


import unittest

def product_function(first_arg, second_arg):
    result = first_arg * second_arg
    return result

class TestForFunction(unittest.TestCase):
    def test_product_function(self):
        self.assertEqual(product_function(2,3), 6)   # check equality

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)  # call unittest.main() to start testing


# In[12]:


import unittest


class TestForFunction(unittest.TestCase):
    def test_issameobject(self):
        a = [1,2,3,4]
        b = a
        c= [1,2,3,4]
        self.assertIs(a, c)    

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


# In[14]:


import unittest

def product_function(first_arg, second_arg):
    result = first_arg * second_arg
    return result

class TestForFunction(unittest.TestCase):
    def test_isdigit(self):
        self.assertTrue("shirin".isalpha()) 

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)  # call unittest.main()


# ### Error Handling

# In[7]:


file_name = 'another_input_file.txt'
try: 
    file_handle = open(file_name, 'r')
    
except IOError:
    print('Cannot open', file_name)
    
except RuntimeError:
    print('A run-time error has occurred')
    
else:
    print(file_name, 'has', len(file_handle.readlines()), 'lines')
    file_handle.close()
    
finally:
    print('Exiting file reading')


# In[ ]:




