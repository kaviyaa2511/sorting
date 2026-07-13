import random
import time

def countingSort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    i = 0
    while i < n:
        index = (arr[i] // exp) % 10
        count[index] += 1
        i += 1

    i = 1
    while i < 10:
        count[i] += count[i - 1]
        i += 1

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    i = 0
    while i < n:
        arr[i] = output[i]
        i += 1


def radixSort(arr):
    maximum = max(arr)
    exp = 1

    while maximum // exp > 0:
        countingSort(arr, exp)
        exp *= 10

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


sizes = [100,1000,10000,100000]
times=[]

print("1. Random")
print("2. Ascending")
print("3. Descending")
print("4. Partial Order")
print("5. Missing Number")
print("6. Duplicate Values")

choice = int(input("Enter case number: "))

for n in sizes:
    if choice == 1:
        arr = random_case(n)
    elif choice == 2:
        arr = ascending_case(n)
    elif choice == 3:
        arr = descending_case(n)
    elif choice == 4:
        arr = partial_order_case(n)
    elif choice == 5:
        arr = missing_number_case(n)
    elif choice == 6:
        arr = duplicate_values_case(n)

    else:
        print("Invalid Choice")
        break
    start = time.perf_counter()
    radixSort(arr)

    end = time.perf_counter()
    times.append(end-start)

    print(f"Input Size = {n} : Sorted Successfully")
    print(times)
