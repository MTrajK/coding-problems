//check if there exist two elements in an array whose sum is equal to the sum of rest if the array
//a simple solution is to consider every pair one by ,find its sum and compare tshubsum with rest 
//of the elements, if we ind a pair which satisfies the condition then return true 
//the time complexity of this solution is O(n3)

//an effecient solution is to find the sum of all array elements . let this sum be "sum". now the 
//task reduces to finding a pair with sum equals to sum/2,another optimization is, a pair can exist
//only is the sub of the array is even because we are basically dividing the array into two parts 
//with equal sum
//1- Find the sum of whole array. Let this sum be “sum”
//2- If sum is odd, return false.
//3- Find a pair with sum equals to “sum/2” using hashing based method discussed here as method 2. If a pair is found, print it and return true.
//instead of hasing what you can also do is select each and every element and then do a binary search for sum/2-n this will be of complexity O(nlogn)
//4- If no pair exists, return false.

