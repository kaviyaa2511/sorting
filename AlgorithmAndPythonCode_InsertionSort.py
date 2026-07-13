import random

'''
insertionSort(num, n)
Step 1: i = 1
Step 2: while i < n
Step 2.1: k = num[i]
Step 2.2: j = i - 1
Step 2.3: while j >= 0 and num[j] > k
Step 2.3.1: num[j + 1] = num[j]
Step 2.3.2: j = j - 1
Step 2.4: num[j + 1] = k
Step 2.5: i = i + 1
Step 3: return num
'''

def insertionSort(num, n):
    i = 1
    while i < n:
        k = num[i]
        j = i - 1
        while j >= 0 and num[j] > k:
            num[j + 1] = num[j]
            j = j - 1
        num[j + 1] = k
        i = i + 1
    return num


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
sizes = [100, 1000, 10000, 100000]
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
        sorted_arr = insertionSort(arr.copy(), len(arr))
        print(f"{name} case sorted successfully.")
