def greet(*args):
    if len(args) == 1:
        return f"Hello, {args[0]}!"
    return f"Hello, {', '.join(args[:-1])} and {args[-1]}!"
print(greet('Ivan', 'Roman', 'Ruslan'))