//Given two sorted arrays and a number x, find the pair whose sum is closest to x 
//and the pair has an element from each array.
//We are given two arrays ar1[0…m-1] and ar2[0..n-1] and a number x, we need to find 
//the pair ar1[i] + ar2[j] such that absolute value of (ar1[i] + ar2[j] – x) is minimum.


//A Simple Solution is to run two loops. The outer loop considers every element of first
// array and inner loop checks for the pair in second array. We keep track of minimum 
//difference between ar1[i] + ar2[j] and x.

//We can do it in O(n) time using following steps.
//1) Merge given two arrays into an auxiliary array of size m+n using merge process of merge sort.
// While merging keep another boolean array of size m+n to indicate whether the current element in 
//merged array is from ar1[] or ar2[].
//2) Consider the merged array and use the linear time algorithm to find the pair with sum closest 
//to x. One extra thing we need to consider only those pairs which have one element from ar1[] and 
//other from ar2[], we use the boolean array for this purpose.

//Can we do it in a single pass and O(1) extra space?
//The idea is to start from left side of one array and right side of another array, and use the algorithm 
//same as step 2 of above approach. Following is detailed algorithm.

//1) Initialize a variable diff as infinite (Diff is used to store the 
//   difference between pair and x).  We need to find the minimum diff.
//2) Initialize two index variables l and r in the given sorted array.
//       (a) Initialize first to the leftmost index in ar1:  l = 0
//       (b) Initialize second  the rightmost index in ar2:  r = n-1
//3) Loop while  l = 0
//       (a) If  abs(ar1[l] + ar2[r] - sum) < diff  then 
//           update diff and result 
//       (b) If (ar1[l] + ar2[r] <  sum )  then l++
//       (c) Else r--    
//4) Print the result. 

//wont be writing the code for this problem it is very much similar to the project18.cpp code
