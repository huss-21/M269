def selectionSort (aList):
    for fillslot in range (len(aList)-1,0,-1):
        positionOfMax = 0
        for location in range (1, fillslot + 1):
            if aList [location] > aList[positionOfMax]:
                positionOfMax = location
#               list = [2,32,21,65,49]
        temp = aList[fillslot]
        aList [fillslot] = aList [positionOfMax]
        aList [positionOfMax] = temp
#-------------------------------------------------------------------

n = int(input("Enter the number of items"))
Array = []
for i in range (n):
    element = int(input(f"Enter element {i+1}: "))
    Array.append(element) 


selectionSort(Array)
print(Array)

