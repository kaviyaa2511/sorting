
# Description:
# Generates different test cases for sorting algorithms.

# Test Cases:
# 1. Random
# 2. Ascending
# 3. Descending
# 4. Partial Order
# 5. Missing Number
# 6. Duplicate Values

import random

# 1. Random Numbers
def random_case(size):
    return random.sample(range(1, size * 10), size)



# 2. Ascending Order
def ascending_case(size):
    return list(range(1, size + 1))


# 3. Descending Order
def descending_case(size):
    return list(range(size, 0, -1))



# 4. Partial Order
# First half sorted, second half random
def partial_order_case(size):

    first_half = list(range(1, size // 2 + 1))

    second_half = random.sample(
        range(size + 1, size * 10),
        size - size // 2
    )

    return first_half + second_half



# 5. Missing Number
# One number is removed from the sequence.

def missing_number_case(size):

    arr = list(range(1, size + 1))

    missing = random.randint(1, size)

    arr.remove(missing)

    return arr



# 7. Duplicate Values
# Many repeated values.

def duplicate_values_case(size):

    return [
        random.randint(1, max(2, size // 10))
        for _ in range(size)
    ]


# Return all test cases

def get_test_cases(size):

    return {

        "Random": random_case(size),

        "Ascending": ascending_case(size),

        "Descending": descending_case(size),

        "Partial Order": partial_order_case(size),

        "Missing Number": missing_number_case(size),

        "Missing + Duplicate": missing_duplicate_case(size),

        "Duplicate Values": duplicate_values_case(size)

    }


# Input Sizes
INPUT_SIZES = [100, 1000, 10000, 100000]


# Test Driver
if __name__ == "__main__":

    for size in INPUT_SIZES:

        print(f"\nInput Size : {size}")

        test_cases = get_test_cases(size)

        for name, arr in test_cases.items():

            print(f"{name:25} -> {len(arr)} elements")
