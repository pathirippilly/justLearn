def selectionSort(array,reverse=False):
    """
    Detail:
    1. This sort will search for the smallest (biggest if reverse=True) element starting from the first element
    2. swap minimum (maximum if reverse=True) number with first element
    3. Take the unsorted part and repeat the step 1 and 2 untill it is sorted
    Time complexity(worst case) : O(n^2)
    Space complexity (worst case) : O(n^2)

    :param array: unsorted python list
    :type array : list
    :param reverse: If True , sorting will be done on descending order
    :type reverse : bool
    :return : Sorted array in asceding order (or  in descending order if reverse=True)
    :rtype : list
    """
    size=len(array)
    for indx1 in range(size-1):
        swapVal = array[indx1]
        swapIndx = indx1
        for indx2 in range(indx1+1,size):
            if swapVal<array[indx2] and reverse:
                swapVal = array[indx2]
                swapIndx = indx2
            elif swapVal>array[indx2] and not reverse:
                swapVal = array[indx2]
                swapIndx = indx2
        array[swapIndx],array[indx1]= array[indx1],swapVal
        # print(array)
    return array
