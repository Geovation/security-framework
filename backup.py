import re

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


# def backup(answer) :
#     """
#     >>> backup('123')
#     'Fail'
#     >>> backup('ube 123')
#     'Fail'
#     """
#     x = re.search("\s", answer)
#
#     print(x)
#
# backup("The rain in Spain")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
