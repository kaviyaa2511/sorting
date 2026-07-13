import random

'''
heapify(num, n, i)
Step 1: largest = i
Step 2: l = 2 * i + 1
Step 3: r = 2 * i + 2
Step 4: if l < n and num[l] > num[largest]
Step 4.1: largest = l
Step 5: if r < n and num[r] > num[largest]
Step 5.1: largest = r
Step 6: if largest != i
Step 6.1: swap(num[i], num[largest])
Step 6.2: heapify(num, n, largest)
Step 7: return

heapSort(num)
Step 1: n = length(num)
Step 2: i = n/2 - 1
Step 3: while i >= 0
Step 3.1: heapify(num, n, i)
Step 3.2: i = i - 1
Step 4: i = n - 1
Step 5: while i > 0
Step 5.1: swap(num[0], num[i])
Step 5.2: heapify(num, i, 0)
Step 5.3: i = i - 1
Step 6: return num
'''

def heapify(num, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and num[l] > num[largest]:
        largest = l
    if r < n and num[r] > num[largest]:
        largest = r
    if largest != i:
        num[i], num[largest] = num[largest], num[i]
        heapify(num, n, largest)

# Heap Sort
def heapSort(num, n):
    i = n // 2 - 1
    while i >= 0:
        heapify(num, n, i)
        i = i - 1
    i = n - 1
    while i > 0:
        num[0], num[i] = num[i], num[0]
        heapify(num, i, 0)
        i = i - 1
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
        sorted_arr = heapSort(arr.copy(), len(arr))
        print(f"{name} case sorted successfully.")