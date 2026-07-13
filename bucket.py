# ALGORITHM : BUCKET SORT
#
# bucketSort(A)
#
# Step 1: n ← length(A)
#
# Step 2: max_val ← max(A)
#
# Step 3: Create n empty buckets
#
# Step 4: Repeat for each element in A
#
# Step 4.1: index ← (element × n) // (max_val + 1)
#
# Step 4.2: bucket[index] ← bucket[index] + element
#
# Step 5: Sort each bucket
#
# Step 6: result ← Merge all buckets
#
# Step 7: Return result


import random
import time

# Bucket Sort
def bucketSort(arr):
    n = len(arr)
    max_val = max(arr)
    buckets = [[] for _ in range(n)]   
    for num in arr:
        index = (num * n) // (max_val + 1)
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()

   
    result = []
    for bucket in buckets:
        result.extend(bucket)

    return result


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



sizes = [100, 1000, 10000]
times = []

for n in sizes:

    print(f"\n{'=' * 40}")
    print(f"Input Size = {n}")
    print(f"{'=' * 40}")

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
        sorted_arr = bucketSort(arr.copy())
        end = time.perf_counter()

        print(f"{name} case sorted successfully.")
        times.append(end - start)

        

print("\nExecution Times:")
print(times)