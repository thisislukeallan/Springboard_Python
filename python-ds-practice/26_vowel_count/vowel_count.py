def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    v_count = {}
    vowels = 'aeiou'
    for letter in phrase.lower():
        frequency = 0
        if letter in vowels:
            v_count[letter] = v_count.get(letter, frequency) + 1
    return v_count