//you will be given a sorted array which will be rotated at one point 
//for example 5 6 7 8 1 3 4
// your role is to find the missing number 2 in our case
//this solution will work only in the case when all the elements of the second array 
//but yes as the array is sorted and it is pivoted at one point so before thet point all the elements woul be larger
//than all the element before that pivot 
//what i am trying to say is that
//lets say you are given a sorted array and if you pivot it at one point then all the elements following the pivot
//woul be larger than all the elements preceeding the pivot
//so once you attach the second half of the array in front of the first half of the array
//so even the minimum of the first half of array would be larger than the maximum of the second half of the array(after rotation)

// the problem arises when there is repetition of numbers
#include<iostream>
using namespace std;
int binary(int a[],int l,int u,int x)
{
    if(u>=l)
    {
        int mid=(l+u)/2;

        if(a[mid]==x)
        {
            return mid ;
        }
        else if(a[mid]>x)
        {
            return binary(a,l,mid-1,x);
        }
        else
        {
            return binary(a,mid+1,u,x);
        }
        
    }
    return -1;
}
int main()
{
    int t;cin>>t;
    while(t--)
    {
        int n,k;cin>>n>>k;
        int a[n];
        for(int i=0;i<n;i++)
        cin>>a[i];
        int i=0,j=n-1;
        while(a[i]>a[j])
        {
            i++;
            j--;
        }
        int pivot=0;
        if(a[j-1]<a[j] && a[i+1]>a[i])
        {
            pivot=j;
        }
        else if(a[j-1]<a[j] && a[i+1]<a[i])
        {
            pivot=i;
        }
        cout<<pivot<<endl;
        int q; cin >>q;
        int l1=0,u1=pivot;
        int l2=pivot+1; int u2=n-1;
        cout<<binary(a,l1,u1,k)<<endl;
        cout<<binary(a,l2,u2,k);
    }

}