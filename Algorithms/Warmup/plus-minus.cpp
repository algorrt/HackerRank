// Author : Rajanikant Tenguria

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<iostream>

using namespace std;

int main()
{
    int n;
    cin>>n;
    float pl=0,mn=0,zr=0;
    for(int i=0;i<n;i++)
    {
        int val;
        cin>>val;
        if(val==0)
            zr++;
        else if(val>0)
            pl++;
        else
            mn++;
    }
    zr=zr/(float)n;
    pl=pl/(float)n;
    mn=mn/(float)n;
    printf("%0.03f\n%0.03f\n%0.03f\n",pl,mn,zr);
}
