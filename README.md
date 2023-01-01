# flipper zero tools by rs-develop
More tools may be added ...

## mfkey_extract
Automatically downloads the content of the `.mfkey32.log` file from the flipper, reads the values, calculates the key's using mfkey32v2 and uploads the key's to the flippers nfc user dict. Also provides the extrcat mode. This mode can be used to extract the key's from a local `.mfkey32.log` file which was downloaded using qFlipper. The extract mode creates a `mf_classic_dict_user.nfc` file which can be uploaded to the flipper device using qFlipper. The `cli` mode is for Linux users only. `Mfkey32vs` is mandatory (https://github.com/equipter/mfkey32v2). 

**Available arguments**
```shell
usage: mfkey_extract.py [-h] [--cli] [--detect] [--extract LOGFILE]
                        [--clean-cache] [--clean-mfkey32-log] [--bkp-user-dict]
                        [--rm-dict-user]

Extracts Mifare valus from flipper or a local mfkey32.log file, computes the
key's using mfkey32v2 and uploads them to flipper. The new computed key's will
added to the content of the "/SD/nfc/assets/mf_classic_dict_user.nfc" file. The
cli and detect mode are Linux only.

options:
  -h, --help           show this help message and exit
  --cli                Extract the values via flipper CLI, compute the key's
                       and upload them to flipper (full auto mode)
  --detect             Detect Flipper Zero Device - prints only the block
                       device
  --extract LOGFILE    Extract Keys from a local mfkey32.log file and creates a
                       "mf_classic_dict_user.nfc" file.
  --clean-cache        Removes all files in the (/SD/nfc/.cache) directory.
  --clean-mfkey32-log  Cleans the mfkey32.log file from flipper.
  --bkp-user-dict      Creates a backup of the "mf_classic_dict_user.nfc" file.
                       The backup file will be placed in the same dir on the
                       flipper.
  --rm-dict-user       Removes the "mf_classic_dict_user.nfc" file from the
                       flipper.

```

**Steps for cli mode**
1) Read the Mifare Classic Card/Chip
2) Skip reading the key`s
3) Select "Detect Reader"
4) Connect the flipper to the computer
5) run `mfkey_extract.py --cli`
6) Read the card again. Now more key's and sectors should be available for read.

**Steps for extract mode**
1) Read the MIFARE Classic Card/Chip
2) Skip reading the key's
3) Select "Detect Reader"
4) Extract the '.mfkey32.log' using qFlipper (enable hidden files)
5) Execute the script: `mfkey_extract.py --extract` </path/to/mfkey32.log>'
6) Copy the generated 'mf_classic_dict_user.nfc' to the flipper (maybe backup your old one first)
7) Read the card again.

**Extra features**
- clean-cache: remove all cache files from flipper `/SD/nfc/.cache/` to prevent reading errors
- clean-mfkey32-log: removes the `/SD/nfc/.mfkey32.log` file from flipper to create clean captures using `Detect Reader`
- bkp-user-dict: Creates a backup of the `mf_classic_dict_user.nfc` file named `mf_classic_dict_user.nfc.bkp` (/SD/nfc/assets/mf_classic_dict_user.nfc.bkp)
- rm-dict-user: Removes the `/SD/nfc/assets/mf_classic_dict_user.nfc` file from flipper