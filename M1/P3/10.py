def is_good_password(password):
    return (len(password) >= 7 and
            any(c.isdigit() for c in password) and
            any(c.islower() for c in password) and
            any(c.isupper() for c in password))

print("YES" if is_good_password(input()) else "NO")
