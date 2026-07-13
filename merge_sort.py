# ------------------------------------------------------------
# File Name : merge_sort.py
#
# Program : Merge Sort Performance Analysis
#
# Description:
# Performs Merge Sort on different test cases generated
# from test_cases.py and measures execution time.
#
# Graphs are generated using matplotlib and saved as PNG.
# ------------------------------------------------------------


# ------------------------------------------------------------
# ALGORITHM : MERGE SORT
#
# mergeSort(A, left, right)
#
# Step 1: if left < right
#
# Step 1.1: mid = (left + right) // 2
#
# Step 1.2: mergeSort(A, left, mid)
#
# Step 1.3: mergeSort(A, mid + 1, right)
#
# Step 1.4: merge(A, left, mid, right)
#
# Step 2: return A
#
#
# merge(A, left, mid, right)
#
# Step 1: Create Left[] and Right[]
#
# Step 2: i = 0, j = 0, k = left
#
# Step 3: while i < len(Left) and j < len(Right)
#
# Step 3.1: if Left[i] <= Right[j]
#
# Step 3.1.1: A[k] = Left[i]
#
# Step 3.1.2: i = i + 1
#
# Step 3.2: else
#
# Step 3.2.1: A[k] = Right[j]
#
# Step 3.2.2: j = j + 1
#
# Step 3.3: k = k + 1
#
# Step 4: Copy remaining Left[]
#
# Step 5: Copy remaining Right[]
#
# Step 6: return A
# ------------------------------------------------------------


import os
import time
import matplotlib.pyplot as plt

from test_cases import INPUT_SIZES
from test_cases import get_test_cases


# ------------------------------------------------------------
# Merge Function
# ------------------------------------------------------------

def merge(A, left, mid, right):

    Left = A[left:mid + 1]
    Right = A[mid + 1:right + 1]

    i = 0
    j = 0
    k = left

    while i < len(Left) and j < len(Right):

        if Left[i] <= Right[j]:

            A[k] = Left[i]
            i += 1

        else:

            A[k] = Right[j]
            j += 1

        k += 1

    while i < len(Left):

        A[k] = Left[i]
        i += 1
        k += 1

    while j < len(Right):

        A[k] = Right[j]
        j += 1
        k += 1


# ------------------------------------------------------------
# Merge Sort
# ------------------------------------------------------------

def mergeSort(A, left, right):

    if left < right:

        mid = (left + right) // 2

        mergeSort(A, left, mid)

        mergeSort(A, mid + 1, right)

        merge(A, left, mid, right)


# ------------------------------------------------------------
# Measure Execution Time
# ------------------------------------------------------------

def measure_time(array):

    A = array.copy()

    start = time.perf_counter()

    mergeSort(A, 0, len(A) - 1)

    end = time.perf_counter()

    return (end - start) * 1000

# ------------------------------------------------------------
# Create Graph Folder
# ------------------------------------------------------------

GRAPH_FOLDER = "graphs"

if not os.path.exists(GRAPH_FOLDER):
    os.makedirs(GRAPH_FOLDER)


# ------------------------------------------------------------
# Main Program
# ------------------------------------------------------------

print("\nMERGE SORT PERFORMANCE ANALYSIS")
print("-" * 50)

# Loop through every test case
for case_name in get_test_cases(INPUT_SIZES[0]).keys():

    print(f"\nTest Case : {case_name}")

    execution_time = []

    # Loop through each input size
    for size in INPUT_SIZES:

        # Generate all test cases for the current size
        test_cases = get_test_cases(size)

        # Select the required test case
        array = test_cases[case_name]

        # Measure execution time
        time_taken = measure_time(array)

        execution_time.append(time_taken)

        print(f"Input Size : {len(array):6}    "
              f"Execution Time : {time_taken:.3f} ms")

# --------------------------------------------------------
# Plot Graph
# --------------------------------------------------------

plt.figure(figsize=(12, 7))

# Create equally spaced x-axis positions
x_positions = list(range(len(INPUT_SIZES)))

plt.plot(
    x_positions,
    execution_time,
    marker='o',
    linestyle='-',
    linewidth=2.5,
    markersize=8,
    label="Merge Sort"
)

# Display execution time above each point
offset = max(execution_time) * 0.03 if max(execution_time) > 0 else 0.01

for x, y in zip(x_positions, execution_time):

    plt.text(
        x,
        y + offset,
        f"{y:.3f}",
        ha='center',
        va='bottom',
        fontsize=10
    )

plt.title(f"Merge Sort - {case_name}", fontsize=16, fontweight='bold')

plt.xlabel("Number of Inputs (n)", fontsize=13)

plt.ylabel("Execution Time (ms)", fontsize=13)

# Display original input sizes with equal spacing
plt.xticks(
    x_positions,
    [str(size) for size in INPUT_SIZES],
    fontsize=11
)

plt.yticks(fontsize=11)

plt.grid(True, linestyle='--', alpha=0.6)

plt.legend(fontsize=11)

plt.tight_layout()

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
print("Merge Sort Performance Analysis Completed")
print("Graphs saved inside the 'graphs' folder.")
print("--------------------------------------------")

    """# --------------------------------------------------------
    # Plot Graph
    # --------------------------------------------------------

    plt.figure(figsize=(10, 6))

    plt.plot(
        INPUT_SIZES,
        execution_time,
        marker='o',
        linestyle='-',
        linewidth=2,
        markersize=8,
        label="Merge Sort"
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

    plt.title(f"Merge Sort - {case_name}", fontsize=16)

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
print("Merge Sort Performance Analysis Completed")
print("Graphs saved inside the 'graphs' folder.")
print("--------------------------------------------") """