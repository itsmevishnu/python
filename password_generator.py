import random

def generate_password(length):
    # defining the characters required in the password
    small = "abcdefghijklmnopqrstuvwxyz"
    caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "1234567890"
    symbols = "!@#$%&*()[];:?/"
    allowed = small+caps+numbers+symbols

    password = "".join([ random.choice(allowed) for i in range(length)])

    return password

def main():
    # reads the input
    length = int(input("Enter the legnth of password\t"))
    password = generate_password(length)
    print(f"The suggested password is : {password}")

if __name__ == '__main__':
    main()