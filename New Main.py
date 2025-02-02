import string

def check_pwd():
    password = input("Enter Password")
    strength = 0
    remarks = ''
    lower_count = upper_count = num_count = wspace_count = special_count = 0

    for char in password:
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            wspace_count += 1
        else:
            special_count += 1

    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if wspace_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1

    if strength == 1:
        remarks = "Very Bad Password!!! Change ASAP"
    elif strength == 2:
        remarks = "Not A Good Password!!! Change ASAP"
    elif strength == 3:
        remarks = "It's a weak password, consider changing"
    elif strength == 4:
        remarks = "It's a hard password, but can be better"
    elif strength == 5:
        remarks = "A very strong password"

    print("\nYour password has:")
    print(f"{lower_count} lowercase characters")
    print(f"{upper_count} uppercase characters")
    print(f"{num_count} numeric characters")
    print(f"{wspace_count} whitespace characters")
    print(f"{special_count} special characters")
    print(f"Password Strength: {strength}")
    print(f"Hint: {remarks}\n")

def ask_pwd(another_pwd=False):
    while True:
        if another_pwd:
            choice = input('Do you want to enter another password? (y/n): ')
        else:
            choice = input('Do you want to check a password? (y/n): ')

        choice = choice.strip().lower()  # Remove spaces & make lowercase

        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print('Invalid input, please enter "y" or "n".')

print('+++ Welcome to Password Checker +++')

ask_pw = ask_pwd()  # Ask user if they want to check a password

while ask_pw:
    check_pwd()  # Run password checker
    ask_pw = ask_pwd(True)  # Ask again if they want to check another password

print("Exiting Password Checker. Goodbye!")
