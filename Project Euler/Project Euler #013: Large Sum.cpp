#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    double sum=0,n,i=10,q,x,r,s,t,u;
    long int c,d;
    cin>>n;
    q=pow(10,40);
    r=pow(10,41);
    s=pow(10,42);
    t=pow(10,51)-1;
    u=pow(10,52)-1;
    while(n--)
        {
        cin>>x;
        sum=sum+x;
    }
    if(sum<=t)
    {
    sum=sum/q;
    c=sum/10;
    }
    else if(sum<=u)
        {
    sum=sum/r;
    c=sum/10;
    }
    else
        {
    sum=sum/s;
    c=sum/10;
    }
    //sum=int(sum);
    cout<<c;
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}
