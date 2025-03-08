import random

def generate_random_code():
    """Generate a random 5-digit code"""
    return "".join(str(random.randint(0, 9)) for _ in range(5))
