def merge(dict_list):
    result = {}
    for d in dict_list:
        for key, value in d.items():
            if key not in result:
                result[key] = set()
            result[key].add(value)
    return result

result = merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}])
print(result)
