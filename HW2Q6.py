def tripleMergeSort(alist):  # A recursive function that breaks lists into 3 elements then sorts them
    global comparison # Made global so it is not redefined at zero everytime the loop is run
    print("Splitting ", alist)
    if len(alist) < 2:
        return 0 # No Comparisons needed because 1 item is a sorted list also breaks loop to prevent infinite recursion

    third = len(alist) // 3

    leftThird = alist[:third]  # Separates the larger list into three smaller lists that will be sorted
    middleThird = alist[third:(2*third)]
    rightThird = alist[(2*third):]

    tripleMergeSort(leftThird)  # sort each part of the separated list recursively
    tripleMergeSort(middleThird)
    tripleMergeSort(rightThird)

    indexL = 0 # position in left third of list is initialized at 0
    indexM = 0 # position in middle third of list is initialized at 0
    indexR = 0 # position in right third of list is initialized at 0
    pos = 0 # initializes position in "alist" at 0

    while indexL < len(leftThird) and indexM < len(middleThird) and indexR < len(rightThird):
        if leftThird[indexL] > rightThird[indexR]:
            if leftThird[indexL] > middleThird[indexM]:
                alist[pos] = leftThird[indexL]
                indexL += 1
            else:
                alist[pos] = middleThird[indexM]
                indexM += 1
            comparison += 2 # Counts up two due to embedded conditional
        else:
            if rightThird[indexR] > middleThird[indexM]:
                alist[pos] = rightThird[indexR]
                indexR += 1
            else:
                alist[pos] = middleThird[indexM]
                indexM += 1
            comparison += 2 # Counts up two because of embedded conditional
        pos += 1

    while indexL < len(leftThird) and indexM < len(middleThird):
        if leftThird[indexL] > middleThird[indexM]:
            alist[pos] = leftThird[indexL]
            indexL += 1
        else:
            alist[pos] = middleThird[indexM]
            indexM += 1
        pos += 1
        comparison += 1

    while indexL < len(leftThird) and indexR < len(rightThird):
        if leftThird[indexL] > rightThird[indexR]:
            alist[pos] = leftThird[indexL]
            indexL += 1
        else:
            alist[pos] = rightThird[indexR]
            indexR += 1
        pos += 1
        comparison += 1

    while indexM < len(middleThird) and indexR < len(rightThird):
        if middleThird[indexM] > rightThird[indexR]:
            alist[pos] = middleThird[indexM]
            indexM += 1
        else:
            alist[pos] = rightThird[indexR]
            indexR += 1
        pos += 1
        comparison += 1

    while indexL < len(leftThird):
        alist[pos] = leftThird[indexL]
        indexL += 1
        pos += 1

    while indexM < len(middleThird):
        alist[pos] = middleThird[indexM]
        indexM += 1
        pos += 1

    while indexR < len(rightThird):
        alist[pos] = rightThird[indexR]
        indexR += 1
        pos += 1
    print("Merging ", alist)
    return comparison

comparison = 0
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
comps = tripleMergeSort(alist)
print("Sorted list: ", alist)  # Print the sorted list
print("Number of comparisons: ", comps) # Print the number of comparisons