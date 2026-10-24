
# 🔐 Password Strength Checker

## 📌 Project Overview

The Password Strength Checker is a simple Python application that evaluates password strength based on five basic security criteria. It helps users understand password composition and demonstrates fundamental Python concepts such as conditional statements, strings, loops, functions, and dictionaries.

## 🎯 Objectives

- Check whether a password contains at least 8 characters.
- Identify uppercase and lowercase letters.
- Verify the presence of numeric digits.
- Check for special symbols.
- Classify passwords as STRONG, MODERATE, or WEAK.
- Allow users to check multiple passwords in a single session.

## ✨ Features

- 📏 **Length Validation:** Checks whether the password contains at least 8 characters.
- 🔠 **Uppercase Validation:** Checks for at least one uppercase letter (A–Z).
- 🔡 **Lowercase Validation:** Checks for at least one lowercase letter (a–z).
- 🔢 **Number Validation:** Checks for at least one digit (0–9).
- 🔣 **Symbol Validation:** Checks for at least one symbol from `!@#$%^&*`.
- 💪 **Strength Classification:** Displays the overall password strength.
- 🔄 **Repeated Testing:** Allows users to check multiple passwords without restarting the program.

## 🛠️ Technologies Used

- 🐍 **Programming Language:** Python 3
- 🌿 **Version Control:** Git
- 🐙 **Repository Hosting:** GitHub

## 📂 Project Structure

```text
Password-Strength-Checker/
├── password_checker.py
├── README.md
└── screenshots/
    ├── strong_password.png
    ├── moderate_password.png
    └── weak_password.png
```

## 📋 Requirements

- Python 3.x installed on your system.
- A terminal or command prompt.
- No external Python packages are required.

## 🚀 How to Run

**Step 1:** Clone or download this repository.

**Step 2:** Open the project folder in your terminal.

**Step 3:** Run the following command:

```bash
python password_checker.py
```

**Step 4:** Enter a password when prompted.

**Step 5:** Review the validation results and overall password strength.

**Step 6:** Enter `y` to check another password or `n` to quit. You can also enter `exit` at the password prompt to terminate the program.

## 📏 Password Strength Rules

| Criteria | Requirement |
|---|---|
| 📏 Length | At least 8 characters |
| 🔠 Uppercase | At least one uppercase letter (A–Z) |
| 🔡 Lowercase | At least one lowercase letter (a–z) |
| 🔢 Number | At least one digit (0–9) |
| 🔣 Symbol | At least one character from `!@#$%^&*` |

### 💪 Strength Classification

| Criteria Passed | Password Strength |
|---|---|
| 5 out of 5 | 🟢 STRONG |
| 3 or 4 out of 5 | 🟡 MODERATE |
| Fewer than 3 out of 5 | 🔴 WEAK |

## 💻 Sample Output

### ✅ Test Case 1: Strong Password

**Input:** `Hello@123`

```text
=== Password Strength Checker ===

Enter your password (or type 'exit' to quit): Hello@123

Password Analysis:
Length (at least 8 characters): Satisfied
Uppercase Letter (A-Z): Satisfied
Lowercase Letter (a-z): Satisfied
Number (0-9): Satisfied
Symbol (!@#$%^&*): Satisfied

Password Strength: STRONG
```

### ⚠️ Test Case 2: Moderate Password

**Input:** `Abc123`

```text
Password Analysis:
Length (at least 8 characters): Not satisfied
Uppercase Letter (A-Z): Satisfied
Lowercase Letter (a-z): Satisfied
Number (0-9): Satisfied
Symbol (!@#$%^&*): Not satisfied

Password Strength: MODERATE
```

### ❌ Test Case 3: Weak Password

**Input:** `password`

```text
Password Analysis:
Length (at least 8 characters): Satisfied
Uppercase Letter (A-Z): Not satisfied
Lowercase Letter (a-z): Satisfied
Number (0-9): Not satisfied
Symbol (!@#$%^&*): Not satisfied

Password Strength: WEAK
```

## 📸 Screenshots

Screenshots of the program's execution are included in the `screenshots/` directory.

They demonstrate:

- ✅ Strong password validation.
- ⚠️ Moderate password validation.
- ❌ Weak password validation.

These screenshots provide visual evidence that the program works as expected.

## 🛡️ Security Note

This project is intended for educational purposes. It checks basic password composition rules and does not measure resistance to password guessing, dictionary attacks, or credential leaks.

**Important:** Do not enter real, sensitive, or reused passwords into this demonstration program.

## 🎓 Learning Outcomes

- Understanding Python strings, loops, functions, and conditional statements.
- Using dictionaries to organize validation criteria.
- Applying basic password validation techniques.
- Testing programs with different inputs.
- Learning Git, GitHub repository management, and project documentation.

## 👩‍💻 Author

Developed as a Python programming and GitHub learning task.

## 📜 License

This project is available for educational and learning purposes.
