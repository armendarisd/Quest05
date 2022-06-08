def my_array_uniq(param_1):
    resultantList = []
 
    for element in param_1:
        if element not in resultantList:
            resultantList.append(element)
    
    return resultantList