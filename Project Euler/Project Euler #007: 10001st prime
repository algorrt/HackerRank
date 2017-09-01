// Author : Rajanikant Tenguria

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    long int n , m , mx = 0 ;
    long int num;
    vector <long int> v; 
    cin >> n;
    while (n--)
    {
        cin >> m;
        mx = max(mx,m);
        v.push_back(m);
    }    
    mx = mx * mx ;
    vector<long int> prime {2};
    for (long int i = 3 ; i < 105000 ; i = i+2)
    {
        int cnt = 1;
        for (long int j = 2 ; j < int(sqrt(i))+1 ; j++)
        {
            if (i % j == 0)
            {
                cnt = 0;
                break;
            }
        }
        if (cnt == 1)
        {
            prime.push_back(i);
        }
    }
    for (long int i = 0 ; i < v.size() ; i++)
    {
        cout << prime[v[i]-1] << endl;
    }/*
    for (long int i = 0 ; i < prime.size() ; i++)
    {
        cout << prime[i] << " ";
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}
