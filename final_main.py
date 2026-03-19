import os
import time
import csv

from sorting_algorithms.selection_sort import selection_sort
from sorting_algorithms.bubble_sort import bubble_sort
from sorting_algorithms.insertion_sort import insertion_sort
from sorting_algorithms.merge_sort import merge_sort
from sorting_algorithms.quick_sort import quick_sort
from sorting_algorithms.heap_sort import heap_sort
from sorting_algorithms.radix_sort import radix_sort

TESTCASE_DIR = "testcases"
RUNS = 5

# 🔥 CHANGE THIS EACH RUN
ALGO_NAME = "selection"


# -------- ALGO MAPPING --------
def get_algorithm(name):
    return {
        "selection": selection_sort,
        "bubble": bubble_sort,
        "insertion": insertion_sort,
        "merge": merge_sort,
        "heap": heap_sort,
        "radix": radix_sort,
        "quick_best": lambda arr: quick_sort(arr, "median"),
    }[name]


# -------- PRETTY NAME --------
def format_algorithm_name(name):
    return {
        "selection": "Selection Sort",
        "bubble": "Bubble Sort",
        "insertion": "Insertion Sort",
        "merge": "Merge Sort",
        "heap": "Heap Sort",
        "radix": "Radix Sort",
        "quick_best": "Quick Sort (Median of Three)",
    }[name]


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
    start = time.perf_counter()
    func(arr)
    end = time.perf_counter()
    return (end - start)


# -------- MAIN --------
def main():
    algo_func = get_algorithm(ALGO_NAME)
    algo_pretty = format_algorithm_name(ALGO_NAME)

    results = []

    for file in sorted(os.listdir(TESTCASE_DIR)):
        arr = read_testcase(os.path.join(TESTCASE_DIR, file))
        input_type, n = extract_details(file)

        # skip slow algos
        if n > 20000 and ALGO_NAME in ["bubble", "insertion", "selection"]:
            results.append([algo_pretty, input_type, n, "SKIPPED"])
            continue

        times = [measure_time(algo_func, arr) for _ in range(RUNS)]
        avg = sum(times) / RUNS

        avg = f"{avg:.6f}"  # seconds formatted

        results.append([algo_pretty, input_type, n, avg])

    # -------- WRITE CSV --------
    file_exists = os.path.exists("final_results.csv")
    file_empty = (not file_exists) or os.path.getsize("final_results.csv") == 0

    with open("final_results.csv", "a", newline="") as f:
        writer = csv.writer(f)

        if file_empty:
            writer.writerow(["Algorithm", "Input Type", "Input Size (N)", "Average Time (s)"])

        writer.writerows(results)

    print(f"{algo_pretty} done and saved.")


if __name__ == "__main__":
    main()