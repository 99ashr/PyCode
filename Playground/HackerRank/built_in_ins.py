#!/usr/bin/env python3


n = int(input().strip())
arr = map(int, input().strip().split(' '))
print(sum(arr))

# ---------------------------------------------------------------------------- #

N = input()
M = map(int, input().split())
if all(k > 0 for k in M):
    if any(str(i)[::-1] == str(i) for i in M):
        print(True)
    else:
        print(False)
else:
    print(False)
