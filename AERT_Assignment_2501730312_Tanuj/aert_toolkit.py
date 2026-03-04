# ---------- Part A: Stack ADT ----------

class StackADT:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# I used StackADT to store mid indices visited in binary search
binary_search_trace_stack = StackADT()

# ---------- Part B: Factorial & Fibonacci ----------

def factorial(n):
    """Recursive factorial, handles n >= 0."""
    if n < 0:
        # invalid input
        return None
    # base case
    if n == 0:
        return 1
    # recursive case
    return n * factorial(n - 1)


# global counters for fibonacci
naive_calls = 0
memo_calls = 0

def fib_naive(n):
    """Simple recursive fibonacci without memoization."""
    global naive_calls
    naive_calls += 1

    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


def fib_memo(n, memo=None):
    """Recursive fibonacci with memoization."""
    global memo_calls
    memo_calls += 1

    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        memo[n] = n
        return n

    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


# ---------- Part C: Tower of Hanoi ----------

def hanoi(n, source, auxiliary, destination):
    """Recursive Tower of Hanoi solution."""
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    hanoi(n - 1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    hanoi(n - 1, auxiliary, source, destination)


# ---------- Part D: Recursive Binary Search ----------

def binary_search(arr, key, low, high):
    """Recursive binary search. Returns index or -1."""
    if low > high:
        return -1

    mid = (low + high) // 2

    # store mid index in stack trace
    binary_search_trace_stack.push(mid)

    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_search(arr, key, low, mid - 1)
    else:
        return binary_search(arr, key, mid + 1, high)


# ---------- Helper to run test cases ----------

def test_factorial():
    print("Factorial Test Cases:")
    for n in [0, 1, 5, 10]:
        result = factorial(n)
        print(f"factorial({n}) = {result}")
    print()


def test_fibonacci():
    global naive_calls, memo_calls

    print("Fibonacci Test Cases:")
    for n in [5, 10, 20, 30]:
        naive_calls = 0
        memo_calls = 0

        val_naive = fib_naive(n)
        val_memo = fib_memo(n)

        print(f"n = {n}")
        print(f"  fib_naive({n}) = {val_naive}, calls = {naive_calls}")
        print(f"  fib_memo({n})  = {val_memo}, calls = {memo_calls}")
        print()
    print()


def test_hanoi():
    print("Tower of Hanoi for N = 3:")
    hanoi(3, "A", "B", "C")
    print()


def test_binary_search():
    print("Binary Search Test Cases:")

    arr = [1, 3, 5, 7, 9, 11, 13]
    keys = [7, 1, 13, 2]

    print("Array:", arr)
    for key in keys:
          # clear stack before each search
        while not binary_search_trace_stack.is_empty():
            binary_search_trace_stack.pop()

        index = binary_search(arr, key, 0, len(arr) - 1)
        print(f"search {key} -> index {index}")

        # print mid indices visited from stack
        trace = []
        while not binary_search_trace_stack.is_empty():
            trace.append(binary_search_trace_stack.pop())
        trace.reverse()  # because stack is LIFO
        print("  mid indices visited:", trace)

    # empty array case
    empty_arr = []
    key = 5
    index = binary_search(empty_arr, key, 0, len(empty_arr) - 1)
    print("\nEmpty array test:")
    print("Array:", empty_arr)
    print(f"search {key} -> index {index}")
    print()


def main():
    test_factorial()
    test_fibonacci()
    test_hanoi()
    test_binary_search()


if __name__ == "__main__":
    main()
