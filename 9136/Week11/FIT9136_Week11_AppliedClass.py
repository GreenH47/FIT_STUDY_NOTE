#!/usr/bin/env python
# coding: utf-8

# # FIT9136 - Week 11 Applied Session

# ## Table of Contents:
# 
# 1. [*Exercise 1: Recursion](#exercise-1)
# 2. [*Exercise 2: Fibonacci Series](#exercise-2)
# 3. [*Exercise 3: Sum of Numbers](#exercise-3)
# 4. [*Exercise 4: Recursive Linear Search](#exercise-4)

# ### *Exercise 1:  Recursion<a class="anchor" id="exercise-1"></a>

# <div class="alert alert-block alert-success">
# 
# * **Divide-and-Conquer**:
#     * Solving a complex problem by breaking it into **smaller manageable sub-problems** 
#     * Sub-problems can then be solved in a similar way (with the same solution)
#     * **Sub-solutions are then combined to produce the final solution for the original problem**
#     
# * **Recursion**:
#     * A <font color="blue">divide-and-conquer</font> approach for solving computational problems
#     * Each problem is “recursively” <font color="blue">decomposed into sub-problems</font> (which have the same properties the original problem but smaller in size)
#     * When the sub-problems have reached the <font color="blue">simplest form</font>, i.e. a <font color="blue">known solution</font> can be defined
#     * The <font color="blue">known solutions of these sub-problems are then recomposed</font> together to produce the solution of the original problem
#    
# <br>    
# <br> 
#     
# **<font color="red">Task:</font> List all benefits(advantages) and detriments(Distadvantages) for using recursion.**
#     
# </div>

# **<font color="red">Answer:</font>**
# 
# * **Benefits (Advantages)**:
#     * 
#     * 
# 
# * **Detriments (Disadvantages)**:
# 	* 
#     *

# <div class="alert alert-block alert-success">
#     
# Now, Let us look at the codes that help us to understand the **recursion** and **Laws** that helps to write the recursive functions.
#     
# The `three Laws` are as follow:
# 1. **Base Case**:  is usually the smallest input and has an easily verifiable solution. This is also the mechanism that stops the function from calling itself forever. 
# 2. **Recursive Case**:  is the set of all cases where a recursive call, or a function call to itself, is made.
# 3. **Convergence Case**: its state and move toward the base case.    
# 
# <br>    
# <br> 
#     
# **<font color="red">Task:</font> Find all the `3 cases` for the following code, and answer what the code does:**    
#     
# * **A:**
# ```
# def foo (b):
#     return aux_foo(b,0)
# def aux_foo(b,a):
#     if b == a:
#         return 1
#     else:
#         return 1 + aux_foo(b-1,a)    
# ```
# 
# * **B:**
# ```
# def fun(a, b): 
#     if (b == 0): 
#         return 1 
#     if (b % 2 == 0): 
#         return fun(a*a, b//2)    
#     return fun(a*a, b//2)*a      
# ```    
# </div>    

# **<font color="red">Answer:</font>**
# 
# **A:**
# * 
# * 
# 
# **B:**
# * 
# * 

# ### *Exercise 2:  Fibonacci Series<a class="anchor" id="exercise-2"></a>

# <div class="alert alert-block alert-success">
# 
# Fibonacci numbers are a classic example of recursive definitions. Fibonacci numbers are generated by adding the two previous numbers together. The sequence of numbers starts with [1,1].
# 
# * [Fibonacci example](https://www.mathsisfun.com/numbers/fibonacci-sequence.html#:~:text=The%20Fibonacci%20Sequence%20is%20the,the%20two%20numbers%20before%20it%3A&text=and%20so%20on)    
# 
#     
# <br>
# <br>
# 
# * **<font color="blue">Part-1:</font>** Write a function that calculates the Nth Fibonacci number **iteratively**.
# * **<font color="blue">Part-2:</font>** Write a function that calculates the Nth Fibonacci number **recursively**.
#     
# </div> 

# In[1]:


# Part-1
# write your answer here for iterative implemenation
def iter_fib(N):
    pass

if __name__ == "__main__":
    for i in range(10):
        print(iter_fib(i),end = ", ")


# In[2]:


# Part-2
# write your answer here for Recursive implementation
def rec_fib(N):
    pass

if __name__ == "__main__":
    for i in range(11):
        print(rec_fib(i),end=", ")


# ### *Exercise 3:  Sum of Numbers<a class="anchor" id="exercise-3"></a>

# <div class="alert alert-block alert-success">
# 
# Given a number, return the total sum of that number multiplied by every number between 1 and 10. Do not use the sum() built-in function.
# 
# Example:
# 
# * total_sum(1) ➞ 55
# 
# 1 x 1 + 1 x 2 + 1 x 3 ...... 1 x 9 + 1 x 10 = 55
# 
# * total_sum(6) ➞ 330
# 
# 6 x 1 + 6 x 2 + 6 x 3 ...... 6 x 9 + 6 x 10 = 330
#     
# <br>
# <br>
#     
# **Write a python code to find sum of number using recursion.**    
# 
# </div>

# In[6]:


#write your answer here
def total_sum(n, ten = 10):
    pass


# In[7]:


total_sum(1)


# In[8]:


total_sum(6)


# ### *Exercise 4:  Recursive Linear Search<a class="anchor" id="exercise-4"></a>

# <div class="alert alert-block alert-success">
# 
# **Write a python code to implement a Linear Search that is recursive. Would the Big O complexity of Linear Search be changed if it were coded recursively?**    
#   
# </div>

# In[9]:


## implementation
def rec_lin_search(li,item):
    return aux_rec_lin_search(0,li,item)

def aux_rec_lin_search(i,li,item):
    pass

li = [1,2,3,4,5,6,7,8,9,0]

print(rec_lin_search(li,1))


# **Answer:**

# In[ ]:




