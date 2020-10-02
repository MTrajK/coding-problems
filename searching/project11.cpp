//given an unsorted array and a number n find if there
//exists a pair of element in the array whose difference is n

//the most basic approach to solve such kind of problem is that
//you will perform two loop in the first loop you will select an element
//and then in the second loop you will search for the desired element in the array
//the time complexity of this array is O(n2)

//we can improve the above method by applying binary search in the second step 
//what basically we will do is that first we will select one element a[i] from the array in the first loop
//then in the second loop we will do a binary search for a[i]+n in a[i+1.....n-1]
//if the element is found return pair
//in this the time complexity of the sorting will be O(nlogn) and binary search will also be of O(nlogn)
//so the overall timecomplexity will be O(nlogn)

//the second step of above method can be improved to O(n) the first step remain same.
// the idea for above step is to take two index variables i and j, initialise tehm as 0 and 1
//now run a linear loop , if a[j]-a[i]<n then we need a greater number therefore increment j,else increment i
//the time complexity of this algorithm overall is also O(nlogn)

#include<bits/stdc++.h>
using namespace std;
int binary(int a[],int l,int h,int x)
{
    if(h<l)
    return 0;

    if(x==a[l]) return l;

    if(x==a[h]) return h;
    
    int mid=(h+l)/2;
    if(x==a[mid])return mid;

    else if(x>a[mid]) return binary(a,mid+1,h,x);

    else return binary(a,l,mid-1,x);
}
int main()
{
    int t;cin>>t;
    while(t--)
    {
        int n,x;cin>>n>>x;
        int a[n];
        for(int i=0;i<n;i++)
        cin>>a[i];
        int k=0;
        sort(a,a+n);
        for(int i=0;i<n;i++)
        {
            k=binary(a,i+1,n-1,abs(a[i]-x));
            if(k==-1)
        {
            cout<<"not found"<<endl;
        }

            if(k!=-1)
            {
                cout<<"found "<<a[i]<<" "<<a[k]<<endl;
                break;
            }
        }
        if(k==-1)
        {
            cout<<"not found"<<endl;
        }
    }
    return 0;
}