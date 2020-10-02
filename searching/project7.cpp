//you would be given an array with repetitions 
//your job is to find the no of occirence of a particular number
//there are many ways to solve this

//the first method being the linear search in which you will iterate through the array and whenever you come across that 
//particular number you will increment the counter variable the time complexity of this method is O(n)

//the second method being is that you will first do a binary search to locate the given number next your job is
//to find the occurence of that number in the left hand side of the number at the located and do the similar job on the
//right hand side of the number at the located index in this way you reduce the time complexity to O(logn + count)
//where cound is the number of occurence

//the third method is the best method it is basically the improved version of the binary serach
//in this method you first find out the index of the first occurence of the the given number and the last occurence of 
//the number and then in the end you basically subtract both the indexes to get the no of occurence 

#include<bits/stdc++.h>
using namespace std;
int binary(int a[],int l,int h,int x)
{
    if(h<l)
    return -1;

    int mid=(l+h)/2;

    if(a[mid]==x)
    return mid;

    if(x>a[mid])
    return binary(a,mid+1,h,x);

    
    return binary(a,l,mid-1,x);
}
int count(int a[],int n,int x)
{
    int d=binary(a,0,n-1,x);

    if(d==-1)
    return -1;
    int count=1;
    int left=d-1;
    while(left>=0 && a[left]==x)
    count++,left--;

    int right=d+1;
    while(right<n && a[right]==x)
    count++,right++;

    return count;
}
int improved_binary(int a[],int n,int x)
{
    int *low=lower_bound(a,a+n,x);//get the index of  first occurence of x

    if(low==(a+n) && *low!=x)//if the element is not present return 0;
    return 0;

    //if the element is present then find the index of the last occurence 
    int *high=upper_bound(low,a+n,x);

    return high-low; 
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
        int x;cin>>x;

        sort(a,a+n);

        cout<<count(a,n,x)<<endl;
        cout<<improved_binary(a,n,x)<<endl;

    }
}
