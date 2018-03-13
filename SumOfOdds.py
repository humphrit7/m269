def sumOfOdds(n):
    """
    Calculates the sum off the first n odd numbers

    Parameters
    ----------
    n - an integer

    Returns
    -------
    the sum of the first n odd numbers
    """
    if n == 1:
        return 1
    else:
        return ((2 * n) - 1) + sumOfOdds(n-1)