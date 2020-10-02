//searching a element in an array where each adjacent element differs by 1 
//the most effecient way to do this is :
//start from the left most element
//The idea is to start comparing from the leftmost element and find the difference between current array element and x. 
//Let this difference be ‘diff’. From the given property of array, we always know that x must be at-least ‘diff’ away, 
//so instead of searching one by one, we jump ‘diff’.

// C++ program to search an element in an array where 
// difference between all elements is 1 
#include<bits/stdc++.h> 
using namespace std; 
  
// x is the element to be searched in arr[0..n-1] 
int search(int arr[], int n, int x) 
{ 
    // Traverse the given array starting from 
    // leftmost element 
    int i = 0; 
    while (i<n) 
    { 
        // If x is found at index i 
        if (arr[i] == x) 
            return i; 
  
        // Jump the difference between current 
        // array element and x 
        i = i + abs(arr[i]-x); 
    } 
  
    cout << "number is not present!"; 
    return -1; 
} 
  
// Driver program to test above function 
int main() 
{ 
    int arr[] = {8 ,7, 6, 7, 6, 5, 4, 3, 2, 3, 4, 3 }; 
    int n = sizeof(arr)/sizeof(arr[0]); 
    int x = 3; 
    cout << "Element " << x  << " is present at index "
         << search(arr,n,3); 
    return 0; 
}