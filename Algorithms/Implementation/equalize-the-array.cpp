// Author : Rajanikant Tenguria

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<map>
using namespace std;

int main() {int n,max=0,q;
    cin>>n;
    map<int,int>m; 
    for(int i=0;i<n;i++){
        cin>>q;
        m[q]++;
        if(m[q]>max)
            max=m[q];
    }
    cout<<n-max;
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}
