def intersection(l1, l2):
    """Return intersection of two lists as a new list::
    
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
        
        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]
        
        >>> intersection([1, 2, 3], [3, 4])
        [3]
        
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """
    intersect = []
    for item1 in l1:
        for item2 in l2:
            if item1 == item2:
                intersect.append(item2)
    return intersect

    # set2 = set(l2)
    # return [val for val in l1 if val in set2]

    # Alternatively, using built-in set math:
    # return list(set(l1) & set(l2)) 