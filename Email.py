email = input("Enter your Email")
k = False
t = False
f = False
if len(email) >= 6:
    f = True
    if email[0].isalpha():
        f = True
        if ('@' in email) and (email.count('@') == 1):
            f = True
            if (email[-4] == '.') or (email[-3] == '.'):
                f = True
                for i in email:
                    if i == i.isspace():
                        f = True
                        k = True
                    elif i == i.upper():
                        f = True
                        t = True
                    elif i != i.isalpha() and i != i.isnumeric():
                        f = True
                        t = True
                    else:
                        print('Wrong Email:ERROR- character error')
                        exit()

            else:
                print('Wrong Email:ERROR-. placed on invalid place')
                exit()
        else:
            print('Wrong Email:ERROR-@ is missing or greater than 1 character(@) of email ')
            exit()

    else:
        print('Wrong Email:ERROR-1st character of email is invalid')
        exit()

else:
    print('WRONG EMAIL Error- Length is too small without @ or . or invalid character')
    exit()

if f == True:
    print("Email is ok!")
