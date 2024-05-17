def add_tuple(tuple_a=(), tuple_b=()):
    # Define the default values for the tuples
    tuple_a = (0, 0) if len(tuple_a) < 2 else tuple_a[:2]
    tuple_b = (0, 0) if len(tuple_b) < 2 else tuple_b[:2]

    # Add the corresponding elements of the tuples
    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return result
