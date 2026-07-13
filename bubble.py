
# ALGORITHM : BUBBLE SORT
#
# bubbleSort(a)
#
# Step 1: Let n = length of a
#
# Step 2: Repeat for i = 0 to n - 2
#
# Step 2.1: Repeat for j = 0 to n - i - 2
#
# Step 2.1.1: Compare a[j] and a[j + 1]
#
# Step 2.1.2: If a[j] > a[j + 1]
#
# Step 2.1.2.1: Swap a[j] and a[j + 1]
#
# Step 2.2: Largest element is placed at its correct position
#
# Step 3: Repeat until all passes are completed
#
# Step 4: Return a

import random
import time

# Bubble Sort
def bubbleSort(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


# 1. Random
def random_case(n):
    return random.sample(range(1, n * 10), n)


# 2. Ascending
def ascending_case(n):
    return list(range(1, n + 1))


# 3. Descending
def descending_case(n):
    return list(range(n, 0, -1))


# 4. Partial Order
def partial_order_case(n):
    arr = list(range(1, n + 1))
    swaps = n // 5

    for _ in range(swaps):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        arr[i], arr[j] = arr[j], arr[i]

    return arr


# 5. Missing Number
def missing_number_case(n):
    arr = list(range(1, n + 2))
    arr.remove(random.choice(arr))
    return arr


# 6. Duplicate Values
def duplicate_values_case(n):
    return [random.randint(1, n // 2) for _ in range(n)]


# Input sizes
sizes = [100, 1000, 10000]
times = []

for n in sizes:

    print(f"\n{'='*40}")
    print(f"Input Size = {n}")
    print(f"{'='*40}")

    cases = {
        "Random": random_case(n),
        "Ascending": ascending_case(n),
        "Descending": descending_case(n),
        "Partial Order": partial_order_case(n),
        "Missing Number": missing_number_case(n),
        "Duplicate Values": duplicate_values_case(n)
    }

    for name, arr in cases.items():
        start = time.perf_counter()
        sorted_arr = bubbleSort(arr.copy())
        end = time.perf_counter()

        print(f"{name} case sorted successfully.")
        times.append(end - start)

        

print("\nExecution Times:")
print(times)