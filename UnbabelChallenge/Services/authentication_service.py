"""
Responsible for encrypting the passwords of new users, and 
comparing the provided passwords with stored passwords on login.

Also responsible for keeping track of wether the user is logged
in or not, and what is their corresponding user_id

Stored password structure = [PASSWORD_HASH][SALT]
  First 64 bytes = password hash
  Last 64 bytes = password salt
"""

import hashlib, binascii, os
 
logged_in = False
current_user_id = -1

def hash_password(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

def verify_password(stored_password, provided_password):
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  provided_password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password
