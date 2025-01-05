import re, random, os, json

USERS_PATH = "data/users.json"

def validate_nip(nip: str) -> bool:
    """Validate user's NIP"""
    length = 10
    if len(nip) != length:
        return False
    control_digit = int(nip[length - 1])
    wages = [6, 5, 7, 2, 3, 4, 5, 6, 7]
    nip = [int(num) for num in nip]
    result = (sum([nip[i] * wages[i] for i in range(length - 1)])) % 11
    return True if result == control_digit else False
    
def validate_pesel(pesel: str) -> bool:
    """Validate user's PESEL"""
    length = 11
    if len(pesel) != length:
        return False
    control_digit = int(pesel[length - 1])
    wages = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    pesel = [int(num) for num in pesel]
    result = 0
    for i in range(length - 1):
        product = pesel[i] * wages[i]
        if product < 10:
            result += product
        else:
            result += (product % 10)
    if result < 10:
        result = 10 - result
    else:
        result = 10 - (result % 10)
    return True if result == control_digit else False


def validate_regon(regon: str) -> bool:
    """Validate user's REGON"""
    length = len(regon)
    if length not in {9, 14}:
        return False
    control_digit = int(regon[length - 1])
    regon = [int(num) for num in regon]
    match length:
        case 9:
            wages = [8, 9, 2, 3, 4, 5, 6, 7]
        case 14:
            wages = [2, 4, 8, 5, 0, 9, 7, 3, 6, 1, 2, 4, 8]
    result = (sum([regon[i] * wages[i] for i in range(length - 1)])) % 11
    if result % 10 == 0:
        result = 0
    return True if result == control_digit else False

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