import getpass
from collections import Counter

def main():
    print("=" * 50)
    print("        PASSWORD SECURITY AUDITOR V1")
    print("=" * 50)

    #getpass used to hide name for privacy reasons 
    password = getpass.getpass("ENTER UNIQUE PASSWORD: ")

    analysis = character_analysis(password)
    length_rating = length_analysis(analysis["length"])
    variety = char_variety(analysis)
    repeated = find_repeat(password)
    sequential = sequential_check(password)


    print("\nPASSWORD ANALYSIS...")
    print("-" * 50)

    print(f"PASSWORD LENGTH: {checkmark(analysis['length'])}")
    print(f"PASSWORD UPPERCASE: {checkmark(analysis['uppercase'])}")
    print(f"PASSWORD LOWERCASE: {checkmark(analysis['lowercase'])}")
    print(f"PASSWORD NUMBER: {checkmark(analysis['numbers'])}")
    print(f"PASSWORD SPECIAL CHAR: {checkmark(analysis['special'])}")
    print(f"SEQUENTIAL CHARACTERS: {checkmark(sequential)}")

    print(f"\nLENGTH RATING: {length_rating}")
    print(f"\nCHARACTER VARIETY SCORE: {variety}/4")

    if repeated:
        print("REPEATED CHARACTERS: ✗")
        print(f"REPEATED: {repeated}")
    else:
        print("REPEATED CHARACTERS: ✓")

if __name__ == "__main__":
    main()

def character_analysis(password):
    return {
        "length": len(password),
        "uppercase": any(char.isupper() for char in password),
        "lowercase": any(char.islower() for char in password),
        "numbers": any(char.isdigit() for char in password),
        "special": any(char.isalnum() for char in password),
    }

def checkmark(value):
    return "✓" if value else "✗"

def length_analysis(length):
    if length < 6:
        return "VERY WEAK"
    elif length < 10:
        return "WEAK"
    elif length < 14:
        return "STRONG"
    else:
        return "VERY STRONG"

def char_variety(analysis):
    catagories = 0

    if analysis["uppercase"]:
        catagories += 1
    if analysis["lowercase"]:
        catagories += 1
    if analysis["numbers"]:
        catagories += 1
    if analysis["special"]:
        catagories += 1

    return catagories

def find_repeat(password):
    counts = Counter(password)

    repeated = {
        char: count
        for char, count in counts.items()
        if count >= 3
    }

    return repeated

def sequential_check(password):
    password = password.lower()
    sequences = [
        "abcdefghijklmnopqrstuvwxyz",
        "0123456789",
        "qwertyuiop",
        "asdfghjkl",
        "zxcvbnm"
    ]

    for sequence in sequences:
        for i in range(len(sequence) - 2):
            if sequence[i:i + 3] in password:
                return True
    return False