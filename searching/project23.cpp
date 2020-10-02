//Given an array of integers, find the nearest smaller number for every element such that the smaller element is on left side.
//Examples:
//Input:  arr[] = {1, 6, 4, 10, 2, 5}
//Output:         {_, 1, 1,  4, 1, 2}
//First element ('1') has no element on left side. For 6, 
//there is only one smaller element on left side '1'. 
//For 10, there are three smaller elements on left side (1,
//6 and 4), nearest among the three elements is 4.

//the basic solution this problem is to operate in two loops,
//the first loop will start from the second element till the last one
//while the second loop will run from one element previous to the element selected in the above loop in the reverse direction
//and as soon as a smaller element is encountered print it and break the inner loop
//however this wont be an efficient method as the time complexity of this method is O(n2)

// the effecient solution includes the use of stack what you do basically is
// you start the loop first from the first element to the last element 
// in the loop you will first run a while loop to check if the stack is not empty and if its not but if the top element is greater than the 
// current selected element in the array then pop that element
// if the stack is empty then print '_'
// else print the top and push the current element on top of the stack
// the time complexity of above method is O(n).


#include<bits/stdc++.h>
using namespace std;
void newarray(int a[],int n)
{
    stack <int> s;
    for(int i=0;i<n;i++)
    {
        while(!s.empty() && s.top()>=a[i])
        s.pop();
        
        if(s.empty())cout<<"_"<<" ";

        else cout<<s.top()<<" ";

        s.push(a[i]);
    }
}
int main()
{
    int t;cin>>t;
    while(t--)
    {
        int n;cin>>n;int a[n];
        for(int i=0;i<n;i++)cin>>a[i];
        
        newarray(a,n);
    }
    return 0;
}