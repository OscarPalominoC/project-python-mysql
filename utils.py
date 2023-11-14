# Validate email using regex
import re


def validate_email(email: str):
    """
    A function that validates an email using regular expressions.

    Args:
        email (str): Email provided by the user.

    Returns:
        Bool: True if it is a valid email. False if it is an invalid email.
    """
    regex = r'[A-Za-z0-9._%+-]+@+[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
    if re.match(regex, email):
        return True
    return False