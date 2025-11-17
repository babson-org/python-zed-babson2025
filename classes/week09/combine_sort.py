from combine import combine
def combine_sort(unsorted):

    unsorted = [5, 4, 3, 2, 1]
    size = len(unsorted)

    # start with the first element as the initial 'left' list
    left = unsorted[0:1]

    # loop through the rest of the list, combining step by step
    for idx in range(1, size):
        right = [unsorted[idx: idx + 1]]    
        left = combine(left, right) 

    return(left)
print(combine_sort)