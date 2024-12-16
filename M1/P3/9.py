def is_valid_ip(ip):
    octets = ip.split(".")
    return all(octet.isdigit() and 0 <= int(octet) <= 255 and str(int(octet)) == octet for octet in octets) and len(octets) == 4

print(is_valid_ip('10.0.1.1'))
print(is_valid_ip('10.1.1.a'))
print(is_valid_ip('10.1.1.260'))
print(is_valid_ip('10.0023.0123.0000015'))
