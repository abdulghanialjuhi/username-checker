import os
from dotenv import load_dotenv

load_dotenv()

SENDER = os.getenv("EMAIL_ADDRESS")
PASSWORD = os.getenv("PASSWORD")
RECEIVER = os.getenv("RECEIVER")
