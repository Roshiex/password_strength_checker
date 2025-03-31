def check_password_strength(password):
    #check the strength of the password and return score and feedback
    score = 0
    feedback = []

    #check length 
    if len(password) < 8:
        feedback.append("Password too short. Use at least 8 characters")
    else:
        score += 1

    #check for upper case
    if not any(char.isupper() for char in password):
        feedback.append("Add uppercase letters")
    else:
        score += 1

    #check lower case 
    if not any(char.islower() for char in password):
        feedback.append("Add lowercase letters")
    else:
        score += 1

    #check nums
    if not any(char.isdigit() for char in password):
        feedback.append("Add numbers")
    else:
        score += 1

    #check special char
    special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>/?"
    if not any(char in special_chars for char in password):
        feedback.append("Add special characters like !@#$%^&*()-_=+[]{}|;:'\",.<>/?")
    else:
        score += 1

    #convert score strength rating
    if score == 0:
        strength = "V. Weak"

    elif score == 1:
        strength = "Weak"

    elif score == 2:
        strength = "Mid"

    elif score == 3:
        strength = "Getting Stronger"

    elif score == 4:
        strength = "V. strong"

    elif score == 5:
        strength = "Excellent"

    return strength, feedback

def main():
    print("===Password Strength Checker===")
    print("This checks how strong your password is")
    print("Be smart, do not post your real passwords or people might hack you")

    while True:
        password = input("Enter a password to check (or 'x' to quit): ")

        if password.lower() == 'x':
            break

        strength, feedback = check_password_strength(password)

        print(f"Password Strength: {strength}")

        if feedback:
            print("\nSuggestions to improve:")
            for suggestion in feedback:
                print(f"- {suggestion}")
        else:
            print("\nExcellent password!")
        
        print("\n====================================")
    
    print("Thank you for using Password Strength Checker!")

if __name__ == "__main__":
    main()