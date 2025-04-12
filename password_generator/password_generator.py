
import random
import string

def generate_password(length=12, use_symbols=True):
    if length < 6:
        return "❌ Password too short! Choose 6 characters or more."

    characters = string.ascii_letters + string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choices(characters, k=length))
    return password

def save_passwords(passwords, filename="saved_passwords.txt"):
    with open(filename, "a") as file:
        for pwd in passwords:
            file.write(pwd + "\n")
    print(f"✅ {len(passwords)} password(s) saved to {filename}.")

def menu():
    print("\n🔐 Welcome to the Enhanced Password Generator 🔐")
    print("1. Generate a single password")
    print("2. Generate multiple passwords")
    print("3. Exit")

def main():
    while True:
        menu()
        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            try:
                length = int(input("Enter password length (min 6): "))
                use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
                pwd = generate_password(length, use_symbols)
                print(f"Generated Password: {pwd}")
            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == '2':
            try:
                count = int(input("How many passwords to generate? "))
                length = int(input("Enter password length (min 6): "))
                use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
                passwords = [generate_password(length, use_symbols) for _ in range(count)]

                for i, pwd in enumerate(passwords, 1):
                    print(f"{i}. {pwd}")

                save = input("Do you want to save these passwords? (y/n): ").lower() == 'y'
                if save:
                    save_passwords(passwords)

            except ValueError:
                print("❌ Please enter valid numbers.")

        elif choice == '3':
            print("👋 Exiting... Stay secure!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == '__main__':
    main()
