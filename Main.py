from Password import Password

def main():


    length = int(input("Length of the new password:  "))
    password = Password(length)
    print("\n"+password.newPassword())


if __name__ == "__main__":
    main()
