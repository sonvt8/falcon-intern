import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
import sys
import os
from dotenv import load_dotenv; load_dotenv()  # auto load .env

file_exists = os.path.isfile(".env")
if file_exists:
    from config import USER, PASSWD, DB, HOST, PORT
else:
    with open(".env", "a+") as f:
        config_string = f'export USERNAME=yourUSER\n' \
                        f'export PASS=yourPASS\n' \
                        f'export DB=yourHOST\n' \
                        f'export HOST=yourHOST\n' \
                        f'export PORT=yourPORT\n'
        f.write(config_string)
        print("Please fill all configuration parameters in .evn located in your directory to connect database")
        sys.exit(1)

class Database():
    # replace the user, password, hostname and database according to your configuration according to your informationdoc
    url = 'postgresql://{user}:{passwd}@{host}:{port}/{db}'.format(
        user=os.getenv("USERNAME"),
        passwd=os.getenv("PASS"),
        host=os.getenv("HOST"),
        port=os.getenv("PORT"),
        db=os.getenv("DB")
    )
    engine = db.create_engine(url)
    session = sessionmaker(bind= engine)()

    # def __init__(self):
    #     try:
    #         self.connection = self.engine.connect()
    #         print("Hura!!!Successfully connect to database...")
    #     except Exception as e:
    #         print(e)
    #         sys.exit(1)
