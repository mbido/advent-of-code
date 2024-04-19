import hashlib

def md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()