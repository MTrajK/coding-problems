//find the first and the second smallest number
#include<bits/stdc++.h>
using namespace std;
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

        int first=10000,second=10000;
        for(int i=0;i<n;i++)
        {
            if(a[i]<first)
            {
                first = a[i];
            }
            else if(a[i]<second)
            {
                second = a[i];
            }

        }
         cout<<first<<" "<<second<<endl;
    }
}