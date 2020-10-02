//Given an array that is sorted and then rotated around an unknown point. 
//Find if the array has a pair with a given sum ‘x’. It may be assumed that
// all elements in the array are distinct

//the basic idea behind the solution of this problem is that first we have to find 
//the pivot element which will be the largest element and the element next to the pivot element
//will be the smallest element we can find this by normal linear iteration or by doing the binary search
//as dsicussed in one of the following projects

//once you have the pivot element what you need to do then is take two pointers one pointing to the pivot element
//and the other pointing to the element next to the pivot element and then we find the sum of two elements 
//if the sum is equal to the given sum return true else decrement and increment in the rotated manner till one reaches the 
//corner end

//the time complexity of the above method is basically O(n) but we can reduce the complexit of the pivot finding step to
//O(logn) by using the binary search method

//to find the no of pairs whose sum is equal to the given key
//
#include<bits/stdc++.h>
using namespace std;
bool rotated(int arr[],int n,int x)
{
    int i; 
    for (i=0; i<n-1; i++) 
        if (arr[i] > arr[i+1]) 
            break; 
    int l = (i+1)%n;  // l is now index of smallest element 
    int r = i;        // r is now index of largest element 
  
    // Keep moving either l or r till they meet 
    while (l != r) 
    { 
         // If we find a pair with sum x, we return true 
         if (arr[l] + arr[r] == x) 
              return true; 
  
         // If current pair sum is less, move to the higher sum 
         if (arr[l] + arr[r] < x) 
              l = (l + 1)%n; 
         else  // Move to the lower sum side 
              r = (n + r - 1)%n; 
    } 
    return false;

}
int main()
{
    int t;cin>>t;
    while(t--)
    {
        int n,x;cin>>n>>x;
        int a[n];
        for(int i=0;i<n;i++)cin>>a[i];
        if(rotated(a,n,x))
        cout<<"found"<<endl;
        else
        {
            cout<<"not found"<<endl;
        }
        
    }
}