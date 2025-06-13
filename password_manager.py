
from cryptography.fernet import Fernet

# Uncomment and run this ONCE to generate the key
# def write_key():
#     key = Fernet.generate_key()
#     with open('key.key', 'wb') as key_file:
#         key_file.write(key)
# write_key()  # Run only once

def load_key():
    with open('key.key', 'rb') as file:
        key = file.read()
    return key

master_pwd = input("What's your master password? ")

key = load_key()
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pwd = data.split(" | ")
            print("User:", user, "| Password:", fer.decrypt(pwd.encode()).decode())

def add():
    name = input("Enter the Account name: ")
    pwd = input("Enter Password: ")
    with open('passwords.txt', 'a') as f:
        f.write(name + " | " + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones (view/add), or press 'q' to quit?: ").lower()

    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode selected.")
        continue
