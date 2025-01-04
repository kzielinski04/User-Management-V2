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

# user = {"name": "Kacper", "surname": "Zielinski", "pesel": "04211507457", "nip": "0224111111", "regon": "380186266"}