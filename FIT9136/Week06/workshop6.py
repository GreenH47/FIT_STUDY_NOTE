from stack import Stack

int_stack = Stack()
int_stack.push(1)
int_stack.push(2)
print(int_stack.pop(), end= ",")
int_stack.push(3)
print(int_stack.pop(), end=",")
print(int_stack.pop())