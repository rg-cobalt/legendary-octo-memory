def insecure_hashing(password):
    # Insecure hashing
    import hashlib
    return hashlib.md5(password.encode()).hexdigest()
