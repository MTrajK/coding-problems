//Given an unsorted array of size n. Array elements are 
//in the range from 1 to n. One number from set {1, 2, …n} 
//is missing and one number occurs twice in the array. 
//Find these two numbers.

//first method is to sort the array and then traverse the array 
//and then find the missing and the repetetive number 
//time complexity will be O(nlogn).

//using the count array method the time complexity of such method
//will be O(n)

//traverse the array ,while traversing ,use the absolute value
//of every element as index and make the value at this index 
//as negative to mark if visited . if something is already negative
//then thus is the repeating element. to find the missing traverse 
//the array again and look for a positie value
//time complexity of this method will also be O(n)

//another method involves forming of two equations the first 
//one being S=n(n+1)//2-x+y
//the second one being P=1*2*3.....*n*y/x
//now you have two variables and two equation you can solve 
//them to get the missing and the repeating element
//time complexity of this method will also be O(n).

//another method involves using of xor operator and the time complexity of this method is also O(n) 
//this method involves to take xor on all the element of the array let the answer be xor1 then xor xor 1 with all the 
//no from 1 to n then after the succesfull operation the result will contain the xor of the repeated element and the 
//missing element to separate these two elements we have to separate all the elements according to the first set bit method
//for this you have to calculate the mask which is done by m= x^ ~(x-1)

#include<bits/stdc++.h>
using namespace std;
void missing3(int a[],int n)
{
    int x=0;
    for(int i=0;i<n;i++)x=x^a[i];

    for(int i=1;i<=n;i++)x=x^i;

    int m=x & ~(x-1);

    int p=0,q=0;

    for(int i=0;i<n;i++)
    {
        if(m&a[i])
        {
            p=p^a[i];
        }
        else
        {
            q=q^a[i];
        }
        
    }
    for(int i=1;i<=n;i++)
    {
        if(i & m)
        {
            p=p^i;
        }
        else
        {
            q=q^i;
        }
        
    }
    cout<<"the missing ekement is "<<p<<endl<<"the repeating element is  "<<q<<endl;
}

void missing2(int a[],int n)
{
    int s=0,p=1,s1=0,p1=1;
    for(int i=0;i<n;i++)
    {
        s=s+a[i];
        p=p*a[i];
        s1=s1+(i+1);
        p1=p1*(i+1);
        
    }
    cout<<"the missing element is "<<(((s-s1)*p1)/(p-p1))<<endl;
    cout<<"the repeating element is "<<(((s-s1)*p)/(p-p1))<<endl;

}
void missing1(int a[],int n)
{
    for(int i=0;i<n;i++)
    {
        if(a[abs(a[i])-1]>0)
        {
            a[abs(a[i])-1]=-a[abs(a[i])-1];
        }
        else
        {
            cout<<"the repeating element is"<<abs(a[i])<<endl;
        }
    }
    for(int i=0;i<n;i++)
        {
            if(a[i]>0)
            cout<<"missing element is"<<i+1<<endl;
        }
        for(int i=0;i<n;i++)
        {
            if(a[i]<0)
            {
                a[i]*=-1;
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
        for(int i=0;i<n;i++)
        {
            cin>>a[i];
        }
        missing1(a,n);
        missing2(a,n);
        missing3(a,n);
    }
    return 0;
}
