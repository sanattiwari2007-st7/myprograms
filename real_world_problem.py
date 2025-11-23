def is_valid_simple_email(email_address):
    """
    Checks if a string meets simple email validation criteria.

    Args:
        email_address (str): The string to validate.

    Returns:
        bool: True if the string is a valid simple email, False otherwise.
    """
    if ' ' in email_address:
        return False

    if email_address.count('@') != 1:
        return False

    try:
        local_part, domain_part = email_address.split('@')
    except ValueError:
        return False
    if '.' not in domain_part:
        return False

    if not local_part or not domain_part:
        return False
        
    return True

print("--- Simple Email Validator Tests ---")

print(f"test@example.com: {is_valid_simple_email('test@example.com')}") 
print(f"user.name123@sub.domain.net: {is_valid_simple_email('user.name123@sub.domain.net')}") 

print("-" * 35)

print(f"test@example: {is_valid_simple_email('test@example')}") 
print(f"test@example@com: {is_valid_simple_email('test@example@com')}") 
print(f"test example@com: {is_valid_simple_email('test example@com')}") 
print(f"@example.com: {is_valid_simple_email('@example.com')}") 
print(f"test@.com: {is_valid_simple_email('test@.com')}") 