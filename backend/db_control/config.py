from dotenv import load_dotenv

load_dotenv()

import os

PORT = os.getenv('PORT')
DB_USER = os.getenv('DB_USER')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')
DATABASE = os.getenv('DATABASE')
