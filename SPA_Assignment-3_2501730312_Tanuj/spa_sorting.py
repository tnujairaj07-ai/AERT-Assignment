import random
import time


# ---------- Insertion Sort ----------
def insertion_sort(arr):
    a = arr[:]           # work on a copy, keep it simple
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


# ---------- Merge Sort ----------
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:   # <= to keep it stable
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


# ---------- Quick Sort (helper) ----------
def _partition(a, low, high):
    pivot = a[high]          # last element as pivot
    i = low - 1
    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1


def _quick_sort_iterative(a, low, high):
    stack = [(low, high)]
    while stack:
        l, h = stack.pop()
        if l < h:
            p = _partition(a, l, h)
            # Push right side first, then left side
            if p + 1 < h:
                stack.append((p + 1, h))
            if l < p - 1:
                stack.append((l, p - 1))


def quick_sort(arr):
    a = arr[:]
    if len(a) > 1:
        _quick_sort_iterative(a, 0, len(a) - 1)
    return a


def check_correctness():
    test = [5, 2, 9, 1, 5, 6]
    expected = [1, 2, 5, 5, 6, 9]
    print("Correctness check on", test)

    for name, func in [
        ("Insertion Sort", insertion_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort),
    ]:
        out = func(test)
        print(f"{name}: {out}, OK =", out == expected)


# ---------- Timing Utility ----------
def measure_time(sort_func, arr):
    data = arr[:]                 # same data for each algorithm
    start = time.time()
    sort_func(data)
    end = time.time()
    return (end - start) * 1000.0 # ms


# ---------- Dataset Generator ----------
SIZES = [1000, 5000, 10000]


def generate_datasets():
    random.seed(42)  # fixed seed for repeatability
    datasets = []

    for n in SIZES:
        # random
        rand_list = [random.randint(1, 100000) for _ in range(n)]
        # sorted
        sorted_list = sorted(rand_list)
        # reverse-sorted
        rev_list = sorted_list[::-1]

        datasets.append(("random", n, rand_list))
        datasets.append(("sorted", n, sorted_list))
        datasets.append(("reverse", n, rev_list))

    return datasets


def run_experiments():
    datasets = generate_datasets()

    # To also save console output in output.txt, we build a big string
    lines = []

    lines.append("Sorting Performance Analyzer (SPA)\n")
    lines.append("Correctness Check:\n")
    test = [5, 2, 9, 1, 5, 6]
    expected = [1, 2, 5, 5, 6, 9]
    lines.append(f"Test list: {test}\n")
    for name, func in [
        ("Insertion Sort", insertion_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort),
    ]:
        out = func(test)
        lines.append(f"{name}: {out}, OK = {out == expected}\n")

    header = "\nTiming results (ms):\n"
    lines.append(header)
    print(header.strip())

    table_header = f"{'Type':<10} {'Size':<8} {'Algorithm':<15} {'Time (ms)':>10}"
    lines.append(table_header + "\n")
    print(table_header)

    for input_type, n, arr in datasets:
        for name, func in [
            ("Insertion Sort", insertion_sort),
            ("Merge Sort", merge_sort),
            ("Quick Sort", quick_sort),
        ]:
            t = measure_time(func, arr)
            row = f"{input_type:<10} {n:<8} {name:<15} {t:>10.3f}"
            lines.append(row + "\n")
            print(row)

            print("About to write output.txt")
            with open("output.txt", "w", encoding="utf-8") as f:
                f.writelines(lines)
                print("Finished writing output.txt")

    # Write to output.txt
    with open("output.txt", "w", encoding="utf-8") as f:
        f.writelines(lines)

    print("\nResults also saved to output.txt")


if __name__ == "__main__":
    check_correctness()
    run_experiments()