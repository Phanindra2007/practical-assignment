import os
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(BASE_DIR, "quick_results.csv"))

colors = {
    "Quick Sort (First Pivot)":     "red",
    "Quick Sort (Random Pivot)":    "blue",
    "Quick Sort (Median of Three)": "green",
}

cases = ["Random", "Sorted", "Reverse"]
case_titles = {
    "Random":  "Average Case - Random Input",
    "Sorted":  "Best Case - Sorted Input",
    "Reverse": "Worst Case - Reverse Sorted Input",
}

algos = list(colors.keys())

GRAPHS_DIR = os.path.join(BASE_DIR, "graphs/Quick_graphs")
os.makedirs(GRAPHS_DIR, exist_ok=True)

# Graphs 1-3: Time vs n
for case in cases:
    plt.figure(figsize=(12, 7))
    subset = df[df["Input Type"] == case]
    for algo in algos:
        data = subset[subset["Algorithm"] == algo].sort_values("Input Size (N)")
        if data.empty: continue
        plt.plot(data["Input Size (N)"], data["Average Time (s)"].astype(float),
                 marker='o', label=algo, color=colors[algo], linewidth=2)
    plt.title(f"QuickSort - Time vs n - {case_titles[case]}", fontsize=14)
    plt.xlabel("Input Size (n)", fontsize=12)
    plt.ylabel("Average Time (seconds)", fontsize=12)
    plt.legend(fontsize=10)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(GRAPHS_DIR, f"quicksort_time_{case.lower()}.png"), dpi=150)
    plt.close()
    print(f"Saved quicksort_time_{case.lower()}.png")

# Graphs 4-6: Comparisons vs n
for case in cases:
    plt.figure(figsize=(12, 7))
    subset = df[df["Input Type"] == case]
    for algo in algos:
        data = subset[subset["Algorithm"] == algo].sort_values("Input Size (N)")
        if data.empty: continue
        plt.plot(data["Input Size (N)"], data["Comparisons"],
                 marker='o', label=algo, color=colors[algo], linewidth=2)
    plt.title(f"QuickSort - Comparisons vs n - {case_titles[case]}", fontsize=14)
    plt.xlabel("Input Size (n)", fontsize=12)
    plt.ylabel("Number of Comparisons", fontsize=12)
    plt.legend(fontsize=10)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(GRAPHS_DIR, f"quicksort_comparisons_{case.lower()}.png"), dpi=150)
    plt.close()
    print(f"Saved quicksort_comparisons_{case.lower()}.png")

print("\nDone! All 6 Quick Sort graphs were saved in the graphs/ folder.")