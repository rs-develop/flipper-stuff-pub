# flipper zero tools by rs-develop

## extract-mifare-classic-keys.py
Automatically extracts the the values from '.mfkey32.log', calculates the key's using Mfkey32v2 and creates a new 'mf_calssic_dict_user.nfc' file.

**Steps**
1) Read the MIFARE Classic Card/Chip
2) Skip reading the key's
3) Select "Detect Reader"
4) Read the values from the Reader Device
5) Extract the '.mfkey32.log' using qFlipper (enable hidden files)
6) Execute the script: 'extract-mifare-classic-keys.py </path/to/mfkey32.log>' (make sure the mfkey32v2 binary is located in the same directory as the script)
7) Copy the generated 'mf_classic_dict_user.nfc' to the flipper (maybe backup your old one first)
8) Read the card again

