//binary search
#include<iostream>
using namespace std;
int main()
{
    int n,k;cin>>n>>k;
    int a[n];
    for(int i=0;i<n;i++)cin>>a[i];
    int l=0,u=n-1;
    int mid=0;
    while(l<u)
    {
        if(k==a[l] || k==a[u])
        {
            cout<<"found"<<endl;
        }
      mid=(l+u)/2;
      if(k==a[mid])
      {
          cout<<mid<<endl;
          break;
      }
      else if(k<a[mid])
      {
       u=mid-1; 
      }
      else if(k>a[mid])
      {
          l=mid+1;
      }
      else
      {
          cout<<"not found"<<endl;
      }
      
      
    }
}