
import string


def check_password(password):
    checks = {
        "Length (at least 8 characters)": len(password) >= 8,
        "Uppercase Letter (A-Z)": any(c in string.ascii_uppercase for c in password),
        "Lowercase Letter (a-z)": any(c in string.ascii_lowercase for c in password),
        "Number (0-9)": any(c in string.digits for c in password),
        "Symbol (!@#$%^&*)": any(c in "!@#$%^&*" for c in password),
    }

    print("\nPassword Analysis:")

    for criterion, satisfied in checks.items():
        status = "Satisfied" if satisfied else "Not satisfied"
        print(f"{criterion}: {status}")

    passed = sum(checks.values())

    if passed == 5:
        strength = "STRONG"
    elif passed >= 3:
        strength = "MODERATE"
    else:
        strength = "WEAK"

    print(f"\nPassword Strength: {strength}")


def main():
    print("=== Password Strength Checker ===")

    while True:
        password = input(
            "\nEnter your password (or type 'exit' to quit): "
        )

        if password.lower() == "exit":
            break

        check_password(password)

        choice = input(
            "\nDo you want to check another password? (y/n): "
        ).strip().lower()

        if choice != "y":
            break

    print("\nThank you! Goodbye!")


if __name__ == "__main__":
    main()
