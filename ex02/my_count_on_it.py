import array

def my_count_on_it(param_1):
    index = 0
    param_2 = []
    while(index < len(param_1)):
        param_2.append(len(param_1[index]))
        index += 1
    return param_2
