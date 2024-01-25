def freq_count(coll):
    """Returns a frequency count of collection"""

    count = {}

    for n in coll:
        count[n] = count.get(n, 0) + 1

    return count


def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    return freq_count(str(num1)) == freq_count(str(num2))