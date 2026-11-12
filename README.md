# Password Strength Checker

A Python program that rates how strong a password is and gives tips to improve it.

## What it checks
- Length (12+ characters)
- Uppercase, lowercase, numbers and symbols
- A list of common weak passwords, including ones like "password123"

## How to run
1. Install Python 3
2. Run: `python password_checker.py`
3. Type a password when asked

## Example
**Weak** password:
Enter a password to check: password123
Score: 0 out of 6
Rating: Weak
- Use at least 12 characters.
- Add an uppercase letter.
- Add a symbol like ! or #.
- This is a very common password. Pick something unique.
**Strong** password:
Enter a password to check: Tigers#Rule2026
Score: 6 out of 6
Rating: Strong

## What I learned
...

## Limitations
It only checks a short list of common passwords. Real tools use much larger lists.
