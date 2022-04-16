from distutils.util import strtobool
from dotenv import load_dotenv
import os

load_dotenv()

PRODUCTION = strtobool(os.getenv("PRODUCTION"))
USE_RAILWAY = strtobool(os.getenv("USE_RAILWAY"))
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Database
POSTGRESQL_URI = os.getenv("POSTGRESQL_URI")