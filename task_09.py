def connect_dicts(dict1, dict2):

    if sum(dict1.values()) > sum(dict2.values()):
        main_dict = dict1
        side_dict = dict2

    elif sum(dict1.values()) < sum(dict2.values()):
        main_dict = dict2
        side_dict = dict1

    else:
        main_dict = dict2
        side_dict = dict1

    main_dict = {k: v for k, v in main_dict.items() if v >= 10}
    side_dict = {k: v for k, v in side_dict.items() if v >= 10}

    merged = {**side_dict, **main_dict}
    sorted_dict = dict(sorted(merged.items(), key=lambda item: item[1]))
    
    return sorted_dict
