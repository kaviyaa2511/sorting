#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>

using namespace std;

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

int partition(vector<int>& A,int low,int high)
{
    int pivot=A[high];

    int i=low-1;

    for(int j=low;j<high;j++)
    {
        if(A[j]<=pivot)
        {
            i++;

            swap(A[i],A[j]);
        }
    }

    swap(A[i+1],A[high]);

    return i+1;
}

void quickSort(vector<int>& A,int low,int high)
{
    if(low<high)
    {
        int p=partition(A,low,high);

        quickSort(A,low,p-1);

        quickSort(A,p+1,high);
    }
}

void printArray(vector<int> A)
{
    for(int x:A)
        cout<<x<<" ";

    cout<<endl;
}

int main()
{
    srand(time(0));

    int sizes[]={100,1000,10000,100000};

    for(int n:sizes)
    {
        vector<int> arr(n);

        for(int i=0;i<n;i++)
            arr[i]=rand()%1000;

        cout<<"\nInput Size : "<<n<<endl;

        if(n==100)
        {
            cout<<"\nBefore Sorting\n";
            printArray(arr);
        }

        quickSort(arr,0,n-1);

        if(n==100)
        {
            cout<<"\nAfter Sorting\n";
            printArray(arr);
        }
        else
        {
            cout<<"Sorting Completed.\n";
        }

        cout<<"--------------------------------------\n";
    }

    return 0;
}