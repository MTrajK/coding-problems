//given an array of integers which is initially inceasing and then 
//decreasing find the maximum value in the array

//one method to solve this is linear search time complexity
//will be O(n)

//we can apply binary search too by modifying it a little bit
//if the mid is greater than both of t adjacent element then
//this is the max element
//if mid element is greater than its next element but is smaller
//than its previous element so the max lies on the left side of 
//the mid
//if mid element is smaller than its next element and greater
// than the previous element then maximum lies on right side 
//of mid.

//the third and probably the most easiest method is to use the stl
//sort on the array and find the last element time complexity
//of this method will also be O(logn) 
#include<iostream>
using namespace std;
int max(int a[],int l,int h)
{
    if(l==h)
    return a[l];

    if((h==l+1) && a[l]>=a[h])return a[l];

    if((h==l+1) && a[h]>=a[l])return a[h];

    int mid=(l+h)/2;

    if(a[mid]>a[mid+1] && a[mid]>a[mid-1])return a[mid];

    else if(a[mid]>a[mid+1] && a[mid]<a[mid-1])return max(a,l,mid-1);

    else return max(a,mid+1,h);
}

int main()
{
    int t;cin>>t;
    while(t--)
    {
        int n;cin>>n;
        int a[n];
        for(int i=0;i<n;i++)
        {
            cin>>a[i];
        }
        cout<<max(a,0,n-1)<<endl;
    }
}
