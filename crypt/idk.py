import itertools
import math
code = 'rbebbbgyuprubrayugbmes'


tracker = []
for i in range(len(code)):
    tracker.append(i)


for l in range(2,math.ceil(len(code)/2)+1):
    temp = tracker.copy()
    curr = 0
    decrypt = ""
    while len(temp) != 0:
        decrypt = decrypt + code[curr]
        temp.remove(curr)
        curr += l
        if curr >= len(code):
            try:
                curr = temp[0]
            except:
                break
    print(decrypt)
    print(l)
    print()


        


