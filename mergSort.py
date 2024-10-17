def mergeSort(aList):
    if len(aList) > 1:
        mid = len(aList) // 2
        leftHalf = aList[:mid]
        rightHalf = aList[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)

        i = j = k = 0

        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                aList[k] = leftHalf[i]
                i += 1
            else:
                aList[k] = rightHalf[j]
                j += 1
            k += 1

        while i < len(leftHalf):
            aList[k] = leftHalf[i]
            i += 1
            k += 1

        while j < len(rightHalf):
            aList[k] = rightHalf[j]
            j += 1
            k += 1
#---------------------------------------------------------------------

n = int(input("Enter the number of elements  "))
Array = []
for i in range (n):
    element = int(input(f"Enter element {i+1}: "))
    Array.append(element)
mergeSort(Array)
print("Your sorted list is:" , Array)
