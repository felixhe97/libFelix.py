

MOD = int(1e9 + 7)

def numarrangement(sc: int, lc: int, n: int) -> int:
    if sc < 2 or lc < 2 or n < 1:
        return -1
    return 0

def seating(d: int, t: int, q: list) -> None:
    if d < 2 or t < 2:
        print(f"constraints {d} and {t} must be >= 2")
        return
    if not q:
        print("seating queries must be non empty")
        return
    sc = 0
    lc = 0
    if d < t:
        sc = d
        lc = t
    else:
        sc = t
        lc = d
    for n in q:
        print(numarrangement(sc, lc, n))

if __name__ == "__main__":
    # must be fewer than d seated consecutively, so d must be >= 2
    d = 3
    # must be fewer than t seated consecutively, so t must be >= 2
    t = 2
    # for each seating size in q array, return how many different full seating
    # arrangements that satisfy above two constraints
    q = [1, 2, 3, 4, 5, 6]
    #    2  3  4  5  7  9
    seating(d, t, q)
    seating(1,1,[3])
