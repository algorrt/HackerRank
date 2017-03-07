#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() 
{
    long long int n,sum=0,a,b,x;
    cin>>n;
    while(n--)
    {
        long long int y;
        cin>>y;
        sum=2;
        a=2;
        b=0;
        x=0;
        while(x<y)
        {
            x=4*a+b;
            b=a;
            a=x;
            if(x<y)
                {
                sum=sum+x;
            }
        } 
        cout<<sum<<endl;
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}
