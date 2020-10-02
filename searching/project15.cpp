//Search in an almost sorted array
//Given an array which is sorted, but after sorting some elements are moved to either of the 
//adjacent positions, i.e., arr[i] may be present at arr[i+1] or arr[i-1]. Write an efficient 
//function to search an element in this array. Basically the element arr[i] can only be swapped 
//with either arr[i+1] or arr[i-1].

//The idea is to compare the key with middle 3 elements, if present then return the index. 
//If not present, then compare the key with middle element to decide whether to go in left half 
//or right half. Comparing with middle element is enough as all the elements after mid+2 must be 
//greater than element mid and all elements before mid-2 must be smaller than mid element.

#include<bits/stdc++.h>
using namespace std;
int binary(int a[],int l,int h,int x)
{
    if(l>h)return -1;

    if(l==h)
    {
        if(a[l]==x)
        return l;
        else
        {
            return -1;
        }
    }
    int mid=(l+h)/2;
    if(a[mid]==x)return mid;
    else if(a[mid-1]==x)return mid-1;
    else if(a[mid+1]==x)return mid+1;
    else if (x>a[mid])return binary(a,mid+2,h,x);
    else return binary(a,l,mid-2,x);
}    
int main()
{
    int t;cin>>t;
    while (t--)
    {
        int n;cin>>n;int a[n];
        for(int i=0;i<n;i++)cin>>a[i];
        int x;cin>>x;
        int k=binary(a,0,n-1,x);
        if(k=!-1)
        cout<<a[k]<<endl;
        else
        {
            cout<<"not present"<<endl;
        }
    }
    return 0;
}
