def selectionSort(array, reverse=False):
    """
    Detail:
    1. This sort will search for the smallest (biggest if reverse=True) element starting from the first element
    2. swap minimum (maximum if reverse=True) number with first element
    3. Take the unsorted part and repeat the step 1 and 2 until it is sorted
    > Worst Case Time Complexity is: O(N2)
    > Average Case Time Complexity is: O(N2)
    > Best Case Time Complexity is: O(N2)
    > Space Complexity: O(1)

    :param array: unsorted python list
    :type array : list
    :param reverse: If True , sorting will be done on descending order
    :type reverse : bool
    :return : Sorted array in ascending order (or  in descending order if reverse=True)
    :rtype : list
    """
    size = len(array)
    for index1 in range(size - 1):
        swapVal = array[index1]
        swapIndex = index1
        for index2 in range(index1 + 1, size):
            if swapVal < array[index2] and reverse:
                swapVal = array[index2]
                swapIndex = index2
            elif swapVal > array[index2] and not reverse:
                swapVal = array[index2]
                swapIndex = index2
        array[swapIndex], array[index1] = array[index1], swapVal
        # print(array)
    return array

def bubbleSort(array,reverse=False):

    """
    Detail:
    1. For each step in an iteration , each element in the array is compared with very next element
    and the swapped if that element is greater than next element (if reverse=True ,
    then it will swap if element is less than next element )
    3. It will repeat untill complete array is sorted
    > Worst Case Time Complexity is: O(N2)
    > Average Case Time Complexity is: O(N2)
    > Best Case Time Complexity is: O(N)
    > Space Complexity: O(1)

    :param array: unsorted python list
    :type array : list
    :param reverse: If True , sorting will be done on descending order
    :type reverse : bool
    :return : Sorted array in ascending order (or  in descending order if reverse=True)
    :rtype : list
    """


    n = len(array)
    # Traverse through all array elements
    for index1 in range(n):
        swapped = False

        # Last i elements are already
        #  in place
        for index2 in range(0, n - index1 - 1):

            # traverse the array from 0 to
            # n-i-1. Swap if the element
            # found is greater than the
            # next element
            if (array[index2] > array[index2 + 1]  and not reverse) or (array[index2] < array[index2 + 1] and reverse):
                array[index2], array[index2 + 1] = array[index2 + 1], array[index2]
                swapped = True

        # IF no two elements were swapped
        # by inner loop, then break
        if swapped == False:
            break
    return array
