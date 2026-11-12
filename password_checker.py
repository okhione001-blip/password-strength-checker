
import string

def check_length(password):
    return len(password) >= 12

def has_upper(password):
    return any(c.isupper() for c in password)

def has_lower(password):
    return any(c.islower() for c in password)

def has_digit(password):
    return any(c.isdigit() for c in password)

def has_symbol(password):
    return any(c in string.punctuation for c in password)

COMMON_PASSWORDS = {
    "password", "123456", "12345678", "qwerty", "abc123",
    "letmein", "welcome", "admin", "iloveyou", "monkey",
    "dragon", "football", "111111", "password1", "passw0rd",
    "111", "222" , "1234" , "qwertyuiop", "aa123456", "princess"
}

def is_common(password):
    lowered = password.lower()
    stripped = lowered.rstrip("0123456789")
    return lowered in COMMON_PASSWORDS or stripped in COMMON_PASSWORDS

def score_password(password):
    score = 0
    tips = []

    if check_length(password):
        score += 2
    else:
        tips.append("Use at least 12 characters.")

    if has_upper(password):
        score += 1
    else:
        tips.append("Add an uppercase letter.")

    if has_lower(password):
        score += 1
    else:
        tips.append("Add a lowercase letter.")

    if has_digit(password):
        score += 1
    else:
        tips.append("Add a number.")

    if has_symbol(password):
        score += 1
    else:
        tips.append("Add a symbol like ! or #.")

    if is_common(password):
        score = 0
        tips.append("This is a very common password. Pick something unique.")

    return score, tips

def get_rating(score):
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"

password = input("Enter a password to check: ")

score, tips = score_password(password)
print("Score:", score, "out of 6")
print("Rating:", get_rating(score))
for tip in tips:
    print("-", tip)