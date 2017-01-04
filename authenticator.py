#!/usr/bin/python

import sys
import os
from hashlib import sha512, sha256
import base64

from lib.hotpie import TOTP


b32Key = ''
secret = base64.b32decode(b32Key)

digits = TOTP(secret, digits=6 )
print(digits)

