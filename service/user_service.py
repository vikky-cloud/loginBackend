# service/user_service.py
from dal.user_dal import create_user, find_user_by_email
from werkzeug.security import generate_password_hash, check_password_hash

def register_user(data):
    # Check if user already exists
    user = find_user_by_email(data['email'])
    if user:
        return {"message": "User already exists"}

    # Hash the password
    hashed_password = generate_password_hash(data['password'], method='sha256')

    # Create user in DB
    create_user(data['username'], data['email'], hashed_password)
    
    return {"message": "User registered successfully"}

def login_user(data):
    # Find user by email
    user = find_user_by_email(data['email'])
    if not user or not check_password_hash(user.password, data['password']):
        return {"message": "Invalid credentials", "status": 401}
    
    return {"message": "Login successful", "status": 200}
