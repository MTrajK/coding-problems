//Given a two integers say a and b. Find the quotient after 
//dividing a by b without using multiplication, division and 
//mod operator

//basic approach :
//keep subtracting the divisor from divided until the dividend becoes
//less than divisors.the dividend becomes the remainder and the number of
//times subtraction is done becomes the quotient .


#include<bits/stdc++.h>
using namespace std;
long long divide(long long dividend,long long divisor)
{
    long long sign=((dividend<0)^(divisor<0)) ? -1 : 1;

    dividend=abs(dividend);
    divisor=abs(divisor);

    long long quotient = 0;
    while(dividend>=divisor)
    {
        dividend -= divisor;
        ++quotient;
    }
    if(quotient>=pow(2,31))quotient--;
    return sign*quotient;
}
int main()
{
    long long a;cin>>a;
    long long b;cin>>b;
    cout<<divide(a,b);
}
