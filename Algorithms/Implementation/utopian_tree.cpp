// Author : Rajanikant Tenguria

#include <iostream>
using namespace std;

int main() 
{
    int T,N,i;
    cin>>T;
    while(T--)
    {
        cin>>N;
        long long int s = 1;
        for(i=1 ; i<=N ; i++)
        {
                if(i%2 == 0)
                      s++;
                else
                     s = 2*s;
        }
        cout<<s<<endl;
    }
    //cout << height << endl;
    return 0;
}
