# Stack Implementation
# create a class stack
class Stack:
    # create a constructor to initialize the stack & count variable
    def __init__(self):
        self.the_stack = []
        self.count = 0

    # overload len method to get the siz/count of the stack
    def __len__(self):
        return self.count

    # is_empty method checks if stack is empty or not
    def is_empty(self):
        return self.count == 0

    # push method push the item into stack
    def push(self, item):
        self.the_stack.append(item)
        self.count += 1

    # pop method pops out the item from top of the stack
    def pop(self):
        assert not self.is_empty()
        self.count -= 1
        return self.the_stack.pop()

    # peek method helps us to look inside the values of stack
    def peek(self):
        assert not self.is_empty()
        return self.the_stack[-1]

# your code here
# Create set of operators
OPERATORS = set(['+', '-', '*', '/', '^'])
# Create a dictionary having priorities
PRIORITY = {'+':1, '-':1, '*':2, '/':2, '^':3}
def infix_to_postfix(expression):
    pass


# User inputs the expression:
expression = input('Enter infix expression')
print('infix expression: ',expression)
print('postfix expression: ',infix_to_postfix(expression))