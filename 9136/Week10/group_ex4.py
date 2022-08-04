temp1 = [5, 2]

temp2 = [3, 5]

temp3 = [[temp1], [temp2]]

for i in temp3:
    for j in i:
        print(j[0]*j[1])
