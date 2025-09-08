# You have been given an array of positive integers A1,A2,...,An with length N and you 
# have to print an array of same length(N) where the values in the new array are the sum of 
# every number in the array, except the number at that index. Write program in Python 
# Language. Write a C++ Program 

n=int(input("Enter the Size of an Array:- "))
arr = []
for i in range(n):
    a = int(input(f"Enter the Element {i+1}:-"))
    arr.append(a)


sum = 0
for i in range(n):
    sum += arr[i]

new_arr=[]
for i in range(n):
    new_arr.append(sum-arr[i])

print(f"The new Array is:- {new_arr}")