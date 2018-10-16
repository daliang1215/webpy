import os
from hashlib import sha256
from hmac import HMAC

def encrypt_password(password, salt=None):
    """Hash password on the fly."""
    if salt is None:
        salt = os.urandom(8) # 64 bits.

    assert 8 == len(salt)
    assert isinstance(salt, str)

    if isinstance(password, unicode):
        password = password.encode('UTF-8')

    assert isinstance(password, str)

    result = password
    for i in xrange(10):
        result = HMAC(result, salt, sha256).digest()

    return salt + result

def validate_password(hashed, input_password):
    if hashed == encrypt_password(input_password, salt=hashed[:8]):
        return 0 
    else:
        return 1

hashed = encrypt_password('123456')
print hashed
print validate_password(hashed, '123456')

print encrypt_password('123456')

##
# Ref URL: https://www.cnblogs.com/suke99/p/5814723.html
#
##
