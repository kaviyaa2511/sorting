#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void bucketSort(vector<int>& arr) {
    int n = arr.size();
    int maxVal = *max_element(arr.begin(), arr.end());

    vector<vector<int>> bucket(n);

    
    for (int i = 0; i < n; i++) {
        int index = (arr[i] * n) / (maxVal + 1);
        bucket[index].push_back(arr[i]);
    }

    
    for (int i = 0; i < n; i++)
        sort(bucket[i].begin(), bucket[i].end());

    
    int k = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < bucket[i].size(); j++)
            arr[k++] = bucket[i][j];
}

int main() {
    vector<int> arr = {29, 25, 3, 49, 9, 37, 21, 43};

    bucketSort(arr);

    cout << "Sorted array: ";
    for (int x : arr)
        cout << x << " ";

    return 0;
}