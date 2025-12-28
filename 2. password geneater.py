import random
import string

length = int(input("Enter password length: "))

print("Choose complexity:")
print("1. Letters only")
print("2. Letters + Numbers")
print("3. Letters + Numbers + Symbols")

choice = input("Enter choice: ")

if choice == "1":
    chars = string.ascii_letters
elif choice == "2":
    chars = string.ascii_letters + string.digits
elif choice == "3":
    chars = string.ascii_letters + string.digits + string.punctuation
else:
    print("Invalid choice")
    exit()

password = "".join(random.choice(chars) for _ in range(length))
print("Generated Password:", password)




