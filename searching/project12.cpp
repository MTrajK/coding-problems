//you will be given an unsorted array your job is to find the peek element in the array
//peek element is that array which is larger than its neighbour

//naive aproach to this problem is to normally traverse the array
//if the first element is greater than the second element and similarly the last element
//is greater than the second last number print those numbers and terminate
//else if the above condition is not specified then travers the whole array from 
//second element to the second last element and keep checking if the element is greater
//than its neighbour
//time complexity of that method is O(n)

//other method is a diviude and conquer method , it is a very wonderful method
//in this method we will basically apply binary search and first we will check if the 
//middle element is the peek element or not ,if yes then print the middle element and terminate
//if not then check if the element to the right of the middle element is larger then the peek 
//exists on the right side then apply the binary search on the right sub array and find for the peek element
//however if the left element is also larger than the middle element then the peek exists on the left sub array too
//repeat the above mentioned steps and find the peek
//this will reduce the time complexity to O(logn)


#include<bits/stdc++.h>
using namespace std;
void peek(int a[],int n)
{
    if(a[0]>a[1])
    {
        cout<<a[0];
        return;
    }
    else if(a[n-1]>a[n-2])
    {
        cout<<a[n-1];
        return;
    }
    else
    {
        for(int i=1;i<n-1;i++)
        {
            if(a[i]>a[i-1] && a[i]>a[i+1])
            {
                cout<<a[i];
                return;
            }
        }
    }
    cout<<"no peek found"<<endl;
    return;
}
void peek2(int a[],int l,int h,int n)
{
    if(l>h)
    {
        cout<<"no peek found"<<endl;
        return;
    }
    int mid=(l+h)/2;
    if((mid == 0 || a[mid]>a[mid-1]) && (mid==n-1 || a[mid]>a[mid+1]))
    {
        cout<<a[mid]<<endl;
        return;
    }
    else if(mid>0 && a[mid]<a[mid-1])
    {
        return peek2(a,l,mid-1,n);
    }
    else
    {
        return peek2(a,mid+1,h,n);
    }
    cout<<"no peek exists"<<endl;
    return;
    
}
int main()
{
    int t;
    cin>>t;
    while (t--)
    {
        int n;cin>>n;int a[n];
        for(int i=0;i<n;i++)cin>>a[i];
        peek(a,n);
        peek2(a,0,n-1,n);
    }
    return 0;    
}