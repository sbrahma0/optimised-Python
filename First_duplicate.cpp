#include <iostream> 
using namespace std; 
  
// Function to print duplicates 
int printRepeating(int arr[], int size) 
{ 
int i;
for (i = 0; i < size; i++) 
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
