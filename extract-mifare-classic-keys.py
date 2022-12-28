#!/usr/bin/python
# Dependencies: https://github.com/equipter/mfkey32v2
# Author: rs-develop
# Version: 1

import sys
import re
import subprocess
import os

def help():
    print(sys.argv[0] + "<mfkey32.log>")
    print("Extract the values from the mfkey32.log file and calculates the key's using mfkey32v2.")
    print("Get mfkey32v2 from: https://github.com/equipter/mfkey32v2")

if len(sys.argv) < 2:
    help()
    exit()

if not os.path.exists("mfkey32v2"):
    print("mfkey32v2 binary not found")
    print("Get mfkey32v2 from: https://github.com/equipter/mfkey32v2")
    exit()

with open(sys.argv[1], "r") as mfkey32:
    print("Starting processing...")
    keys = set()
    for line in mfkey32:
        res = re.findall(r"[a-f0-9]{8}", line)
        mfkey_res = subprocess.run(['./mfkey32v2',res[0],res[1], res[2], res[3], 
                                    res[4], res[5], res[6]], 
                                    stdout=subprocess.PIPE).stdout.decode('utf-8')
        key_res = re.findall(r"Found Key: \[([a-f0-9]{12})", mfkey_res)
        if key_res:
            print("Key found: "+ key_res[0])
            keys.add(key_res[0])

    print("------------")
    print(str(len(keys)) + " keys found!")
    
    with open("mf_classic_dict_user.nfc", 'w') as out:
        for key in keys:
            out.writelines(key.upper() + "\n")

    print("Key's written to mf_classic_dict_user.nfc")

print("finished")