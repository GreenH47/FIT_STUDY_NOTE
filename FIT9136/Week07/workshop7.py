# open file for reading
file = open('example.txt', 'r')

# read one line at a time
# This is a dog
# print(file.readline())

# iterate through each of the lines and print it
# This is a dog
# The weather is good
# Food is delicious
# for line in file:
#     print(line)

# read the entire content as a list
# ['This is a dog\n', 'The weather is good\n', 'Food is delicious']
# print(file.readlines())

# Lets remove the \n at the end of line
# ['This is a dog', 'The weather is good', 'Food is delicious']
# read the entire content as a list
content = file.readlines()

# create an empty list
result = []

# Iterated through each item of the list
for line in content:
    line = line.strip('\n')  # remove the newline character
    # add the edited line to the new list
    result.append(line)

# display the new list
print(result)

# close the file
file.close()


#open the file for writing
write_file = open("demo.txt", "w")

#iterate through each item in the list
for i in result:
    #write the item into the file
    write_file.write(i + '\n')

# close the file
write_file.close()

#open file for reading
file = open('example.txt', 'r')

#read the entire content as a string
print(file.read())