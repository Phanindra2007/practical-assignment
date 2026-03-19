import random
import sys
sys.setrecursionlimit(10**7)

def quick_sort(arr, pivot_type="first"):
    a = arr.copy()
    _quick_sort(a, 0, len(a) - 1, pivot_type)
    return a

def _quick_sort(a, low, high, pivot_type):
    if low < high:
        pi = partition(a, low, high, pivot_type)
        _quick_sort(a, low, pi - 1, pivot_type)
        _quick_sort(a, pi + 1, high, pivot_type)

def choose_pivot(a, low, high, pivot_type):
    if pivot_type == "random":
        return random.randint(low, high)
    elif pivot_type == "median":
        mid = (low + high) // 2
        trio = [(a[low], low), (a[mid], mid), (a[high], high)]
        trio.sort()
        return trio[1][1]
    return low  # default first

def partition(a, low, high, pivot_type):
    pivot_idx = choose_pivot(a, low, high, pivot_type)
    a[pivot_idx], a[high] = a[high], a[pivot_idx]

    pivot = a[high]
    i = low - 1

    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]

    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1