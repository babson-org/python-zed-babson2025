def combine(left,right):
    array = []
    l_cur = 0
    r_cur = 0 

    while l_cur <len(left) and r_cur < len(right):
        if left[l_cur] <right [r_cur]:
            array.append(left[l_cur])
            l_cur += 1 
        else:
            array.append(right[r_cur])
            r_cur += 1

    return array + left [l_cur:] + right [r_cur:]