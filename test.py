import zmq
import json

context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5556")

print("test.py attempting to connect to server...")

#REGISTER TEST
register_data = {
    "context": "register",
    "username": "owen",
    "password": "mypassword123",
    "birth_date": "01/01/2000"
}

print("\nSending register request...")

socket.send_json(register_data)

received = socket.recv_json()

print(f"service.py status: {received['status']}")
print(f"Message: {received['message']}")

#LOGIN TEST
login_data = {
    "context": "login",
    "username": "owen",
    "password": "mypassword123"
}

print("\nSending login request...")

socket.send_json(login_data)

received = socket.recv_json()

print(f"service.py status: {received['status']}")
print(f"Message: {received['message']}")

#FORGOT PASSWORD TEST
forgot_password_data = {
    "context": "forgot_password",
    "username": "owen",
    "birth_date": "01/01/2000",
    "new_password": "newpassword456"
}

print("\nSending forgot password request...")

socket.send_json(forgot_password_data)

received = socket.recv_json()

print(f"service.py status: {received['status']}")
print(f"Message: {received['message']}")

#LOGIN WITH NEW PASSWORD TEST
new_login_data = {
    "context": "login",
    "username": "owen",
    "password": "newpassword456"
}

print("\nSending login request with new password...")

socket.send_json(new_login_data)

received = socket.recv_json()

print(f"service.py status: {received['status']}")
print(f"Message: {received['message']}")

#FALSE LOGIN TEST (WRONG PASSWORD)
wrong_password_data = {
    "context": "login",
    "username": "owen",
    "password": "incorrectpassword"
}

print("\nSending login request with wrong password...")

socket.send_json(wrong_password_data)

received = socket.recv_json()

print(f"service.py status: {received['status']}")
print(f"Message: {received['message']}")

#FALSE LOGIN TEST (WRONG USERNAME)
wrong_username_data = {
    "context": "login",
    "username": "not_a_user",
    "password": "whatever"
}

print("\nSending login request with wrong username...")

socket.send_json(wrong_username_data)

received = socket.recv_json()

print(f"service.py status: {received['status']}")
print(f"Message: {received['message']}")

#FALSE PASSWORD RESET TEST (WRONG BIRTH DATE)
wrong_birthdate_data = {
    "context": "forgot_password",
    "username": "owen",
    "birth_date": "12/31/1999",
    "new_password": "badreset"
}

print("\nSending forgot password request with wrong birth date...")

socket.send_json(wrong_birthdate_data)

received = socket.recv_json()

print(f"service.py status: {received['status']}")
print(f"Message: {received['message']}")

#FALSE PASSWORD RESET TEST (USERNAME NOT FOUND)
missing_user_data = {
    "context": "forgot_password",
    "username": "notauser",
    "birth_date": "01/01/2000",
    "new_password": "newpass"
}

print("\nSending forgot password request with missing username...")

socket.send_json(missing_user_data)

received = socket.recv_json()

print(f"service.py status: {received['status']}")
print(f"Message: {received['message']}")

#INVALID CONTEXT TEST
invalid_context_data = {
    "context": "delete_account",
    "username": "owen"
}

print("\nSending invalid context request...")

socket.send_json(invalid_context_data)

received = socket.recv_json()

print(f"service.py status: {received['status']}")
print(f"Message: {received['message']}")