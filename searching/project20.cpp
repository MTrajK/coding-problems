//Find position of an element in a sorted array of infinite numbers
//we cannot apply binary search diectly because in such an array we dont have the bounds defined
//so the best call would be to find the bounds first and then apply the binary search 

//to find the bounds what we need to do is 
//Let low be pointing to 1st element and high pointing to 2nd element of array, Now compare key with high index element,
//->if it is greater than high index element then copy high index in low index and double the high index.
//->if it is smaller, then apply binary search on high and low indices found.
#include<bits/stdc++.h>
using namespace std;
void bounds(int a[])