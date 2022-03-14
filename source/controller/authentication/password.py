import os
import hashlib

# code for encrypting userpassword and generated salt
class EncPassword():
    def __init__(self, password: str, salt: str=None):
        self.__password = password
        if (salt is None):
            self.salt = os.urandom(8)
        else:
            self.salt = bytearray.fromhex(salt)

    def getPassword(self):
        return(hashlib.pbkdf2_hmac('sha256', self.__password.encode(), self.salt, 100).hex())

    def getSalt(self):
        return(self.salt.hex())