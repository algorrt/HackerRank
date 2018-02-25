#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n, nw;
    cin >> n;
    vector <int> a(101);
    for (int x = 0; x < n; x++)
    {
        cin >> nw;
        a[nw] = a[nw]^1;
    }
    /*for (int x = 0; x < 101; x++)
    {
        //cout << x << " " << a[x] << endl;
        a[x] = a[x] % 2;
        //cout << x << " " << a[x] << endl;
    }*/
    for (int x = 0; x < 101; x++)
    {
        if (a[x] == 1)
        {
            cout << x;
            break;
        }
    }
    return 0;
}
