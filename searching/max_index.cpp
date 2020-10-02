//you will be given an array you have to find the difference bw two index of the numbers such that a[i]<=a[j]
//https://practice.geeksforgeeks.org/problems/maximum-index/0
#include<bits/stdc++.h>
#include<vector>
#include<iostream>
using namespace std;
int main()
{
    int t;cin>>t;
    while(t--)
    {
        int n;cin>>n;
        int a[n];
        for(int i=0;i<n;i++)cin>>a[i];

        vector <int> s;

        for(int i=0;i<n;i++)
        {
            int j=i+1;
            int k=0;
            while(a[i]<=a[j])
            { 
               k++;
               j++;
            }
             s.push_back(k);
        }
        int m=s.size();
        int max=0;
        for(int i=0;i<m;i++)
        {
            if(max<=s.at(i))
            max=s.at(i);
        }
        cout<<endl<<max+1<<endl;
    }
    return 0;
}