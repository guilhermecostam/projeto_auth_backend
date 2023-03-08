import random
import string

def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))

def random_email() -> str:
    return f"{random_lower_string()}@{random_lower_string()}.com"

def random_cpf_pis() -> str:
    return ''.join(
        random.choice(
            string.ascii_uppercase + string.ascii_lowercase + string.digits
        ) for _ in range(11))