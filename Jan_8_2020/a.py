import sys

line1 = sys.stdin.readline()
line2 = sys.stdin.readline()
n = int(line1)
arr = list(map(lambda x: int(x), line2.split()))

m = 0
t = 0
for x in range(len(arr)):
    temp = arr[x]
    if temp > t:
        t = temp
    if t == x + 1:
        m += 1

print(m)
