import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
import sys
import os
from dotenv import load_dotenv; load_dotenv()  # auto load .env

url = 'postgresql://{user}:{passwd}@{host}:{port}/{db}'.format(
    user=os.getenv("USERNAME"),
    passwd=os.getenv("PASS"),
    host=os.getenv("HOST"),
    port=os.getenv("PORT"),
    db=os.getenv("DB")
)

class Database():
    try:
        engine = db.create_engine(url)
        session = sessionmaker(bind= engine)()
        print("Hura!!!Successfully connect to database...")
    except Exception:
        print("Connection fail. Please, modify parameters in .env to connect database")
        sys.exit(1)
