def is_valid_password(self, password):
    return hashlib.sha256(password.encode()).hexdigest() == self.__password
