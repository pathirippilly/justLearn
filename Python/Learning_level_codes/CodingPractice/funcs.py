def count_substring(string, sub_string):
    """
    This function accepts a string to search and another substring to be searched
    and returns an integer which is the number occurrences of substring in string

    :param str string: A string to search
    :param str sub_string: A substring to be searched inside string
    :return: occurrences  sub_string in string
    :rtype: int
    """
    if string.find(sub_string) + 1:
        return count_substring(string[string.find(sub_string) + max(len(sub_string) - 1,1):], sub_string) + 1
    else:
        return 0


def factorial(number):
    """
    This function accepts an integer and returns the factorial of the number

    :param int number: number for which factorial needs to be calculated
    :returns: factorial of the number
    :rtype: int
    """
    if number<=1:
        return 1
    else:
        return factorial(number-1)*number