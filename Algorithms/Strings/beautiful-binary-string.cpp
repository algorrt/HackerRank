// Author : Rajanikant Tenguria

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int m , count = 0 ;
    string s;
    cin >> m >> s;
    int i = 0 ;
    while (i < m)
    {   
        //cout<<i<<" ";
        if (s[i] == '0' && s[i+1] == '1' && s[i+2] == '0')
        {
            count += 1;
            i += 3;                
        }
        else
        {
            i += 1;
        }
    }
    cout << count;
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}
