# Write a C++ / python program for Linear Search and Binary Search

def bin_Search(l,num,count):
    if(len(l) == 0):
        print("The Given Number is Not Found in the list")
        return -1
    
    a = len(l) // 2
    n = num
    c=count 
    c+=1
    if(l[a] == num ):
        print(f"The Number Found at {c} steps in Binary Search ")
        return "Pass"

    elif(l[a]>num):
        new_list = l[:a]
        return bin_Search(new_list,n,c)

    elif(l[a]<num):
        new_list=l[a+1:len(l)]
        return bin_Search(new_list,n,c)

def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i  
    return -1


n=int(input("Enter the Size of an Array:- "))
l = []
for i in range(n):
    a=int(input(f"Enter the array element {i+1}:- "))
    l.append(a)


print(l)
count = 0
search_for = int(input("Enter the Which Value You want to find:- "))
bin_Search(l,search_for,count)

result = linear_search(l, search_for)
if result != -1:
    print(f"Element found at index {result} in Linear Search at the {result+1} step ")
else:
    print("Element not found in the list")


