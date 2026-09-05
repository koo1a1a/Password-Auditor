import getpass

def main():
    print("=" * 50)
    print("        PASSWORD SECURITY AUDITOR V1")
    print("=" * 50)

    #getpass used to hide name for privacy reasons 
    password = getpass.getpass("Enter unique password: ")

    print("\nPassword has been recieved")
    print(f"Password lenght: {len(password)}")

if __name__ == "__main__":
    main()

def character_analysis(password):
    return {
        "length": len(password),
        
    }