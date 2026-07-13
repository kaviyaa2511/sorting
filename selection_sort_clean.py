import random
import time

def selectionSort(a):
    n = len(a)
    i = 0
    while i < n - 1:
        min = i
        j = i + 1
        while j < n:
            if a[j] < a[min]:
                min = j
            j += 1
        a[i], a[min] = a[min], a[i]
        i += 1

    return a


def random_case(n):
    return random.sample(range(1, n * 10), n)


def ascending_case(n):
    return list(range(1, n + 1))


def descending_case(n):
    return list(range(n, 0, -1))


def partial_order_case(n):
    arr = list(range(1, n + 1))
    swaps = n // 5

    for _ in range(swaps):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        arr[i], arr[j] = arr[j], arr[i]

    return arr


def missing_number_case(n):
    arr = list(range(1, n + 2))
    arr.remove(random.choice(arr))
    return arr


def duplicate_values_case(n):
    return [random.randint(1, n // 2) for _ in range(n)]


sizes = [100,1000,10000]
times=[]
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
        start=time.perf_counter()
        sorted_arr = selectionSort(arr.copy())
        print(f"{name} case sorted successfully.")
        end=time.perf_counter()
        times.append(end-start)

print(times)