file_handle = open('output_file.txt', 'w')

file_content = ""

line_1 = "first line"
line_2 = "second line"
line_3 = "third line"

file_content += line_1 + '\n' + line_2 + '\n' + line_3 + '\n'

file_handle.write(file_content)

file_handle.close()


#debugging using assert statement
def myadd(x, y):
    assert (x<y), 'x has to be smaller than y'
    return x+y
    print('program done')

myadd(2,3)