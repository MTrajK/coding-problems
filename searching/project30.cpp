//find all triplets with zero sum

//there are basically two methods to solve the problem

//method 1: this method takes O(n3) of time complexity
//in this method we will run three loops and in each loop we will 
//select an element and then in the last loop we will add three elements
//if the sum=0 then we've found the triplet
//the algorithm to the above method is
//run three loops with loop counter i,j,k;
//loop i starts from 0 to n-3
//loop j starts from i+1 to n-2
//loop k starts from j+1 to n-3
//check if the sum of the three selected elements sums to zero or not

//method 2: this method will take O(n2) time complexity
//in this method we will first sort the whole array
///then run a loop from i=0 to n-1 and select a element a[i];
// set two indices l=i+1 and r=n-1
//run another loop until l<r and select two elements a[l] & a[r]
//if the sum of a[l],a[i]&a[r]=0 the we've found the triplet else
//if the sum<0 then l++ else r--;

#include<bits/stdc++.h>
using namespace std;
void triplet(int a[],int n)
{
    sort(a,a+n);
    int found;
    for(int i=0;i<n;i++)
    {
        int l=i+1,r=n-1;
        while(l<r)
        {
            int sum=a[i]+a[l]+a[r];
            if(sum==0)cout<<"found "<<a[i]<<" "<<a[l]<<" "<<a[r]<<endl;

            if(sum<0)l++;
            else r--;
        }
    }
}
int main()
{
    int a[]={0, -1, 2, -3, 1};
    int n=sizeof(a)/sizeof(a[0]);
    triplet(a,n);
    return 0;
}