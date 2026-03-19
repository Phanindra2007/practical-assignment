import random

def quick_sort(arr, mode="first"):
    a = arr.copy()
    comparisons = [0]

    def partition(a, low, high):
        pivot = a[low]
        i = low + 1
        for j in range(low + 1, high + 1):
            comparisons[0] += 1
            if a[j] < pivot:
                a[i], a[j] = a[j], a[i]
                i += 1
        a[low], a[i-1] = a[i-1], a[low]
        return i - 1

    def _qs(a, low, high):
        if low < high:
            if mode == "random":
                r = random.randint(low, high)
                a[low], a[r] = a[r], a[low]
            elif mode == "median":
                mid = (low + high) // 2
                c = [(a[low], low), (a[mid], mid), (a[high], high)]
                c.sort()
                a[low], a[c[1][1]] = a[c[1][1]], a[low]
            pi = partition(a, low, high)
            _qs(a, low, pi-1)
            _qs(a, pi+1, high)

    import sys
    sys.setrecursionlimit(max(10000, len(a)*2))
    _qs(a, 0, len(a)-1)
    return a, comparisons[0]