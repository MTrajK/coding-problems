//minimum time trquired to produce m items 
//Consider n machines which produce same type of items but at different rate i.e., machine 1 takes a1 sec to produce an item, 
//machine 2 takes a2 sec to produce an item. Given an array which contains the time required by ith machine to produce an item. 
//Considering all machine are working simultaneously, the task is to find minimum time required to produce m items.

//method 1: Brute force
//initialize time=0 and increment it by 1. calculate number of item produce st each time until the no of produced item is not equal 
// A better method which would optimize the above solution is by applying the binary seach as the the maximum possible time requied to
//produce m items will be maximum time in the array , amax*m . So,use binary seach bw 1 to amax*m and find the minimum time which produce m items

#include<iostream>
using namespace std;
int find(int a[],int n,int temp)
{
    int time=0;
    for(int i=0;i<n;i++)time += (temp/a[i]);
    return time;
}
int bs(int a[],int n,int m,int high)
{
    int low=1;
    while (low<high)
    {
        int mid=(low+high)/2;
        //calculate the no of items made in mid sec
        int items=find(a,n,mid);
        //if the items made are less than m then increase low to mid+1
        if(items<m)low=mid+1;
        else
        {
            high=mid;
        }
    }
    return high;
}
//return the minimum time required to produce m items with given machine
int mtime(int a[],int n,int m)
{
    int maxval=-100;
    //finding the maximum time in the array
    for(int i=0;i<n;i++)
    maxval=max(a[i],maxval);

    return bs(a,n,m,maxval*m);
}
int mintime(int a[],int n,int m)
{
    int t=0;
    while(1)
    {
        int items=0;
        for(int i=0;i<n;i++)items += (t/a[i]);

        if(items==m)return t;

        t++;
    }
}
int main()
{
    int a[]={1,2,3};
    cout<<mintime(a,3,11)<<endl;
    cout<<mtime(a,3,11)<<endl;
    return 0;
}
