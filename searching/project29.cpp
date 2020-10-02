//check if reversing a subarray makes the array sorted 
//there are three methods to solve this problem
//method 1: simple solution
// a simple solution is to consider every sub array one by one . try reversing 
//every subarray and check if the resersed subarray makes the whole array sorted.
//if yes return true else return false
//the time complexoty of this method is O(n2)

//method 2: the idea is to compare the given array with the sorted array .
//make a copy of the given array and sort it. now, find the first index and last index which do not
//match with the sorted array.if no such indeces are found return true this means thae array is alreasy sorted 
//else check if the elememts present bw the two indices are in strictly decreasing order , if yes print yes
//the time complexity of this method is O(nlogn)

//method 3: answer will be yes when the array is sorted or when the array has three parts.
//first part us increasing subarray ,then decreasing subarray and then increasing subarray.so, we need to check that array
//contains increasing element then some decreasing elements and then some inceasing element ,in all other cases the answer will be mo
//the time complexity of this method will be O(n)

#include<bits/stdc++.h>
using namespace std;
bool comp(int a[],int n)
{
    if(n==1)
    return true;
    int i;
    //find the first increasing part
    for(i=1;i<n && a[i-1]<a[i];i++);

    if(i==n)return true;

    //find the drcreasing part of the array

    int j=i;
    while(j<n && a[j]<a[j-1])
    {
        if(i>1 && a[j]<a[i-2])
        return false;
        
        j++;
    }
    if(j==n) return true;

    int k=j;
    if(a[k]<a[i-1]) return false;

    while(k>1 && k<n)
    {
        if(a[k]<a[k-1])
        return false;
        k++;
    }
    return true;
}
bool compare(int a[],int n)
{
    int temp[n];
    for(int i=0;i<n;i++)
    temp[i]=a[i];

    sort(temp,temp+n);
     int first,last;
    for(int i=0;i<n;i++)
    {
        if(temp[i]!=a[i]){first=i;break;}
    }
    for(int i=n-1;i>=0;i--)
    {
        if(temp[i]!=a[i])
        {
            last=i;
            break;
        }
    }
    if(first>=last)return true;
    do
    {
        if(a[first]<a[first+1])return false;

        first++;
    } while (first!=last);
    return true;
}
int main()
{int a[] = {1, 3, 4, 10, 9, 8 }; 
    int n = sizeof(a)/sizeof(a[0]); 
  
    compare(a, n)? (cout << "Yes" << endl):(cout << "No" << endl); 
    comp(a, n)? (cout << "Yes" << endl):(cout << "No" << endl); 

    return 0;

}