# ------------------------------------------------------------
# File Name : quick_sort.py
#
# Program : Quick Sort Performance Analysis
#
# Description:
# Performs Quick Sort on different test cases generated
# from test_cases.py and measures execution time.
#
# Graphs are generated using matplotlib and saved as PNG.
# ------------------------------------------------------------


# ------------------------------------------------------------
# ALGORITHM : QUICK SORT
#
# quickSort(A, low, high)
#
# Step 1: if low < high
#
# Step 1.1: pivot = partition(A, low, high)
#
# Step 1.2: quickSort(A, low, pivot-1)
#
# Step 1.3: quickSort(A, pivot+1, high)
#
# Step 2: return A
#
#
# partition(A, low, high)
#
# Step 1: pivot = A[high]
#
# Step 2: i = low - 1
#
# Step 3: for j = low to high-1
#
# Step 3.1: if A[j] <= pivot
#
# Step 3.1.1: i = i + 1
#
# Step 3.1.2: swap(A[i], A[j])
#
# Step 4: swap(A[i+1], A[high])
#
# Step 5: return i + 1
# ------------------------------------------------------------


import os
import time
import matplotlib.pyplot as plt

from test_cases import INPUT_SIZES
from test_cases import get_test_cases


# ------------------------------------------------------------
# Partition Function
# ------------------------------------------------------------

def partition(A, low, high):

    pivot = A[high]

    i = low - 1

    for j in range(low, high):

        if A[j] <= pivot:

            i += 1

            A[i], A[j] = A[j], A[i]

    A[i + 1], A[high] = A[high], A[i + 1]

    return i + 1


# ------------------------------------------------------------
# Quick Sort Function
# ------------------------------------------------------------

def quickSort(A, low, high):

    if low < high:

        pivot = partition(A, low, high)

        quickSort(A, low, pivot - 1)

        quickSort(A, pivot + 1, high)


# ------------------------------------------------------------
# Measure Execution Time
# ------------------------------------------------------------

def measure_time(array):

    A = array.copy()

    start = time.perf_counter()

    quickSort(A, 0, len(A) - 1)

    end = time.perf_counter()

    return (end - start) * 1000
# ------------------------------------------------------------
# Create Graph Folder
# ------------------------------------------------------------

import random

GRAPH_FOLDER = os.path.join("graphs", "Merge_Sort")

os.makedirs(GRAPH_FOLDER, exist_ok=True)


# ------------------------------------------------------------
# Random Pivot Partition
# ------------------------------------------------------------

def random_partition(A, low, high):

    random_index = random.randint(low, high)

    A[random_index], A[high] = A[high], A[random_index]

    return partition(A, low, high)


# ------------------------------------------------------------
# Quick Sort (Random Pivot)
# ------------------------------------------------------------

def quickSort(A, low, high):

    if low < high:

        pivot = random_partition(A, low, high)

        quickSort(A, low, pivot - 1)

        quickSort(A, pivot + 1, high)


# ------------------------------------------------------------
# Main Program
# ------------------------------------------------------------

print("\nQUICK SORT PERFORMANCE ANALYSIS")
print("-" * 50)

# Loop through every test case
for case_name in get_test_cases(INPUT_SIZES[0]).keys():

    print(f"\nTest Case : {case_name}")

    execution_time = []

    # Loop through each input size
    for size in INPUT_SIZES:

        # Generate all test cases
        test_cases = get_test_cases(size)

        # Select required test case
        array = test_cases[case_name]

        # Measure execution time
        time_taken = measure_time(array)

        execution_time.append(time_taken)

        print(f"Input Size : {len(array):6}    "
              f"Execution Time : {time_taken:.3f} ms")

# ------------------------------------------------------------
# Plot Graph
# ------------------------------------------------------------

    plt.figure(figsize=(10, 6))

    plt.plot(
        INPUT_SIZES,
        execution_time,
        marker='o',
        linestyle='-',
        linewidth=2,
        markersize=8,
        color='green',
        label='Quick Sort'
    )

    # Display execution time above each point
    for x, y in zip(INPUT_SIZES, execution_time):

        plt.text(
            x,
            y + (max(execution_time) * 0.03),
            f"{y:.3f}",
            ha='center',
            fontsize=10
        )

    plt.title(f"Quick Sort - {case_name}", fontsize=16)

    plt.xlabel("Number of Inputs (n)", fontsize=12)

    plt.ylabel("Execution Time (ms)", fontsize=12)

    plt.xticks(INPUT_SIZES)

    plt.grid(True)

    plt.legend()

    # Save graph
    file_name = case_name.replace(" ", "_").replace("+", "Plus")

    plt.savefig(
        os.path.join(GRAPH_FOLDER, f"{file_name}.png"),
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    print(f"Graph Saved : graphs/{file_name}.png")


print("\n--------------------------------------------")
print("Quick Sort Performance Analysis Completed")
print("Graphs saved inside the 'graphs' folder.")
print("--------------------------------------------")