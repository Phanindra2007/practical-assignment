def heap_sort(arr):
    a = arr.copy()
    n = len(a)
    comparisons = [0]

    def heapify(a, n, i):
        largest = i
        l, r = 2*i+1, 2*i+2
        if l < n:
            comparisons[0] += 1
            if a[l] > a[largest]:
                largest = l
        if r < n:
            comparisons[0] += 1
            if a[r] > a[largest]:
                largest = r
        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            heapify(a, n, largest)

    for i in range(n//2 - 1, -1, -1):
        heapify(a, n, i)
    for i in range(n-1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapify(a, i, 0)
    return a, comparisons[0]