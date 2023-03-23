import os

# Values to be used during development. Here you might specify the URI of a database sitting on localhost.

# Statement for enabling the development environment

DB_USER = os.environ.get("DB_USER","flask_user")
DB_PASS = os.environ.get("DB_PASS","flask")
#POSTGRES_URL = os.environ.get("POSTGRES_URL","localhost:5433")
INSTANCE_HOST = os.environ.get("INSTANCE_HOST","172.31.32.1")
DB_NAME = os.environ.get("DB_NAME","flaskdb")
DB_PORT = os.environ.get("DB_PORT","5433")

# DB_USER = os.environ.get("DB_USER")
# DB_PASS = os.environ.get("DB_PASS")
# #POSTGRES_URL = os.environ.get("POSTGRES_URL","localhost:5433")
# INSTANCE_HOST = os.environ.get("INSTANCE_HOST")
# DB_NAME = os.environ.get("DB_NAME")
# DB_PORT = os.environ.get("DB_PORT")

DB_URL = 'postgresql://{user}:{pw}@{host}:{port}/{db}'.format(user=DB_USER,pw=DB_PASS,host=INSTANCE_HOST,port =DB_PORT, db=DB_NAME)

SQLALCHEMY_DATABASE_URI = DB_URL





