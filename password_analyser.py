import getpass

def main():
    print("=" * 50)
    print("        PASSWORD SECURITY AUDITOR V1")
    print("=" * 50)

    #getpass used to hide name for privacy reasons 
    password = getpass.getpass("ENTER UNIQUE PASSWORD: ")

    analysis = character_analysis(password)
    length_rating = length_analysis(analysis["length"])


    print("\nPASSWORD ANALYSIS...")
    print("-" * 50)

    print(f"PASSWORD LENGTH: {checkmark(analysis['length'])}")
    print(f"PASSWORD UPPERCASE: {checkmark(analysis['uppercase'])}")
    print(f"PASSWORD LOWERCASE: {checkmark(analysis['lowercase'])}")
    print(f"PASSWORD NUMBER: {checkmark(analysis['numbers'])}")
    print(f"PASSWORD SPECIAL CHAR: {checkmark(analysis['special'])}")

    print(f"\nLENGTH RATING: {length_rating}")

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