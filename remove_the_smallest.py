def can_reduce_to_one(a):
    a.sort()
    i, j = 0, 1
    while j < len(a):
        if a[j] - a[i] > 1:
            return "NO"
        i += 1
        j += 1
    return "YES"



