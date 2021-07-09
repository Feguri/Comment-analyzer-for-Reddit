""" BUBBLE SORTING ALGORITHMS """


def sorting_decorator(fun):
    """ Returns wrapper until the list is completely sorted from smallest to biggest number """
    def wrapper(*args):
        result = fun(args[0])
        while True:
            result = fun(result[0])
            if result[1]:
                return result[0]

    return wrapper


@sorting_decorator
def sort_list(_list: list):
    """ Loops through a list using the bubble sort algorithm """

    for item in _list:
        if type(item) != int:
            if type(item) == float:
                break
            elif type(item != float):
                raise TypeError('All list indices must be integers or float')

    curr_index = 0
    complete = True
    while True:
        try:
            if _list[curr_index] > _list[curr_index + 1]:
                previous = _list[curr_index]
                _list[curr_index] = _list[curr_index + 1]
                _list[curr_index + 1] = previous
                complete = False
            curr_index += 1
        except IndexError:
            break
    return [_list, complete]


def sort_dict(_dict: dict):
    """ Loops through a dictionary using the list bubble sort algorithm.
        Dict values must be integers. """

    dict_values = list(_dict.values())

    sorted_values = sort_list(dict_values)

    sorted_dictionary = {}

    for item in sorted_values:
        for key, value in _dict.items():
            if _dict[key] == item:
                sorted_dictionary[key] = item

    return sorted_dictionary
