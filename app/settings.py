import os
from dotenv import load_dotenv

load_dotenv()

SENDER = os.getenv("EMAIL_ADDRESS")
PASSWORD = os.getenv("PASSWORD")
RECEIVER = os.getenv("RECEIVER")
INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")
