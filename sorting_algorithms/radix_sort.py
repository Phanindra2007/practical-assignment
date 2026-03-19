def radix_sort(arr):
    a = arr.copy()
    if not a:
        return a, 0
    comparisons = 0
    max_val = max(a)
    exp = 1
    while max_val // exp > 0:
        output = [0] * len(a)
        count = [0] * 10
        for num in a:
            count[(num // exp) % 10] += 1
        for i in range(1, 10):
            count[i] += count[i-1]
        for i in range(len(a)-1, -1, -1):
            idx = (a[i] // exp) % 10
            output[count[idx]-1] = a[i]
            count[idx] -= 1
        for i in range(len(a)):
            a[i] = output[i]
        exp *= 10
        comparisons += len(a)  # each pass does n comparisons
    return a, comparisons