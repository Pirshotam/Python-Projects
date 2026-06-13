import secrets
import string

def password_generator(length):
    pool = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(pool) for _ in range(length))
    return password

print("===== RANDOM PASSWORD GENERATOR =====")
while True:
    choice = input("Generate Password? [Yes/No]: ").upper()
    if choice=="YES":
        length=int(input("Enter password length: "))
        new_password = password_generator(length)
        print("Password is",new_password)
    elif choice=="NO":
        break
    else:
        print("Invalid input, please enter Yes or No.")

print("===== END =====")