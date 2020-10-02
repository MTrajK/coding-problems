//in this problem you will be given an array of size n-1
// and the elements of the array will be from 1 to n but there will be 
//one element missing so you have to find that element
//without using xor operation

//though if you use xor operation what you will do is that 
//xor all the numbers from 1 to n and let it be a
//then xor all the elements in the array let it be b
//then when you xor a and b you will get the missing number

//there is one another option to solve this kind of problem
//the method is using n*(n+1)/2 formula to find the sum of all the numbers from 1 to n
// then find the sum of the elements in the number 
//then subtract the both the sums to obtain the missing number
#include<iostream>
using namespace std;
int missing(int a[],int n)
{
    int i,total=1;
    for(i=2;i<=(n);i++)
    {
        total+=i;
        total-=a[i-2];
    }
    return total;
}
int main()
{
    int t;cin>>t;
    while(t--)
    {
        int n;cin>>n;
        int x,max=0;
        int a[n-1];
        for(int i=0;i<n-1;i++)
        {
            cin>>a[i];
        }
        cout<<missing(a,n)<<endl;
    }
}