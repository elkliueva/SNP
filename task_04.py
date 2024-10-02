def sort_list(lst):

    if not lst:
        return []
    
    if len(lst) == 1:
        return lst + lst

    min_val = min(lst)
    max_val = max(lst)

    new_lst = []

    for x in lst:
        if x == min_val:
            new_lst.append(max_val)
        elif x == max_val:
            new_lst.append(min_val)
        else:
            new_lst.append(x)

    new_lst.append(min_val)
    return new_lst
