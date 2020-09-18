from typing import List
from copy import deepcopy
from math import floor
from collections import deque

def clockwise_grid_sort(grid: List[List[int]]) -> List[List[int]]:
    m = deepcopy(grid)
    glen = len(m)
    itlen = floor((glen-1)/2)
    for i in range(itlen + 1):
        tosort = []
        for j in range(i, glen - i):
            tosort.append(m[i][j])
        for j in range(i + 1, glen - i):
            tosort.append(m[j][glen-1-i])
        for j in reversed(range(i, glen - i - 1)):
            tosort.append(m[glen-1-i][j])
        for j in reversed(range(i + 1, glen - i - 1)):
            tosort.append(m[j][i])
        tosort.sort()
        tosort = deque(tosort)
        for j in range(i, glen - i):
            m[i][j] = tosort.popleft()
        for j in range(i + 1, glen - i):
            m[j][glen-1-i] = tosort.popleft()
        for j in reversed(range(i, glen - i - 1)):
            m[glen-1-i][j] = tosort.popleft()
        for j in reversed(range(i + 1, glen - i - 1)):
            m[j][i] = tosort.popleft()
    return m