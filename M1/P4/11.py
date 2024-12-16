def modify_list(lst):
    result = []
    for item in lst:
        if isinstance(item, str):
            result.append(item + '!')
        elif isinstance(item, int):
            result.append(item + 1)
        elif isinstance(item, bool):
            result.append(not item)
        elif isinstance(item, list):
            result.append(item * 2)
        elif isinstance(item, dict):
            item["newkey"] = True
            result.append(item)
        elif item is not None:
            result.append(item)
    return result

objects = ["Hello", 179, True, None, [1, 2, 3], {"key": "value"}]
print(modify_list(objects))
