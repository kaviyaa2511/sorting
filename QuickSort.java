package JAVA;

import java.util.Random;

public class QuickSort {

    /*
    ------------------------------------------------------------
    ALGORITHM : QUICK SORT

    quickSort(A, low, high)

    Step 1: if low < high

    Step 1.1: pivot = partition(A, low, high)

    Step 1.2: quickSort(A, low, pivot-1)

    Step 1.3: quickSort(A, pivot+1, high)

    Step 2: return A
    ------------------------------------------------------------
    */

    // Partition Function
    public static int partition(int[] A, int low, int high) {

        int pivot = A[high];

        int i = low - 1;

        for (int j = low; j < high; j++) {

            if (A[j] <= pivot) {

                i++;

                int temp = A[i];
                A[i] = A[j];
                A[j] = temp;
            }
        }

        int temp = A[i + 1];
        A[i + 1] = A[high];
        A[high] = temp;

        return i + 1;
    }

    // Quick Sort Function
    public static void quickSort(int[] A, int low, int high) {

        if (low < high) {

            int pivot = partition(A, low, high);

            quickSort(A, low, pivot - 1);

            quickSort(A, pivot + 1, high);
        }
    }

    // Print Array
    public static void printArray(int[] A) {

        for (int x : A)
            System.out.print(x + " ");

        System.out.println();
    }

    // Main Function
    public static void main(String[] args) {

        int[] inputSizes = {100, 1000, 10000, 100000};

        Random rand = new Random();

        for (int n : inputSizes) {

            int[] arr = new int[n];

            // Generate Random Numbers
            for (int i = 0; i < n; i++) {
                arr[i] = rand.nextInt(1000);
            }

            System.out.println("\n======================================");
            System.out.println("Input Size : " + n);
            System.out.println("======================================");

            // Print only for 100 elements
            if (n == 100) {
                System.out.println("\nBefore Sorting:");
                printArray(arr);
            } else {
                System.out.println("\nRandom array generated.");
            }

            // Perform Quick Sort
            quickSort(arr, 0, n - 1);

            if (n == 100) {
                System.out.println("\nAfter Sorting:");
                printArray(arr);
            } else {
                System.out.println("Sorting Completed.");
            }
        }

        System.out.println("\n--------------------------------------");
        System.out.println("Quick Sort Completed Successfully.");
        System.out.println("--------------------------------------");
    }
}