def get_unique(content: dict) -> set:
    """Get all unique keys for a dictionary of dictionaries of an unknown depth """
    keys = []

    # recursive function to key the keys of all dictionaries contained in the outer dictionary
    def get_all_keys(contents: dict, lst: list) -> None:
        for key, value in contents.items():
            lst.append(key)
            if not isinstance(value, dict):
                continue
            elif isinstance(value, dict):
                get_all_keys(value, lst)

    get_all_keys(content, keys)
    # use set to only return unique values in the list of keys
    return set(keys)
