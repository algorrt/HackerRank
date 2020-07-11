#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() 
{
    long long int n,sum,i,n1,n2,n3,s1,s2,s3,s;
    cin>>n;
    while(n--)
    {
        long long int j=0;
        cin>>j;
        n1=(j-1)/3;
        n2=(j-1)/5;
        n3=(j-1)/15;
        s1=n1*(6+(n1-1)*3);
        s2=n2*(10+(n2-1)*5);
        s3=n3*(30+(n3-1)*15);
        s=(s1+s2-s3)/2;
        cout<<s<<endl;
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}
