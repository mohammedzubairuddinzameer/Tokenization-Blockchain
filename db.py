from supabase import create_client

SUPABASE_URL = "https://egjoebdeyyuqrdcpgtni.supabase.co"
SUPABASE_KEY = "sb_publishable_g6-3rFKDSPeRHnuvNMKvDg_FtbzJB2t"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
