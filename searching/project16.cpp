//to find the union and intersection of two arrays

//to find the union of two array we will follow the following algorithm
//initialize two variables i and j to the first indexes of both the array
//if a[i] is smaller than b[j] then print a[i] and increment i
//if b[j] is smaller than a[i] then print b[j] and increment j
//if both are equal then print any one of them and increment that pointer
//if one array ends print the whole of the other array
//time complexity of this algoritm will be O(m + n)

//to find the intersection of two arrays is simple
//1) Use two index variables i and j, initial values i = 0, j = 0
//2) If arr1[i] is smaller than arr2[j] then increment i.
//3) If arr1[i] is greater than arr2[j] then increment j.
//4) If both are same then print any of them and increment both i and j.

#include<bits/stdc++.h>
using namespace std;
void inter(int a[],int b[],int n,int m)
{
    int i=0,j=0;
    while(i<n && j<m)
    {
        if(a[i]<b[j])i++;
        else if(a[i]>b[j])j++;
        else
        {
            cout<<a[i]<<endl;i++;j++;
        }
        
    }
}
void uni(int a[],int b[],int n,int m)
{
    int i=0,j=0;
    int prev1;
    while(i<n && j<m)
    {
       if(a[i]<b[j])
       {
           cout<<a[i]<<" ";
           prev1=a[i];
           while(prev1==a[i])
           {
               i++;
           }
       } 
       else if(a[i]>b[j])
       {
           cout<<b[j]<<" ";
           prev1=b[j];
           while(prev1==b[j])
           {
               j++;
           }
       }
       else
       {
           prev1=a[i];
           cout<<a[i]<<" ";i++;
           while(prev1==a[i])
           {
               i++;
           }
           while (prev1==b[j])
           {
               /* code */
               j++;
           }
           
           
       }
    }
    if(i>=n)
    {
        while(j<m)
        {
            prev1=b[j];
            cout<<b[j]<<" ";
            while (prev1==b[j])
            {
                /* code */
                j++;
            }
            
        }
    }
    if(j>=m)
    {
        while(i<n)
        {
            prev1=a[i];
            cout<<a[i]<<" ";
            while(prev1==a[i])
            {
                i++;
            }
        }
    }
}

int main()
{
    int t;cin>>t;
    while (t--)
    {
        int n,m;cin>>n>>m;
        int a[n],b[m];
        for(int i=0;i<n;i++)cin>>a[i];
        for(int i=0;i<m;i++)cin>>b[i];
        uni(a,b,n,m);
        cout<<endl;
        inter(a,b,n,m);
    }
    return 0;
}