#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    long int n,a,b,i,p,x;
    cin>>n>>a>>b;
    cout<<1<<endl;
    if(a==3 && b==5)
        {
        for(i=2;i<=sqrt(n);i++)
            {
            p=(i*(i*3-1))/2;
            x=sqrt(2*p);
            //cout<<i<<" "<<x<<" "<<p<<endl;
            if((x*(x+1))==(p*2))
                {
                cout<<p<<endl;
            }
        }
    }
    else if(a==5 && b==6)
        {
        for(i=2;i<=sqrt(n);i++)
            {
            p=(i*(i*3-1))/2;
            x=sqrt(2*p);
            //cout<<i<<" "<<x<<" "<<p<<endl;
            if(((x*(x+1))==(p*2)) && x%2!=0)
                {
                cout<<p<<endl;
            }
        }
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}
