package JAVA;

import java.util.Random;

public class MergeSort {

    /*
    ------------------------------------------------------------
    ALGORITHM : MERGE SORT

    mergeSort(A, left, right)

    Step 1: if left < right

    Step 1.1: mid = (left + right) / 2

    Step 1.2: mergeSort(A, left, mid)

    Step 1.3: mergeSort(A, mid + 1, right)

    Step 1.4: merge(A, left, mid, right)

    Step 2: return A
    ------------------------------------------------------------
    */

    // Merge Function
    public static void merge(int[] A, int left, int mid, int right) {

        int n1 = mid - left + 1;
        int n2 = right - mid;

        int[] L = new int[n1];
        int[] R = new int[n2];

        for (int i = 0; i < n1; i++)
            L[i] = A[left + i];

        for (int j = 0; j < n2; j++)
            R[j] = A[mid + 1 + j];

        int i = 0;
        int j = 0;
        int k = left;

        while (i < n1 && j < n2) {

            if (L[i] <= R[j]) {
                A[k] = L[i];
                i++;
            } else {
                A[k] = R[j];
                j++;
            }

            k++;
        }

        while (i < n1) {
            A[k] = L[i];
            i++;
            k++;
        }

        while (j < n2) {
            A[k] = R[j];
            j++;
            k++;
        }
    }

    // Merge Sort Function
    public static void mergeSort(int[] A, int left, int right) {

        if (left < right) {

            int mid = (left + right) / 2;

            mergeSort(A, left, mid);

            mergeSort(A, mid + 1, right);

            merge(A, left, mid, right);
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

            // Perform Merge Sort
            mergeSort(arr, 0, n - 1);

            if (n == 100) {
                System.out.println("\nAfter Sorting:");
                printArray(arr);
            } else {
                System.out.println("Sorting Completed.");
            }
        }

        System.out.println("\n--------------------------------------");
        System.out.println("Merge Sort Completed Successfully.");
        System.out.println("--------------------------------------");
    }
}