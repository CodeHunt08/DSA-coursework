//  You have been given an array of positive integers A1,A2,...,An with length N and you 
//  have to print an array of same length(N) where the values in the new array are the sum of 
//  every number in the array, except the number at that index. Write program in Python 
//  Language. Write a C++ Program 

#include<iostream>
using namespace std;
int main(){
    int n,sum=0;
    cout<<"Enter the Size of an Array:- "<<endl;
    cin>>n;
    int arr[n],new_arr[n];


    for(int i = 0;i<n;i++){
        cout<<"Enter the Element "<<i+1<<endl;
        cin>>arr[i];
    }

  
    for(int i =0;i<n;i++){
        sum += arr[i];

    }

    for(int i = 0;i<n;i++){ 
        new_arr[i] = sum - arr[i];
    }

    cout<<"The new Array is:- "<<endl;
    for(int i =0;i<n;i++){
        cout<<new_arr[i]<<" ";
    }
return 0;
}
