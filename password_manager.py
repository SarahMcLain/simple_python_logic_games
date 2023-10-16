from cryptography.fernet import Fernet
import os

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


master_pwd = input("What is the master password?")

if master_pwd == "password":
    key = load_key() + master_pwd.encode()
    fer = Fernet(key)




# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)

# write_key()


    def view():
        if not os.path.exists('passwords.csv'):
            print('That file does not exist.  You can create the file by making a new entry')
            add()
        else:
            with open('passwords.csv', 'r') as f:
                for line in f.readlines():
                    data = line.rstrip()
                    name, password = data.split(",")
                    print("User:", name, "\n Password:", fer.decrypt(password.encode()).decode())

    def add():
        name = input('Account Name: ')
        password = input("Password: ")

        with open('passwords.csv', 'a') as f:
            f.write(name + "," + fer.encrypt(password.encode()).decode() + "\n")

    while True: 
        mode = input("Would ou like to add a new password or view existing one? ('view'/'add'/'q')").lower()
        if mode == "view":
            view()
        elif mode == "add":
            add()
        elif mode == 'q':
            quit()
        else:
            print("invalid")
else:
    print("Wrong password. Access Denied")