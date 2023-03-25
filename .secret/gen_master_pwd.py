password1 = input("Enter first password: ")
password2 = input("Enter second password: ")

try:
    if password1[0] == '4' and password2[0] == 'n':
        password1, password2 = password2, password1
except IndexError:
    print("Passwords should atleast be of length 1!")

master_password = password1[::-1] + "_M-M_" + password2[::-1]

print(master_password)
