import os
from app.main import APP_VERSION

def get_db_status():
    if os.getenv("APP_ENV") != "production":
        return "inactive"
    db_url = os.getenv("DB_URL_PROD")
    return "connected" if db_url else "disconnected"
