//program to find the common numbers in three sorted array

//the whole concept is based on the method to find the intersection of two sorted array
//in this method consider three pointers i,j,k :x=a[i],y=b[j],z=c[k]
//if x<y i++ else if y<z j++ else (i.e z is the smallest) k++;
//if the three numbers are equal print any of the element and increment i,j,k
//the time complexity of this method is O(n1+n2+n3)
//write the code yoursself
#include<iostream>
using namespace std;
int main()
{
    int n;cin>>n;
    return 0;
}