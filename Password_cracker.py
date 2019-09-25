#!/usr/bin/python
#__Author__ == 'Ananth Venkateswarlu'
# Simple MD5 password cracker

import md5
import sys

if len(sys.argv) < 3:
    print("Please enter md5 hash\n")
    print("Usage: " + "python " + sys.argv[0] + " <MD5 Hash> <Password file>")
    sys.exit()

try:
    password_file = open(sys.argv[2], 'r')

except:
    print('\nPassword file not found!!\n')
    sys.exit()

print('\nTrying to crack password. Please wait.....\n')
for password in password_file:
    md5hash = md5.new(password.strip()).hexdigest()
    if sys.argv[1] == md5hash:
        print('Password Found: {}').format(password)
        break
else:
    print('\nPassword not found!!\n')


