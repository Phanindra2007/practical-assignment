import os
import time
import csv
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from sorting_algorithms.selection_sort import selection_sort
from sorting_algorithms.bubble_sort import bubble_sort
from sorting_algorithms.insertion_sort import insertion_sort
from sorting_algorithms.merge_sort import merge_sort
from sorting_algorithms.quick_sort import quick_sort
from sorting_algorithms.heap_sort import heap_sort
from sorting_algorithms.radix_sort import radix_sort

TESTCASE_DIR = os.path.join(BASE_DIR, "../testcases")
RUNS = 5
ALGO_NAME = "selection"  # Change this for each run.

def get_algorithm(name):
    return {
        "selection": selection_sort,
        "bubble": bubble_sort,
        "insertion": insertion_sort,
        "merge": merge_sort,
        "heap": heap_sort,
        "radix": radix_sort,
        "quick_first":  lambda arr: quick_sort(arr, "first"),
        "quick_random": lambda arr: quick_sort(arr, "random"),
        "quick_best":   lambda arr: quick_sort(arr, "median"),
    }[name]

def format_algorithm_name(name):
    return {
        "selection": "Selection Sort",
        "bubble": "Bubble Sort",
        "insertion": "Insertion Sort",
        "merge": "Merge Sort",
        "heap": "Heap Sort",
        "radix": "Radix Sort",
        "quick_first":  "Quick Sort (First Pivot)",
        "quick_random": "Quick Sort (Random Pivot)",
        "quick_best":   "Quick Sort (Median of Three)",
    }[name]

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

def measure(func, arr):
    times = []
    comps = []
    for _ in range(RUNS):
        result, c = func(arr)
        comps.append(c)
    for _ in range(RUNS):
        start = time.perf_counter()
        func(arr)
        end = time.perf_counter()
        times.append(end - start)
    avg_time = sum(times) / RUNS
    avg_comp = sum(comps) / RUNS
    return avg_time, avg_comp

def main():
    algo_func = get_algorithm(ALGO_NAME)
    algo_pretty = format_algorithm_name(ALGO_NAME)
    results = []

    for file in sorted(os.listdir(TESTCASE_DIR)):
        arr = read_testcase(os.path.join(TESTCASE_DIR, file))
        input_type, n = extract_details(file)
        avg_time, avg_comp = measure(algo_func, arr)
        results.append([algo_pretty, input_type, n, f"{avg_time:.6f}", int(avg_comp)])
        print(f"{file} | {input_type} | n={n} | time={avg_time:.6f}s | comparisons={int(avg_comp)}")

    csv_path = os.path.join(BASE_DIR, "../csv_data/final_results.csv")
    file_exists = os.path.exists(csv_path)
    file_empty = (not file_exists) or os.path.getsize(csv_path) == 0
    with open(csv_path, "a", newline="") as f:
        writer = csv.writer(f)
        if file_empty:
            writer.writerow(["Algorithm", "Input Type", "Input Size (N)", "Average Time (s)", "Comparisons"])
        writer.writerows(results)

    print(f"\n{algo_pretty} completed and saved.")

if __name__ == "__main__":
    main()