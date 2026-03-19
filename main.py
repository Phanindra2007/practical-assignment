import os
import time
import csv

from sorting_algorithms.quick_sort import quick_sort

TESTCASE_DIR = "testcases"
RUNS = 5


# -------- INPUT TYPE + N --------
def extract_details(filename):
    name = filename.lower()

    if name.startswith("1_"):
        input_type = "Random"
    elif name.startswith("2_"):
        input_type = "Sorted"
    elif name.startswith("3_"):
        input_type = "Reverse"
    else:
        input_type = "Unknown"

    n = int(name.split("_")[1])
    return input_type, n


# -------- READ FILE --------
def read_testcase(file_path):
    with open(file_path, "r") as f:
        tokens = f.read().split()
        nums = [int(x) for x in tokens if x.lstrip('-').isdigit()]
        return nums[1:]


# -------- TIME --------
def measure_time(func, arr):
    try:
        start = time.perf_counter()
        func(arr)
        end = time.perf_counter()
        return (end - start)
    except RecursionError:
        return None


# -------- QUICK VARIANTS --------
quick_algorithms = {
    "Quick Sort (First Pivot)": lambda arr: quick_sort(arr, "first"),
    "Quick Sort (Random Pivot)": lambda arr: quick_sort(arr, "random"),
    "Quick Sort (Median of Three)": lambda arr: quick_sort(arr, "median"),
}


# -------- MAIN --------
def main():
    results = []

    for file in sorted(os.listdir(TESTCASE_DIR)):
        arr = read_testcase(os.path.join(TESTCASE_DIR, file))
        input_type, n = extract_details(file)

        for name, func in quick_algorithms.items():
            times = []

            for _ in range(RUNS):
                t = measure_time(func, arr)
                if t is not None:
                    times.append(t)

            if len(times) == 0:
                avg = "ERROR"
            else:
                avg = f"{(sum(times)/len(times)):.6f}"

            results.append([name, input_type, n, avg])

    # -------- WRITE CSV --------
    with open("quick_results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Algorithm", "Input Type", "Input Size (N)", "Average Time (s)"])
        writer.writerows(results)

    print("QuickSort results saved.")


if __name__ == "__main__":
    main()