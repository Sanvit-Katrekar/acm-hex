password1 = input("Enter first password: ")
password2 = input("Enter second password: ")

master_password = password1[::-1] + "_M-M_" + password2[::-1]

print(master_password)
