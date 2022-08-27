dict1 = {'A': 20, 'B': 15, 'C': 20, 'D': 10, 'E': 20}

temp = []
res = dict()
for key, val in dict1.items():
    if val not in temp:
        temp.append(val)
        res[key] = val

print(res)
