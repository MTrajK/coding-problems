//find the maximum and the minimum in the array with minimum number of searches

//first method would be to create a  class with two ints in it one would be min and the other would be max
//what this would do is that it will get us the results in only one linear search through out the array
//however we can also apply two binary searches for both min and max simultaneously this will reduce the time complexity from 
//n to logn
//regarding the binary search on the array 
//what basically you need to do is that divide the array in to two arrays according to the principle of binary search
//i.e mid=(beg+end)/2
//then after dividing the given array in to two array apply binary search on both the arrays recursively and compare the 
//output from both the array recursively this will ultimately get us the the overall max and minimum element
//this will also reduce the time complexity from n to logn


#include<iostream>
using namespace std;
class pair{
    public:
    int min=10000;
    int max=0;
    pair get(int a)
}
 pair get(int a[],int n)
{
     pair minmax;
    minmax.max=0;
    minmax.min=1000;
    for(int i=0;i<n;i++)
    {
        if(minmax.max<a[i])minmax.max=a[i];

        if(minmax.min>a[i])minmax.min=a[i];
    }
    return minmax;
}
int main()
{
    int t;cin>>t;
    while(t--)
    {
        int n;cin>>n;
        int a[n];
         pair p;
        for(int i=0;i<n;i++)
        {
            cin>>a[i];
        }
        p=get(a,n);
        
        cout<<p.max<<"\n"<<p.min<<"\n";
    }
}