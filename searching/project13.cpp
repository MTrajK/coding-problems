//Find the minimum element in a sorted and rotated array

//one method to solve this problem is by normal traversing we will select each element one by one
//and keep comparing it with every other element 
//however this would not be the desired solution because it will be of O(n^2) time complexity

//other method it to apply the binary search method , in this method we will calculate the mid element and then compare it 
//with its two neighbour if its the minimum of all three then that element is the minimum number 
//else if the mid number if smaller than the last number then the minimum is present in the left side of the mid
//else it is present on the right  side this will reduce the time complexity to O(logn)

#include<bits/stdc++.h>
using namespace std;
int minimum(int a[],int l,int h)
{
    if(l>h)
    {
        return -1;
    }
    if(l==h)
    {
        if(a[l]<a[h])
        return l;
        else
        {
            return h;
        }
        
    }
    int mid=(l+h)/2;
    if(a[mid]<a[mid-1] && a[mid]<a[mid+1])
    return mid;
    else if (a[mid]<a[mid+1] && a[mid]<a[h])
    {
        return minimum(a,l,mid-1);
    }
    else
    {
        return minimum(a,mid+1,h);
    }    
}
int main()
{
    int t;cin>>t;
    while(t--)
    {
        int n;cin>>n;int a[n];
        for(int i=0;i<n;i++)
        cin>>a[i];
        int k=minimum(a,0,n-1);
        cout<<a[k]<<endl;
    }
    return 0;
}