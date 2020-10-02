//find the missing number in the array using xor operator
#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;cin>>t;
    while(t--)
    {
        int n;cin>>n;
        int m=(2*n)+2;
        int a[m];
        for(int i=0;i<m;i++)
        cin>>a[i];

        int x=0;
        for(int i=0;i<m;i++)
        x=x^a[i];

       
      
        int k=x & ~(x-1);
         
        int p=0,q=0;
        for(int i=0;i<m;i++)
        {
           
            if(a[i]&k)           // 1 1 2 2 3 3 4 5 5 6 7 7 
            {
                
                 p=p^a[i];
                
            }
            else
            {
                q=q^a[i];
               
            }
        }
        if(p>q)
        {
            cout<<p<<" "<<q<<endl;
        }
        else
        {
           cout<<q<<" "<<p<<endl;
        }
        
    }
}