def merge_sort(arr):
    comparisons = [0]

    def _merge(a):
        if len(a) <= 1:
            return a
        mid = len(a) // 2
        left = _merge(a[:mid])
        right = _merge(a[mid:])
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            comparisons[0] += 1
            if left[i] <= right[j]:
                result.append(left[i]); i += 1
            else:
                result.append(right[j]); j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    sorted_arr = _merge(arr.copy())
    return sorted_arr, comparisons[0]