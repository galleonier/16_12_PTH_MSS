def check_nickname(nickname):
    if not nickname[0] == '@':
        return "Incorrect"
    if len(nickname) < 5 or len(nickname) > 15:
        return "Incorrect"
    for char in nickname[1:]:
        if not (char.islower() or char.isdigit()):
            return "Incorrect"
    return "Correct"
user_nickname = input()
result = check_nickname(user_nickname)
print(result)
