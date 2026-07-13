#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>

using namespace std;

/*
------------------------------------------------------------
ALGORITHM : MERGE SORT

mergeSort(A, left, right)

Step 1: if left < right

Step 1.1: mid = (left + right) / 2

Step 1.2: mergeSort(A, left, mid)

Step 1.3: mergeSort(A, mid+1, right)

Step 1.4: merge(A, left, mid, right)

Step 2: return A
------------------------------------------------------------
*/

void merge(vector<int>& A, int left, int mid, int right)
{
    int n1 = mid - left + 1;
    int n2 = right - mid;

    vector<int> L(n1), R(n2);

    for(int i=0;i<n1;i++)
        L[i]=A[left+i];

    for(int j=0;j<n2;j++)
        R[j]=A[mid+1+j];

    int i=0,j=0,k=left;

    while(i<n1 && j<n2)
    {
        if(L[i]<=R[j])
            A[k++]=L[i++];
        else
            A[k++]=R[j++];
    }

    while(i<n1)
        A[k++]=L[i++];

    while(j<n2)
        A[k++]=R[j++];
}

void mergeSort(vector<int>& A,int left,int right)
{
    if(left<right)
    {
        int mid=(left+right)/2;

        mergeSort(A,left,mid);

        mergeSort(A,mid+1,right);

        merge(A,left,mid,right);
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

        mergeSort(arr,0,n-1);

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