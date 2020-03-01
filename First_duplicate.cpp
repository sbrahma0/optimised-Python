/**
starts with 0 index, gets the element of that index then (that number-1) index element is checked whether it is -ve, if it 
is not then make it -ve else the previous index i.e., the index in the current loop is the answer
https://youtu.be/XSdr_O-XVRQ
**/

#include <iostream> 
using namespace std; 
  
// Function to print duplicates
// size has to be given as an argument since when we pass an array as an arguement, only the memory address is passed
int printRepeating(int arr[], int size) // int arr[] can be also written as *arr
{
for (int i = 0; i < size; i++) 
{ 
    //cout<<i<<endl;
    if (arr[abs(arr[i])-1] >= 0) 
    arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]; 
    else {
        cout << "The first number to appera as a duplicate is- "<<abs(arr[i]) << " ";
        return 0;
    }
} 
} 
  
// Driver Code 
int main() 
{ 
    int arr[] = {1,2,3,2,3,4,5}; 
    int arr_size = sizeof(arr)/sizeof(arr[0]); 
    printRepeating(arr, arr_size); 
    return 0; 
} 
