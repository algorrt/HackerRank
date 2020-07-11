/*

Author : Rajanikant Tenguria
Language : C++14

Problem 049 : https://www.hackerrank.com/challenges/chocolate-feast

Little Bobby loves chocolate, and he frequently goes to his favorite 5&10 store, Penny Auntie, with n dollars to buy chocolates. 
Each chocolate has a flat cost of c dollars, and the store has a promotion where they allow you to trade in m chocolate wrappers 
in exchange for free piece of chocolate.

For example, if m=2 and Bobby has n=4 dollars that he uses to buy 4 chocolates at c=1 dollar apiece, he can trade in the 4 wrappers to buy 
2 more chocolates. Now he has more 2 wrappers that he can trade in for 1 more chocolate. Because he only has 1 wrapper left at this 
point and 1<m, he was only able to eat a total of 7 pieces of chocolate.

Given n,c ,m and t for trips to the store, can you determine how many chocolates Bobby eats during each trip?

*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int t,n,c,m,x;
    cin>>t;
    while(t--){
        cin>>n>>c>>m;
        int answer=n/c;                           // Computer answer
        x=n/c;                                    // Duplicate value
        while(x>=m)                               // x should be less than m as it is minimum number of chocolates that can be exchanged
            {
            answer=answer+x/m;                    // Increase total number of chocolate by exchanging wrappers
            x=x/m+x%m;            
        }
        cout<<answer<<endl;
    }
    return 0;
}    
