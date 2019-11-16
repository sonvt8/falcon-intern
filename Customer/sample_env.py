import sys
import os

file_exists = os.path.isfile("../.env")
if file_exists:
    print('Please, modify parameters in .env to connect database')
else:
    with open("../.env", "a+") as f:
        config_string = f'USERNAME=yourUSER\n' \
                        f'PASS=yourPASS\n' \
                        f'DB=yourDB\n' \
                        f'HOST=yourHOST\n' \
                        f'PORT=yourPORT\n'
        f.write(config_string)
        print("Please, modify parameters in .env to connect database")
        sys.exit(1)