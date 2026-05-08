from zxcvbn import zxcvbn

# Leetspeak Function
def leetspeak(word):
    return word.replace('a', '@').replace('i', '1').replace('o', '0').replace('e', '3')

# Menu
print("===== Password Security Tool =====")
print("1. Password Strength Checker")
print("2. Custom Wordlist Generator")

choice = input("Enter Your Choice (1/2): ")

# Password Checker
if choice == "1":

    password = input("Enter Password To Check: ")

    result = zxcvbn(password)

    score = result['score']

    print("\nPassword Score:", score)

    if score <= 1:
        print("Weak Password")
    elif score == 2:
        print("Medium Password")
    else:
        print("Strong Password")

# Wordlist Generator
elif choice == "2":

    print("\n--- Wordlist Generator ---")

    name = input("Enter Your Name: ")
    pet = input("Enter Pet Name: ")
    year = input("Enter Birth Year: ")

    wordlist = [
        name + year,
        pet + year,
        name + "@123",
        pet + "@123",
        name + pet,
        name.capitalize() + year,
        pet.capitalize() + "@2025",

        leetspeak(name),
        leetspeak(pet),

        leetspeak(name) + year,
        leetspeak(pet) + "@123"
    ]

    with open("wordlist.txt", "w") as file:
        for word in wordlist:
            file.write(word + "\n")

    print("\nWordlist Generated Successfully!")
    print("Saved in wordlist.txt")

else:
    print("Invalid Choice!")