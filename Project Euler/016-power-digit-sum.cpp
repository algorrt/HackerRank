#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

int main()
{
     long long int val,n,sum;
     cin>>n;
     while(n--)
         {
         sum=0;
     int carry=0;
     cin>>val;
     vector<int>arr(5000,0);
     arr[0]=1; //Initial product = 1



     int k=0; //Current size of the number stored in arr


     for(int i=1;i<=val;i++)
     {
        for(int j=0;j<=k;j++)
        {
            arr[j]=arr[j]*2+carry;
            carry=arr[j]/10;
            arr[j]=arr[j]%10;
        }
        while(carry)    //Propogate the remaining carry to higher order digits
        {
            k++;
            arr[k]=carry%10;
            carry/=10;
        }   
     }
     //for(int i=k;i>=0;i--)
            //cout<<arr[i];
    //cout<<endl;
         for(int i=0;i<5000;i++)
             {
             sum=sum+arr[i];
         }
         cout<<sum<<endl;
     }
    return 0;
}
