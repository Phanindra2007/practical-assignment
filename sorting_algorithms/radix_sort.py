def radix_sort(arr):
    a = arr.copy()
    max_num = max(a)
    exp = 1

    while max_num // exp > 0:
        counting_sort(a, exp)
        exp *= 10

    return a

def counting_sort(a, exp):
    n = len(a)
    output = [0] * n
    count = [0] * 10

    for num in a:
        index = (num // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (a[i] // exp) % 10
        output[count[index] - 1] = a[i]
        count[index] -= 1

    for i in range(n):
        a[i] = output[i]