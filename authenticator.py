#!/usr/bin/python

import sys
import os
from hashlib import sha512, sha256
import base64


dir_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(dir_path + '/lib')

from lib.hotpie.hotpie import TOTP


b32Key = ''
secret = base64.b32decode(b32Key)

digits = TOTP(secret, digits=6 )
print(digits)

