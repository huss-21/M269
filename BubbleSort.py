def bubbleSort(list):    # A Bubble Sort function , will execute upon calling
    n = len(list)


    for i in range(n):                   # This loop traverses through all the elements within the list 
        for j in range (0, n-i-1):
            if list[j] > list[j + 1]:
                list[j], list[j+1] = list[j+1], list[j]  # Swaps the element to the right if it is greater than the next element 


# Example:
n = int(input("Enter the number of items")) # In this example , the array elements will be a user input
Array = [] # init an empty array

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    Array.append(element) # Append the element to the array

bubbleSort(Array) # calling the Bubble Sort function 

print("The sorted array is , " , Array)