import time
import random

def binary_search(arr, target):
    """
    Binary Search Algorithm
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    low, high = 0, len(arr) - 1
    comparisons = 0

    while low <= high:
        comparisons += 1
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons


def performance_analysis():
    sizes = [1000, 5000, 10000, 50000, 100000]

    print(f"{'Size':>10} {'BS Time(ms)':>14} {'BS Comparisons':>16}")
    print("-" * 45)

    for size in sizes:
        arr = sorted(random.sample(range(size * 10), size))
        target = arr[random.randint(0, size - 1)]

        start = time.perf_counter()
        for _ in range(100):
            idx_bs, comp_bs = binary_search(arr, target)

        bs_time = (time.perf_counter() - start) / 100 * 1000

        print(f"{size:>10} {bs_time:>14.4f} {comp_bs:>16}")


# --- Main ---
arr = [2, 5, 10, 15, 23, 35, 48, 60, 75, 90, 105, 120]
target = 35

idx, comps = binary_search(arr, target)

print(f"Array: {arr}")
print(f"Searching for: {target}")
print(f"Found at index: {idx}, Comparisons: {comps}")
print()

performance_analysis()