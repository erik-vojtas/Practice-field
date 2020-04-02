
#Write a program to check the validity of password input by users.
#Conditions:
# At least 1 letter between [a-z]
# At least 1 number between [0-9]
# At least 1 letter between [A-Z]
# At least 1 character from [$#@]
# Minimum length of transaction password: 6
# Maximum length of transaction password: 12


def passwordChecker():
    p = input("Please ENTER a password: ")
    proved_l = False
    proved_u = False
    proved_d = False
    proved_s = False
    special_symbol = r'[$#@]'
    for letter in p:
        if letter.islower():
            proved_l = True
        if letter.isupper():
            proved_u = True
        if letter.isdigit():
            proved_d = True
        if letter in special_symbol:
            proved_s = True
    # print(proved_l, proved_u, proved_d, proved_s)
    if len(p) < 6:
        print(f'Minimum length of password is 6 characters.')
        return passwordChecker()
    elif len(p) > 12:
        print(f'Maximum length of password is 12 characters.')
        return passwordChecker()
    elif proved_l == False:
        print(f'Password has to contain at least 1 letter between [a-z].')
        return passwordChecker()
    elif proved_u == False:
        print(f'Password has to contain at least 1 letter between [A-Z].')
        return passwordChecker()
    elif proved_d == False:
        print(f'Password has to contain at least 1 digit between [0-9].')
        return passwordChecker()
    elif proved_s == False:
        print(f'Password has to contain at least 1 special character between [$#@].')
        return passwordChecker()
    else:
        print(f'Hureey! Your password {p} has been approved!')



passwordChecker()