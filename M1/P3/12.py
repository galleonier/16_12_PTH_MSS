def convert_to_python_case(text):
    return ''.join(['_' + char.lower() if char.isupper() else char for char in text]).lstrip('_')

print(convert_to_python_case('ThisIsCamelCased'))
print(convert_to_python_case('IsPrimeNumber'))
print(convert_to_python_case('FBIIsWatchingYou'))
