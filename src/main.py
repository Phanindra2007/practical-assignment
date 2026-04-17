import os
import time
import csv
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from sorting_algorithms.quick_sort import quick_sort

TESTCASE_DIR = os.path.join(BASE_DIR, "../testcases")
RUNS = 5

def extract_details(filename):
    name = filename.lower().replace(".txt", "")
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

def read_testcase(file_path):
    with open(file_path, "r") as f:
        tokens = f.read().split()
        nums = [int(x) for x in tokens if x.lstrip('-').isdigit()]
        return nums[1:]

quick_algorithms = {
    "Quick Sort (First Pivot)":     lambda arr: quick_sort(arr, "first"),
    "Quick Sort (Random Pivot)":    lambda arr: quick_sort(arr, "random"),
    "Quick Sort (Median of Three)": lambda arr: quick_sort(arr, "median"),
}

def main():
    results = []

    for file in sorted(os.listdir(TESTCASE_DIR)):
        arr = read_testcase(os.path.join(TESTCASE_DIR, file))
        input_type, n = extract_details(file)

        for name, func in quick_algorithms.items():
            times = []
            comps = []

            for _ in range(RUNS):
                try:
                    _, c = func(arr)
                    comps.append(c)
                except:
                    pass

            for _ in range(RUNS):
                try:
                    start = time.perf_counter()
                    func(arr)
                    end = time.perf_counter()
                    times.append(end - start)
                except:
                    pass

            avg_time = f"{sum(times)/len(times):.6f}" if times else "ERROR"
            avg_comp = int(sum(comps)/len(comps)) if comps else 0

            results.append([name, input_type, n, avg_time, avg_comp])
            print(f"{file} | {name} | {input_type} | n={n} | time={avg_time}s | comparisons={avg_comp}")

    with open(os.path.join(BASE_DIR, "../csv_data/quick_results.csv"), "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Algorithm", "Input Type", "Input Size (N)", "Average Time (s)", "Comparisons"])
        writer.writerows(results)

    print("Quick Sort results saved.")

if __name__ == "__main__":
    main()