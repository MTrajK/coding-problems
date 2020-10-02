//you will be given a sorted aay and your job is to find the k closest elements to a given element

//the optimal way to do is to apply binary search to find the corssover point and once you ind the corssover point
//then you can simply print the closest element on each side of the element one by one
//THE TIME COMPLEITY OF THIS METHOD WILL ME O(LOGN+K)

#include<bits/stdc++.h>
using namespace std;
int binary(int a[],int l,int h,int x)
{
    if(l>h)
    {
        return -1;
    }
    if(l==h)return l;

    int mid=(l+h)/2;
    if(a[mid]==x)return mid;
    else if (a[mid]<x)
    {
        return binary(a,mid+1,h,x);
    }
    else
    {
        return binary(a,l,mid-1,x);
    }
}
void find(int a[],int l,int h,int x,int k)
{
    int p=binary(a,l,h,x);//to find the index of the crossover 
    int r=p+1;
    p--;//to get the index of the element before the crossover element
    int count=0;
    while (p>=l && r<h && count<k) 
    {
        if (x - a[p] < a[r] - x) 
            cout<<a[p--]<<endl; 
        else
            cout<<a[r++]<<endl; 
        count++; 
    }
    // If there are no more elements on right side, then 
    // print left elements 
    while (count < k && p >= l) 
        cout<<a[p--]<<endl, count++; 
  
    // If there are no more elements on left side, then 
    // print right elements 
    while (count < k && r < h) 
        cout<<a[r++]<<endl, count++; 
    
}

int main(){
    int t;cin>>t;
    while(t--)
    {
        int n;cin>>n;int a[n];
        for(int i=0;i<n;i++)cin>>a[i];
        int k,x;cin>>k>>x;
        find(a,0,n-1,x,k);
    }
    return 0;

}