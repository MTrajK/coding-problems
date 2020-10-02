//median of two arrays
#include<iostream>
using namespace std;


int max(int x,int y)
{
    if(x>=y)
    {
        return x;
    }
    else
    {
        return y;
    }
    
}
int min(int x,int y)
{
    if(x>=y)
    {
        return y;
    }
    else
    {
        return x;
    }
    
}
void median(int a[],int b[],int x,int y)
{
    //let x<y
   int s=0,e=x-1;
   double median=0;
   int p;
   int i;
   int j;
    while(s<=e)
    {
         i=(s+e)/2;
         j=((x+y+1)/2)-i;
        if(a[i-1]<=b[j] && b[j-1]<=a[i]) 
        {
            cout<<"everything cool"<<endl;
            if((x+y)%2==0)
            {
              median=((double)max(a[i-1],b[j-1])+(double)min(a[i],b[j]))/2;
            }
            else
            {
                median=(double)max(a[i-1],b[j-1]);
            }
            cout<<median<<endl;
            break;
        }
        else if(a[i-1]>b[j] && b[j-1]<=a[i])
        {
            cout<<"move towards left in x"<<endl;
            e=i-1;
        }
        else 
        {
            cout<<"moves towards right in x"<<endl;
            s=i+1;
        }
    }
    
    if(s>x-1)
    {
        i=s;
        j=j-1;
        a[i]=10000;
        if((x+y)%2==0)
        {
              median=((double)max(a[i-1],b[j-1])+(double)min(a[i],b[j]))/2;
              cout<<median<<endl;
        }
        else
        {
            median=max(a[i-1],b[j-1]);
            cout<<median<<endl;
        }
        
    }
    else if(e<s && e<0)
    {
       int q=-1;
        if((x+y)%2==0)
        {
            median=((double)max(q,b[j-1])+(double)min(a[i],b[j]))/2;
        }
        else
        {
            median=(double)max(q,b[i-1]);
        }
        cout<<median;
        
    }
}

int main()
{
    int t;cin>>t;
    while(t--)
    {
        int x,y;
        cout<<"enter x"<<endl;
        cin>>x;
        cout<<"enter y"<<endl;
        cin>>y;
        int a[x],b[y];
        cout<<"enter the elements of first array"<<endl;
        for(int i=0;i<x;i++)
        cin>>a[i];
        cout<<"enter the elements of the second array"<<endl;

        for(int i=0;i<y;i++)
        cin>>b[i];
      
     median(a,b,x,y);   
    }
}
