from typing import List


def flatten_lists(nested_list: List) -> List:
    """ Flattens arbitrarially deeply nested list of lists into a flat list 
        Inputs:
            nested_list: List of lists, to be flattened
        Returns:
            A flat list of all input sublists
    """
    try:
        return_list = []

        # Handle bad data format
        if not isinstance(nested_list, list):
            raise TypeError('Input has to be a list')

        if nested_list == []:
            return nested_list

        for item in nested_list:
            if isinstance(item, list):
                return_list.extend(flatten_lists(item))
            else:
                return_list.append(item)
        
        return return_list
    except Exception as ex:
        print(f'Error flattening list: {ex}')
        raise
