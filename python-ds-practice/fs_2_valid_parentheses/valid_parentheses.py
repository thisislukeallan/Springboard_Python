def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    opened = '('
    closed = ')'
    balance = 0

    for paren in parens:
        if paren == opened:
            balance += 1
        elif paren == closed:
            balance -= 1
        if balance < 0:
            return False
    return balance == 0

# Solution: No need to define open/closed
        
