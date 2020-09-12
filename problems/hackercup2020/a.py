from sys import stdin
from collections import deque

t = int(stdin.readline())

for i in range(t):
    n = int(stdin.readline())
    incoming = stdin.readline()
    outgoing = stdin.readline()
    print(f"Case #{i+1}:")
    # dictionaries in python >= 3.6 are ordered by insertion
    countrymap = {}
    for j in range(n):
        countrymap[j] = []
        if outgoing[j] == 'Y':
            if j > 0 and incoming[j-1] == 'Y':
                countrymap[j].append(j-1)
            if j < n - 1 and incoming[j+1] == 'Y':
                countrymap[j].append(j+1)
    for index in range(n):
        reachable = set()
        d = deque()
        d.append(index)
        while len(d) > 0:
            reached = d.pop()
            if reached not in reachable:
                reachable.add(reached)
                for x in countrymap[reached]:
                    d.append(x)
        ans = ""
        for x in range(n):
            if x in reachable:
                ans += 'Y'
            else:
                ans += 'N'
        print(ans)
