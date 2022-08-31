import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "10605524").strip()
API_HASH = os.getenv("API_HASH", "a4ccc51331a895285a4c57ce10d49f95").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "5257644826:AAHUlM4qDhsitRE6O3z0Leg2J96hXj2QMzI").strip()
DATABASE_URL = os.getenv("DATABASE_URL", "postgres://zzlrfwmp:75B5tfrr7ocO6MOsfogvSPn2XmZccKIF@chunee.db.elephantsql.com/zzlrfwmp").strip()
MUST_JOIN = os.getenv("MUST_JOIN", "hiroshisupport")

if not API_ID:
    print("No API_ID found. Exiting...")
    raise SystemExit
if not API_HASH:
    print("No API_HASH found. Exiting...")
    raise SystemExit
if not BOT_TOKEN:
    print("No BOT_TOKEN found. Exiting...")
    raise SystemExit
if not DATABASE_URL:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit

try:
    API_ID = int(API_ID)
except ValueError:
    print("API_ID is not a valid integer. Exiting...")
    raise SystemExit

if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
