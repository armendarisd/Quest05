def my_is_sort(param_1):
    is_sorted = False
    if(asc_sorted(param_1) or desc_sorted(param_1)):
        is_sorted = True
    return is_sorted

def asc_sorted(param_1):
    is_sorted = True
    index = 0
    while(index < len(param_1)-1 ):
        if(param_1[index] > param_1[index + 1]):
            is_sorted = False
        index += 1
    return is_sorted

def desc_sorted(param_1):
    is_sorted = True
    index = 0
    while(index < len(param_1)-1 ):
        if(param_1[index] < param_1[index + 1]):
            is_sorted = False
        index += 1
    return is_sorted