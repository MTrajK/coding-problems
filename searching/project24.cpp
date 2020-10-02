//you will be given an unsorted array with both positive and negative intergers as elements your job is to find the pair with maximum element

//A Simple Solution is to consider every pair and keep track maximum product. and the time complexity is O(n2)

//an efficient way to solve this is to first sort the array in ascending order then find the product of the first two element and the last two 
//element find the max of the two the time complexity of such method is O(nlogn)

//a more efficient method which includes a single traversal involves the use of 4 variables ,
//a) Maximum positive value
//b) Second maximum positive value
//c) Maximum negative value i.e., a negative value with maximum absolute value
//d) Second maximum negative value.
//the time complexity of this method is O(n).

#include<bits/stdc++.h>
using namespace std;
void product(int a[],int n)
{
    if (n < 2) 
    { 
        cout << "No pairs exists\n"; 
        return; 
    } 
  
    if (n == 2) 
    { 
        cout << arr[0] << " " << arr[1] << endl; 
        return; 
    } 
    int posa=INT_MIN,posb=INT_MIN;
    int nega=INT_MIN,negb=INT_MIN;
    for(int i=0;i<n;i++)
    {
        if(a[i]>posa)
        {
            posb=posa;
            posa=a[i];
        }
        else if(a[i]>posb)
        posb=a[i];

        if(a[i]<0 && abs(a[i])>abs(nega))
        {
            negb=nega;
            nega=a[i];
        }
        else  if(a[i]<0 && abs(a[i])>abs(negb))
        negb=a[i];
    }

    if (nega*negb > posa*posb) 
        cout << "Max product pair is {" << nega << ", "
             << negb << "}"; 
    else
        cout << "Max product pair is {" << posa << ", "
             << posb << "}"; 
}
int main()
{
    int t;cin>>t;
    while(t--)
    {
        int n;cin>>n;int a[n];
        for(int i=0;i<n;i++)cin>>a[i];
        product(a,n);
    }
    return 0;
}