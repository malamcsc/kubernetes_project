import os

DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
INSTANCE_HOST = os.environ.get("INSTANCE_HOST")
DB_NAME = os.environ.get("DB_NAME")
DB_PORT = os.environ.get("DB_PORT")

DB_URL = 'postgresql://{user}:{pw}@{host}:{port}/{db}'.format(user=DB_USER,pw=DB_PASS,host=INSTANCE_HOST,port =DB_PORT, db=DB_NAME)

SQLALCHEMY_DATABASE_URI = DB_URL





