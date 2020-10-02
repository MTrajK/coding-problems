//two elements whose sum is closest to zero

//first method to solve this kind of problem is to
//find sum of every element with every other element and compare all the element
//the store the minimum of absolute of the sum and display the corresponding numbers
//however this method is not effecient and this if of o(n^2) complexity

//another method is to first sort the array then define two variables l and s where l=0 and s=n-1
//find the sum a[l]+a[s]
//if min_sum>sum-> min_sum=sum->if sum<0->l++;else s--;

//
#include<bits/stdc++.h>
using namespace std;
void find_sort(int a[],int n)
{
    int l=0,s=n-1;
    sort(a,a+n);
    int max=100000;
    int sum=0;
    int i,j;
    while(l<=s)
    {
        sum=a[l]+a[s];
        if(abs(max)>abs(sum))
        {
            max=sum;
            i=l;
            j=s;
            if(sum<0)
            {
                l++;
            }
            else
            {
                s--;
            }
            
        }
    }
    cout<<max<<endl;
}
void find(int a[],int n)
{
    int max=a[0]+a[1];
    int l=0,s=0;
    int sum=0;
    for(int i=0;i<n-1;i++)
    {
       for(int j=i+1;j<n;j++)
       {
           sum=a[i]+a[j];
           if(abs(max)>abs(sum))
           {
               max=sum;
               l=i;
               s=j;
           }
       }
    }
    cout<<max<<endl;//" "<<a[l]<<" "<<a[s]<<endl;
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
        find(a,n);
        cout<<endl;
        find_sort(a,n);

    }
}