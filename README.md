# How to Run

## Scripts

- **main.py** - Executes all three Quick Sort variants and logs execution time and comparison counts to `quick_results.csv`.

- **final_main.py** - Runs all 7 sorting algorithms (including Quick Sort with median-of-three pivot selection) and outputs metrics to `final_results.csv`.
  - To switch algorithms, modify the `ALGO_NAME` variable in `final_main.py` at line 20.

- All seven sorting algorithms are implemented in the `sorting_algorithms/` directory.

## Test Cases

Test data is located in the `testcases/` directory.

## How to Execute

To run any script, use the command:

```bash
python3 <file_name>
```

For example:

```bash
python3 main.py
python3 final_main.py
```
