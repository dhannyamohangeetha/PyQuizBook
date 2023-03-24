def create_dict_from_lists(keys, values):
    """
    This function returns a dict made from two lists.
    """
    a_list = list(zip(keys, values))
    dict_1 = dict(a_list)
    return dict_1


def merge_two_dicts(d1, d2):
    """
    Merge two Python dictionaries into one
    """
    dict2 = d1 | d2
    return dict2


def init_dict_with_values(lst, d1):
    """
    Create a dict with default values for each key listed.

    """
    return {key: d1 for key in lst}


def extract_keys_to_dict(datadict, keylist):
    """
    Create a dictionary by extracting the keylist from a given dictionary
    """
    dict3 = {i: datadict[i] for i in keylist}
    return dict3


def delete_keys_from_dict(datadict, keylist):
    """
    Delete a list of keys from a dictionary
    """
    dict4 = {i: datadict[i] for i in datadict if i not in keylist}
    return dict4


def check_dict_for_key(datadict, key):
    """
    Check if a value exists in a dictionary
    (NO FOR loops!)
    """
    return key in datadict.value()


def get_key_of_min_value(ddd):
    """
    Get the key of the minimum value from a dictionary
    """
    return min(ddd, key=ddd.get)


def get_key_of_max_value(ddd):
    """
    Get the key of the maximum value from a dictionary
    """
    return max(ddd, key=ddd.get)
