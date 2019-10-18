from backup import backup

def core(dataCentricToBusiness, dataBackup = ' n'):
    """
    Evaluate if the startup is secure or not.

    Parameters:
        dataCentricToBusiness (str): is the data centriuc to the business ? y/n
        dataBackup (str): is the data backup ? y/n

    Returns:
        str: Pass if it is secure, and Fail if it is not secure or we cannot determine if it is.
    """

    if dataCentricToBusiness == 'y':
        return backup(dataBackup)

    return 'Fail'
