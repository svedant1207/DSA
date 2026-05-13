def lls(arr):
    res = set()
    i, j = 0, 0

    n = len(arr)
    long = 0

    while j < n:
        if s[j] not in res:
            res.add(s[j])
            j += 1
            long = max(long, j-1)

        else:
            res.remove(s[i])
            i += 1


arr = [12, -1, -7, 8, -15, 30, 16, 28]
print(lls(arr, 3))