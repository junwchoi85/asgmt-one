import hashlib


def encrypt_password(password: str) -> str:
    """
    Encrypt password
    :param password: Password
    :return: Encrypted password
    """
    return hashlib.sha256(password.encode()).hexdigest()
