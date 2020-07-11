//Author:Rajanikant Tenguria

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int main() {
      long  int num,sum,j,x;
    cin>>num;
    sum=0;
    for(j=0;j<num;j++)
        {
        cin>>x;
        sum=sum+x;       
    }
    cout<<sum;
    return 0;
}
