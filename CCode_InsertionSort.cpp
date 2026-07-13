#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

void insertionSort(int num[], int n)
{
    int i = 1;
    while (i < n)
    {
        int k = num[i];
        int j = i - 1;
        while (j >= 0 && num[j] > k)
        {
            num[j + 1] = num[j];
            j = j - 1;
        }
        num[j + 1] = k;
        i++;
    }
}

// 1. Random
void randomCase(int a[], int n)
{
    int i = 0;
    while (i < n)
    {
        a[i] = rand() % (n * 10) + 1;
        i++;
    }
}

// 2. Ascending
void ascendingCase(int a[], int n)
{
    int i = 0;
    while (i < n)
    {
        a[i] = i + 1;
        i++;
    }
}

// 3. Descending
void descendingCase(int a[], int n)
{
    int i = 0;
    while (i < n)
    {
        a[i] = n - i;
        i++;
    }
}

// 4. Partial Order
void partialOrderCase(int a[], int n)
{
    ascendingCase(a, n);
    int swaps = n / 5;
    int i = 0;
    while (i < swaps)
    {
        int x = rand() % n;
        int y = rand() % n;
        int temp = a[x];
        a[x] = a[y];
        a[y] = temp;
        i++;
    }
}

// 5. Missing Number
void missingNumberCase(int a[], int n)
{
    int missing = rand() % (n + 1) + 1;
    int i = 1;
    int j = 0;
    while (i <= n + 1)
    {
        if (i != missing)
        {
            a[j] = i;
            j++;
        }
        i++;
    }
}

// 6. Duplicate Values
void duplicateValuesCase(int a[], int n)
{
    int i = 0;
    while (i < n)
    {
        a[i] = rand() % (n / 2) + 1;
        i++;
    }
}

int main()
{
    srand(time(0));
    int sizes[] = {100, 1000, 10000, 100000};
    cout << "1. Random\n";
    cout << "2. Ascending\n";
    cout << "3. Descending\n";
    cout << "4. Partial Order\n";
    cout << "5. Missing Number\n";
    cout << "6. Duplicate Values\n";
    int choice;
    cin >> choice;
    for (int k = 0; k < 4; k++)
    {
        int n = sizes[k];
        int a[n];
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
        else
        {
            cout << "Invalid Choice";
            return 0;
        }
        insertionSort(a, n);
        cout << "Input Size = " << n << " : Sorted Successfully" << endl;
    }
    return 0;
}







