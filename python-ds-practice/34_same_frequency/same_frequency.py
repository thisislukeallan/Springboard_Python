def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    freq_num1 = {}
    freq_num2 = {}

    for num in list(str(num1)):
        freq_num1[num] = freq_num1.get(num, 0) + 1
    for num in list(str(num2)):
        freq_num2[num] = freq_num2.get(num, 0) + 1
    return freq_num1 == freq_num2

# Solution: Create frequency counter function to avoid redundency