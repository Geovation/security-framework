def backup(answer) :
    """
    >>> backup('Yes')
    'Pass'
    >>> backup('Y')
    'Pass'
    >>> backup('y')
    'Pass'
    >>> backup('Ye')
    'Fail'
    >>> backup('No')
    'Fail'
    >>> backup('N')
    'Fail'
    >>> backup('n')
    'Fail'
    >>> backup('Maybe')
    'Fail'
    >>> backup(' ')
    'Fail'
    >>> backup("'")
    'Fail'
    >>> backup('"')
    'Fail'
    >>> backup('123')
    'Fail'
    """
    if answer == 'Ye' or answer == 'No' or answer == 'N' or answer == 'n' \
         or answer == 'Maybe' or answer == ' ' or answer == '"' or answer =="'" \
         or answer.isnumeric() :
        return "Fail"
    return "Pass"
