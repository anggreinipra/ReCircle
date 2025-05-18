from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def sync_to_supabase(table, data):
    try:
        response = supabase.table(table).insert(data).execute()
        if response.status_code == 201:
            print(f"Data synced to Supabase: {data}")
        else:
            print(f"Error syncing data to Supabase: {response.data}")
    except Exception as e:
        print(f"Error syncing to Supabase: {e}")