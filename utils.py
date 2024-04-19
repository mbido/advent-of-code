import hashlib
import re
import numpy as np
from itertools import product

def md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()