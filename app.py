def user_name():
    username = input("Please enter a username with a capital letter: ")
    if len(username) < 6:
        print("The username must contain at least 6 letters. Please try again")
        user_name()
    elif len(username) >= 6:
        if username[0].isupper() == True:
            with open("user data.txt", "a") as file:
                file.write(f"{username}\n")
        elif username[0].isupper() == False:
            print("Please mind the CAPITAL letter.")
            user_name()


def user_surname():
    surname = input("Please enter your surname: ")
    if len(surname) > 0:
        with open("user data.txt", "a") as file:
            file.write(f"{surname}\n")
    if len(surname) == 0:
        user_surname()



def get_email():
    email = input("Please enter your email: ")
    if "@" in email:
        if "." in email:
            if email[-1] == ".":
                print("Invalid email. Characters required after the dot. Please try again")
                get_email()
            else:
                with open("user data.txt", "a") as file:
                    file.write(f"{email}\n")
    else:
        print("Your email should contain an @ character. Please try again")
        get_email()



def get_password():
    flag = 0
    print(
        "Your password should contain letters, numbers, and at least one of these special characters:  !#$%&'()*+,-./:;<=>?@[\]^_`{|}~'")
    password = input("Please enter your password: ")
    special_chars = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~'"
    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "1234567890"

    for i in range(len(special_chars)):
        char = special_chars[i]
        if char in password:
            flag = 1
            break
    for i in range(len(letters)):
        letter = letters[i]
        if letter in password:
            flag = flag + 1
            break

    for i in range(len(numbers)):
        number = numbers[i]
        if number in password:
            flag = flag + 1
            break
    if flag == 3:
        print("Your password is strong enough. Well done!")
        with open("user data.txt", "a") as file:
            file.write(f"{password}\n")
    if flag < 3:
        print("Your password is not strong enough. Please try again.")
        get_password()