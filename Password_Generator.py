import random
import string


def main():
    try:
        length = int(input("Enter the length of the password: "))

        if length <= 0:
            print("Password length must be a positive Integer.")
            return

        getPassword = generatePass(length)
        print(f"Password Generated for the user: {getPassword}")

    except ValueError:
        print("Invalid input! Please enter a positive integer.")


def generatePass(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters)for i in range(length))
    return password

if __name__ == "__main__":
    main()