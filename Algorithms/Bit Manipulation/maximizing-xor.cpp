"""
Author    : Rajanikant Tenguria        
Language  : C++
Problem   : https://www.hackerrank.com/challenges/maximizing-xor/problem
Avg Time  : 0s
% Success : 96.62 (72540/75080)
"""

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int l, r, temp, mx = 0;
    cin >> l >> r;
    for (int i = l; i < r+1; i++)
    {
        for (int j = l+1; j < r+1; j++)
        {
            //cout<<i<<" "<<j<<endl;
            temp = i^j;
            if (temp > mx)
            {
                mx = temp;
            }
        }
    }
    cout << mx;
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}
