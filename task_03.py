def max_odd(array):
    result = []

    for i in array:
        if isinstance(i, (int, float)):  
            i = int(i)  
            if i % 2 != 0:
                result.append(i)
    
    if len(result) == 0:
        return None
    
    return max(result)
