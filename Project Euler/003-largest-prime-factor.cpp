#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


#include <iostream>
#include <cstdlib>
#include <cmath>
using namespace std; 
void get_divisors( long long int n); 
int main() 
{
    long long int n = 0,j,b;
    long long int a[j];
    cin>>b;
    while(b--)
        {
    cin >> n;
    get_divisors(n);
    cout << endl; 
    }
} 
void get_divisors( long long int n)
{
     long long int i,j;
    long long int a[j];
     double sqrt_of_n = sqrt(n);
     for (i = 2; i <= sqrt_of_n; i++)
         if (n % i == 0) 
         {
            a[j]=n; 
            get_divisors(n / i);
            return; 
                 }
     cout << n;
 }
