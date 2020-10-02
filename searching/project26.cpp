//print all possible consecutive numbers with sum N
//we just need to look from 1 to N/2 
//so one basic solution to this question it is that we will keep
//adding the sequence of consecutive numbers is the sum = N then
//print the sequence otherwise start with the next number
//the time complexity of such methpd is O(n2)

//if we optimize the above code , we get the time complexity in 
// the order O(n)
// the code is
#include<stdio.h>
using namespace std;
void printSums(int N) 
{ 
    int start = 1, end = 1; 
    int sum = 1; 
  
    while (start <= N/2) 
    { 
        if (sum < N) 
        { 
            end += 1; 
            sum += end; 
        } 
        else if (sum > N) 
        { 
            sum -= start; 
            start += 1; 
        } 
        else if (sum == N) 
        { 
            for (int i = start; i <= end; ++i) 
                printf("%d ", i); 
  
            printf("\n"); 
            sum -= start; 
            start += 1; 
        } 
    } 
} 
  
// Driver Code 
int main() 
{ 
    printSums(125); 
    return 0; 
} 
