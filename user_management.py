import re, random, os, json

USERS_PATH = "data/users.json"

def load_users():
    """Load users data from users.json"""
    if not os.path.exists(USERS_PATH):
        return []
    with open(USERS_PATH, 'r') as file:
        data = json.load(file)
        return data
    
def add_user(user_data):
    """Add new user"""
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

# user = {"user_name": "Kacper", "user_surname": "Zielinski", "user_pesel": "04211507457", "user_nip": "0224111111", "user_regon": "380186266", "user_id": 43}