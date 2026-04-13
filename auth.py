from db import supabase
import uuid

def signup(username, password):
    user_id = str(uuid.uuid4())

    user = {
        "id": user_id,
        "username": username,
        "password": password
    }

    supabase.table("users").insert(user).execute()
    return user_id


def login(username, password):
    response = supabase.table("users").select("*").eq("username", username).eq("password", password).execute()

    if response.data:
        return response.data[0]
    return None
