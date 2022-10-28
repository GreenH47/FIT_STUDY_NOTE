# https://pythontutor.com/
# https://www.hackerearth.com/practice/algorithms/sorting/insertion-sort/visualize/

# abc = 1 + 2 ** 3 ** 2 % 5
# print(abc)
#
# print(1.1 + 2.2 == 3.3)

alist = [4,2,8,6,5]
# blist = alist
# blist[3] = 999

# blist = alist * 2
# blist[3] = 999
# print(alist)

# a = [ ]
# b = dict()
# b[a]

numbers = [4, 5, 6]
j = 0
total = 0

while j < 3:
    k = j
    while k < 3:
        total = total + numbers[k]
        k += 1
    j += 1

print(total)

