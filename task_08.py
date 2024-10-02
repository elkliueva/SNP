def multiply_numbers(inputs):
    
    if inputs is None:
        return None

    item = 1
    has_digit = False

    str_inputs = str(inputs)

    for i in str_inputs:
        if i.isdigit():
            item *= int(i)
            has_digit = True

    if has_digit:
        return item

    return None
