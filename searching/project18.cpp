//Given a sorted array and a number x, find a pair in array whose sum is closest to x

//A simple solution is to consider every pair and keep track of closest pair 
//(absolute difference between pair sum and x is minimum). Finally print the 
//closest pair. Time complexity of this solution is O(n2)

//An efficient solution can find the pair in O(n) time. The idea is similar to 
//method 2 of this post. Following is detailed algorithm.

//1) Initialize a variable diff as infinite (Diff is used to store the 
//   difference between pair and x).  We need to find the minimum diff.
//2) Initialize two index variables l and r in the given sorted array.
//       (a) Initialize first to the leftmost index:  l = 0
//       (b) Initialize second  the rightmost index:  r = n-1
//3) Loop while l < r.
//       (a) If  abs(arr[l] + arr[r] - sum) < diff  then 
//           update diff and result 
//       (b) Else if(arr[l] + arr[r] <  sum )  then l++
//       (c) Else r--    
#include<iostream>
using namespace std;
void closest(int a[],int n,int x)
{
    int l=0,r=n-1,c=0,b=0;
    int diff=10000;
    while(l<r)
    {
        if(abs(a[l]+a[r]-x)<diff)
        {
            c=l;b=r;
            diff=abs(a[l]+a[r]-x);
        }
        if((a[l]+a[r])>x)r--;
        else l++;       
    }
    cout<<"the closest pair is "<<a[c]<<" "<<a[b];
}
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n,x;cin>>n>>x;int a[n];
        for(int i=0;i<n;i++)cin>>a[i];
        closest(a,n,x);
    }
    return 0;
}