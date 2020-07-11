// Author : Rajanikant Tenguria

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    string x;
    cin>>x;
    if (x[8]=='A'){
        int y=int(x[0])-48;
        int a=int(x[1])-48;
        int b=10*y+a;
        if(b>11){
            cout<<b-12;
            cout<<"0";
            for (int i=2;i<8;i++){
                cout<<x[i];
            }
        }
        else{
            for (int i=0;i<8;i++){
                cout<<x[i];
            }
        }        
    }
    else{        
        int y=int(x[0])-48;
        int a=int(x[1])-48;
        int b=10*y+a;
        if(b==12){
            for (int i=0;i<8;i++){
                cout<<x[i];
            }
        }
        else{
            cout<<b+12;
            for (int i=2;i<8;i++){
                cout<<x[i];
            }
        }        
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}
