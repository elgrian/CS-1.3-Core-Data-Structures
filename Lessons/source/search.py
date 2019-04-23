#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)



def linear_search_iterative(array, item):
    # loops over the array values until the item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found and returns index
    return None  # not found


def linear_search_recursive(array, item, index=0):
    if index == len(array):
        return None  #item not found in the array
    if array[index] == item:
        return index  #item found at index
    return linear_search_recursive(array, item, index + 1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    return binary_search_recursive(array, item)
    

def binary_search_iterative(array, item):
    # Binary search divides the index on the location of the item in the array
    first_indice = 0
    last_indice = len(array)-1


    if item == array[first]:
        #returns first indice in index to determine left of middle
        return first_indice
        
    if item == array[last]: 
        #returns last indice in index to determine right of middle
        return last_indice

    while first <= last:
        #Determines middle of the index
        half = int((last_indice + first_indice) / 2) 
        
        
        #item is equal to value of indice in position half at the array
        if item == array[half]:
             # if the item is the value of the middle indice return the value
            return half       
        #Compares the item string to the array list
        if item > array[half]:
            # If item is more than the array middle, make first indice half+1
            # overwriting the first indice to be one place in front of the half point
            # Which makes the search more efficient
            first_indice = half + 1 

        # Check if item is more than the middle indice of the array 
        if item < array[half]:  
            last_indice = half - 1  # ignores right half by making last indice half - 1

    
   

def binary_search_recursive(array, item, left=None, right=None):
    # Recursive calls the function inside the function itself
    
    if right == None:
        right = len(array)-1
    if left == None:
        left = 0

    half = int((right + left) / 2)

    if left == right:
        return None

    if item == array[half]:
        return half

    elif item > array[half]:
        if item == array[right]:
            return right
        left = half + 1
        
    elif item < array[half]:
        if item == array[left]:
            return left
        right = half - 1

    return binary_search_recursive(array, item, left, right)
    