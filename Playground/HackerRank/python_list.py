#!/usr/bin/env python3

#! -------------------------- All the methods of list ------------------------- #
# ---------------------------------------------------------------------------- #
inp = [['insert', '0', '5'],
       ['insert', '1', '10'],
       ['insert', '0', '6'],
       ['print'],
       ['remove', '6'],
       ['append', '9'],
       ['append', '1'],
       ['sort'],
       ['print'],
       ['pop'],
       ['reverse'],
       ['print']]  # Test Input
# ---------------------------------------------------------------------------- #
l = []
for i in inp:
    k = []
    k = i
    # print(k)
    if k[0] == 'insert':
        l.insert(int(k[1]), int(k[2]))
    elif k[0] == 'print':
        print(l)
    elif k[0] == 'remove':
        l.remove(int(k[1]))
    elif k[0] == 'append':
        l.append(int(k[1]))
    elif k[0] == 'sort':
        l.sort()
    elif k[0] == 'pop':
        l.pop()
    elif k[0] == 'reverse':
        l.reverse()
    else:
        print("Invalid Command")
#! ------------------------------------ EOF ----------------------------------- #
