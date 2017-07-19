#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    long long n,m,o;
    cin>>n;
    while(n--)
        {
        long long a1,a2,i,count=0;
        cin>>a1>>a2;        
        o = sqrt(a1);
        i = sqrt(a2);
        if(o*o==a1 )
            {
            count=i-o+1;
        }
        else
            {
        count=i-o;
        }
         cout<<count<<endl;
        }
       
    
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}
