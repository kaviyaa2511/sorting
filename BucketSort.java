package Sorting.java;

import java.util.ArrayList;
import java.util.Collections;

public class BucketSort {

    public static void bucketSort(int[] arr) {
        int n = arr.length;

        
        int max = arr[0];
        for (int i = 1; i < n; i++) {
            if (arr[i] > max)
                max = arr[i];
        }

        
        ArrayList<ArrayList<Integer>> buckets = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            buckets.add(new ArrayList<Integer>());
        }

        
        for (int i = 0; i < n; i++) {
            int index = (arr[i] * n) / (max + 1);
            buckets.get(index).add(arr[i]);
        }

       
        for (int i = 0; i < n; i++) {
            Collections.sort(buckets.get(i));
        }

       
        int k = 0;
        for (int i = 0; i < n; i++) {
            for (int num : buckets.get(i)) {
                arr[k++] = num;
            }
        }
    }

    public static void main(String[] args) {
        int[] arr = {29, 25, 3, 49, 9, 37, 21, 43};

        bucketSort(arr);

        System.out.println("Sorted Array:");
        for (int num : arr) {
            System.out.print(num + " ");
        }
    }
}
