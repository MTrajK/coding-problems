//Given three sorted arrays A[], B[] and C[], find 3 elements i, j and k from A, B and C respectively 
//such that max(abs(A[i] – B[j]), abs(B[j] – C[k]), abs(C[k] – A[i])) is minimized. Here abs() indicates absolute value.

//A Simple Solution is to run three nested loops to consider all triplets from A, B and C. Compute the value of 
//max(abs(A[i] – B[j]), abs(B[j] – C[k]), abs(C[k] – A[i])) for every triplet and return minimum of all values. 
//Time complexity of this solution is O(n3).

//A Better Solution is to us Binary Search.
//1) Iterate over all elements of A[],
//      a) Binary search for element just smaller than or equal to in B[] and C[], and note the difference.
//2) Repeat step 1 for B[] and C[].
//3) Return overall minimum.
// the time complexity of the given algorithm is O(nlogn)

//Efficient Solution Let ‘p’ be size of A[], ‘q’ be size of B[] and ‘r’ be size of C[]
//1)   Start with i=0, j=0 and k=0 (Three index variables for A,B and C respectively)
//  p, q and r are sizes of A[], B[] and C[] respectively.
//2)   Do following while i < p and j < q and k < r
//    a) Find min and maximum of A[i], B[j] and C[k]
//    b) Compute diff = max(X, Y, Z) - min(A[i], B[j], C[k]).
//    c) If new result is less than current result, change 
//       it to the new result.
//    d) Increment the pointer of the array which contains 
//       the minimum.


// C++ program to find 3 elements such that max(abs(A[i]-B[j]), abs(B[j]- 
// C[k]), abs(C[k]-A[i])) is minimized. 
  
#include<bits/stdc++.h> 
using namespace std; 
  
void findClosest(int A[], int B[], int C[], int p, int q, int r) 
{ 
  
    int diff = INT_MAX;  // Initialize min diff 
  
    // Initialize result 
    int res_i =0, res_j = 0, res_k = 0; 
  
    // Traverse arrays 
    int i=0,j=0,k=0; 
    while (i < p && j < q && k < r) 
    { 
        // Find minimum and maximum of current three elements 
        int minimum = min(A[i], min(B[j], C[k])); 
        int maximum = max(A[i], max(B[j], C[k])); 
  
        // Update result if current diff is less than the min 
        // diff so far 
        if (maximum-minimum < diff) 
        { 
             res_i = i, res_j = j, res_k = k; 
             diff = maximum - minimum; 
        } 
  
        // We can't get less than 0 as values are absolute 
        if (diff == 0) break; 
  
        // Increment index of array with smallest value 
        if (A[i] == minimum) i++; 
        else if (B[j] == minimum) j++; 
        else k++; 
    } 
  
    // Print result 
    cout << A[res_i] << " " << B[res_j] << " " << C[res_k]; 
} 
  
// Driver program 
int main() 
{ 
    int A[] = {1, 4, 10}; 
    int B[] = {2, 15, 20}; 
    int C[] = {10, 12}; 
  
    int p = sizeof A / sizeof A[0]; 
    int q = sizeof B / sizeof B[0]; 
    int r = sizeof C / sizeof C[0]; 
  
    findClosest(A, B, C, p, q, r); 
    return 0; 
} 