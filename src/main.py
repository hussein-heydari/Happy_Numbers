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
    if squared_sum == 1:
        return True
    else:
        return is_happy_num(squared_sum)

while True:
    try:
        user_input = input("You give me a number, and I'll tell you if it's a happy number or not" \
                           "(You can type in exit or quit to terminate the program): ")
        if user_input.lower() in ['exit','quit', 'q']:
            print("Exiting the program. Goodbye!")
            break
        if is_happy_num(user_input):
            print("This number is a happy number!")
    except RecursionError:
        print("This number is not a happy number.")
