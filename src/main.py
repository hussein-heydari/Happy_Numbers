def is_happy_num(num):
    """Takes in a number as input and determines whether it's a happy number or not

    :param num: a number
    :type num: str
    :return: True if happy number, False otherwise
    :rtype: bool
    """
    iterable_num = [int(i) for i in str(num)]
    squared_sum = 0
    for i in iterable_num:
        squared_sum += i ** 2 
    print(squared_sum)
    if squared_sum == 1:
        return True
    else:
        return is_happy_num(squared_sum)
