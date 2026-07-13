import java.util.Random;
import java.util.Scanner;

public class InsertionSortCases {
    static void insertionSort(int num[], int n) {
        int i = 1;
        while (i < n) {
            int k = num[i];
            int j = i - 1;
            while (j >= 0 && num[j] > k) {
                num[j + 1] = num[j];
                j = j - 1;
            }
            num[j + 1] = k;
            i++;
        }
    }

    // 1. Random
    static void randomCase(int a[], int n) {
        Random r = new Random();
        int i = 0;
        while (i < n) {
            a[i] = r.nextInt(n * 10) + 1;
            i++;
        }
    }

    // 2. Ascending
    static void ascendingCase(int a[], int n) {
        int i = 0;
        while (i < n) {
            a[i] = i + 1;
            i++;
        }
    }

    // 3. Descending
    static void descendingCase(int a[], int n) {
        int i = 0;
        while (i < n) {
            a[i] = n - i;
            i++;
        }
    }

    // 4. Partial Order
    static void partialOrderCase(int a[], int n) {
        ascendingCase(a, n);
        Random r = new Random();
        int swaps = n / 5;
        int i = 0;
        while (i < swaps) {
            int x = r.nextInt(n);
            int y = r.nextInt(n);
            int temp = a[x];
            a[x] = a[y];
            a[y] = temp;
            i++;
        }
    }

    // 5. Missing Number
    static void missingNumberCase(int a[], int n) {
        Random r = new Random();
        int missing = r.nextInt(n + 1) + 1;
        int i = 1;
        int j = 0;
        while (i <= n + 1) {
            if (i != missing) {
                a[j] = i;
                j++;
            }
            i++;
        }
    }
    // 6. Duplicate Values
    static void duplicateValuesCase(int a[], int n) {
        Random r = new Random();
        int i = 0;
        while (i < n) {
            a[i] = r.nextInt(n / 2) + 1;
            i++;
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] sizes = {100, 1000, 10000, 100000};
        System.out.println("1. Random");
        System.out.println("2. Ascending");
        System.out.println("3. Descending");
        System.out.println("4. Partial Order");
        System.out.println("5. Missing Number");
        System.out.println("6. Duplicate Values");
        int choice = sc.nextInt();
        int k = 0;
        while (k < sizes.length) {
            int n = sizes[k];
            int[] a = new int[n];
            if (choice == 1)
                randomCase(a, n);
            else if (choice == 2)
                ascendingCase(a, n);
            else if (choice == 3)
                descendingCase(a, n);
            else if (choice == 4)
                partialOrderCase(a, n);
            else if (choice == 5)
                missingNumberCase(a, n);
            else if (choice == 6)
                duplicateValuesCase(a, n);
            else {
                System.out.println("Invalid Choice");
                return;
            }
            insertionSort(a, n);
            System.out.println("Input Size = " + n + " : Sorted Successfully");
            k++;
        }
        sc.close();
    }
}