def mean(*args):
    numbers = [x for x in args if isinstance(x, (int, float))]
    return sum(numbers) / len(numbers) if numbers else 0.0