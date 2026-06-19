import time
import random

def linear_search(arr, target):
    """
    Linear Search Algorithm
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    comparisons = 0

    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons

    return -1, comparisons


def performance_analysis():
    sizes = [1000, 5000, 10000, 50000, 100000]

    print(f"{'Size':>10} {'LS Time(ms)':>14} {'LS Comparisons':>16}")
    print("-" * 45)

    for size in sizes:
        arr = sorted(random.sample(range(size * 10), size))
        target = arr[random.randint(0, size - 1)]

        start = time.perf_counter()
        for _ in range(100):
            idx_ls, comp_ls = linear_search(arr, target)

        ls_time = (time.perf_counter() - start) / 100 * 1000

        print(f"{size:>10} {ls_time:>14.4f} {comp_ls:>16}")


# --- Main ---
arr = [2, 5, 10, 15, 23, 35, 48, 60, 75, 90, 105, 120]
target = 35

idx, comps = linear_search(arr, target)

print(f"Array: {arr}")
print(f"Searching for: {target}")
print(f"Found at index: {idx}, Comparisons: {comps}")
print()

performance_analysis()