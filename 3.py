import re

def assess_password_strength(password):
    # Define criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_char_criteria = re.match(r'^[\w@#$%^&+=]+$', password) is not None

    # Calculate score
    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])

    # Provide feedback
    if score == 5:
        return "Strong"
    elif score >= 3:
        return "Moderate"
    else:
        return "Weak"

def main():
        password = input("Enter your password:")
        strength = assess_password_strength(password)
        print("Password strength:", strength)
if __name__ == "__main__":
    main()