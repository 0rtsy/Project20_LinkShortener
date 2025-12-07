import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
	secret_key: str = os.getenv("SECRET_KEY")
	algorithm: str = os.getenv("ALGORITHM", "HS256")
	database_url: str = os.getenv("DATABASE_URL", "sqlite:///Base.db")

settings = Settings()
