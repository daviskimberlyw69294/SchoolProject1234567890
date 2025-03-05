import random
import string

def get_random_code(length):
    """Generate a random code of the specified length.

    Args:
        length (int): The desired length of the code.

    Returns:
        str: A randomly generated code of the specified length.
    """
    code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    return code
