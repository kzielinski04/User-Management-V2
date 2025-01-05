import re, random, os, json

USERS_PATH = "data/users.json"

def validate_nip(nip: str) -> bool:
    """Validate user's NIP"""
    pass

def validate_pesel(pesel: str) -> bool:
    """Validate user's PESEL"""
    pass

def validate_regon(regon: str) -> bool:
    """Validate user's REGON"""
    pass

def load_users():
    """Load users data from users.json"""
    if not os.path.exists(USERS_PATH):
        return []
    with open(USERS_PATH, 'r') as file:
        data = json.load(file)
        return data
    
def add_user(user_data: dict):
    """Add new user to users.json"""
    user_id = generate_user_id()
    user_data.update({"user_id": user_id})
    data = load_users()
    data.append(user_data)
    with open(USERS_PATH, 'w') as file:
        json.dump(data, file, indent = 4)

def generate_user_id() -> int:
    """Generate unique ID for the user"""
    if not os.path.exists(USERS_PATH):
        return 1
    data = load_users()
    max_id = max([user["user_id"] for user in data])
    return max_id + 1

def edit_user(user_id: int, updated_data: dict):
    """Edit data of the user from users.json"""
    data = load_users()
    if user_id not in [user["user_id"] for user in data]:
        raise Exception("User not found!")
    for user in data:
        if user["user_id"] == user_id:
            user.update(updated_data)
    with open(USERS_PATH, 'w') as file:
        json.dump(data, file, indent = 4)

def remove_user(user_id: int):
    """Remove user's data from users.json"""
    data = load_users()
    updated_data = [user for user in data if user["user_id"] != user_id]
    if len(data) != len(updated_data):
        with open(USERS_PATH, 'w') as file:
            json.dump(updated_data, file, indent = 4)
    else:
        raise Exception("User not found!")

# user = {"user_name": "Wiesiek", "user_surname": "Kałdunow", "user_pesel": "042121507457", "user_nip": "0221111114111111", "user_regon": "38ssss0186266"}