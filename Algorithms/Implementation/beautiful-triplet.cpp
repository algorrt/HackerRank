// Author : Rajanikant Tenguria

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n,m,mx=0,cnt=0,tmp,ar[50000];
    cin>>m>>n;
    for (int i=0;i<m;i++)
    {
        cin>>tmp;
        ar[tmp]++;
        mx=max(mx,tmp);
    }  
    for (int i=0; i<mx;i++)
    {
        if (ar[i]==1 && ar[i+n]==1 && ar[i+2*n]==1)
        {
            cnt++;
        }
    }
    cout<<cnt;
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}
