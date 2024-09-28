def coincidence(list=None, range=None):

    if list is None or range is None:
        return []
    
    result = []
    
    range_min = min(range)
    range_max = max(range)
    
    for item in list:
        if isinstance(item, (int, float)) and range_min <= item <= range_max:
            result.append(item)

    return result
