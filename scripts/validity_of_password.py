import re

def validate_passwords(passwords):
    password_list = passwords.split(',')
    valid_passwords = []
    lowercase_pattern = re.compile(r'[a-z]')
    uppercase_pattern = re.compile(r'[A-Z]')
    digit_pattern = re.compile(r'[0-9]')
    special_char_pattern = re.compile(r'[$#@]')

    for password in password_list:
        if (6 <= len(password) <= 12 and
            lowercase_pattern.search(password) and
            uppercase_pattern.search(password) and
            digit_pattern.search(password) and
            special_char_pattern.search(password)):
            valid_passwords.append(password)

    return ','.join(valid_passwords)

def validate_pwd():
    input_password = "asqwr1234@1,aF145#,2w3E*,2We3345"
    output = validate_passwords(input_password)
    print("Output =", output)
