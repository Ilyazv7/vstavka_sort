def insertion_binary(data):
    c = 0
    count = []
    for i in range(len(data)):
        key = data[i]
        lo, hi = 0, i - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if key < data[mid]:
                hi = mid
            else:
                lo = mid + 1
        for j in range(i, lo + 1, -1):
            data[j] = data[j - 1]
            c += 1
        count = c
        data[lo] = key
    return data, c

