//find the ceiling and floor of a number in an array

// in the basic approach we will do a linear search for the ceiling element we will do the iteration from 0 to n-1 and 
// the minimum element which is greater than equal to the x will be the ceiling and for floor the whole process will be 
//opposite we will iterate from n-1 to 0 this solution will be of linear time complexity i.e O(n).

//other option is to follow the above concept only but instead of linear search we can apply binary search
//this will reduce the time complexity to logn 

#include<bits/stdc++.h>
using namespace std;
int floor_binary(int a[],int l,int h,int x)
{
    if(x==a[l])
    return l;
    if(x<a[0])
    {
        return -1;
    }
    if(x>=a[h])
    {
        return h;
    }
    int mid=(l+h)/2;
    if(x==mid)
    {
        return mid;
    }
    else if(x<a[mid])
    {
        if(mid-1>=l && x>=a[mid-1])
        {
        return mid-1;
        }
        else
        {
          return floor_binary(a,l,mid-1,x);
        }
    }
    else
    {
        if(mid+1<=h && x>=a[mid+1])
        return mid+1;
        else
        return floor_binary(a,mid+1,h,x);
    }
}
int ceil_binary(int a[],int l,int h,int x,int y)
{
    if(x<=a[l])
    {
        return l;
    }
    if(h==y && x>a[h])
    {
        return -1;
    }
    int mid=(l+h)/2;
    if(x==a[mid])
    return mid;
    else if(x>a[mid])
    {
        if(mid+1<=h && x<=a[mid+1])
        return mid+1;
        else
        {
          return ceil_binary(a,mid+1,h,x,y);
        }
    }
    else
    {
        if(mid-1>l && x>a[mid-1])
        return mid;
        else
        {
            return ceil_binary(a,l,mid-1,x,y);
        }
    }   
}
int main()
{
    int t;cin>>t;
    while(t--)
    {
        int n;cin>>n;
        int a[n];
        for(int i=0;i<n;i++)cin>>a[i];

        int flag=0,flag1=0;

        //int c=0;int f=0;
        
        int x;cin>>x;
        sort(a,a+n);

        //cout<<*max_element(a,a+n);
        for(int i=0;i<n;i++)
        {
            if(!flag)
            {
                if(a[i]>=x)
                {
                    cout<<"ceiling "<<a[i]<<endl;
                    flag=1;
                }
            }
            if(!flag1)
            {
                if(a[n-1-i]<=x)
                {
                    cout<<"floor "<<a[n-1-i]<<endl;
                    flag1=1;
                }
            }
        }
        if(!flag)
        {
            cout<<"ceilieng does not exit "<<endl;
        }
        if(!flag1)
        {
            cout<<"floor does not exist "<<endl;
        }
        int index=ceil_binary(a,0,n-1,x,n-1);
        if(index==-1)
        {
            cout<<"ceiling does not exists"<<endl;
        }
        else
        {
            cout<<"ceiling "<<a[index]<<endl;
        }
        int floor=floor_binary(a,0,n-1,x);
        if(floor==-1)
        {
            cout<<"floor does not exists "<<endl;
        }
        else
        {
            cout<<"floor is "<<a[floor]<<endl;
        }
    }
    return 0;
}