import zmq
import json

database = {}

# set up ZeroMQ
context = zmq.Context()
socket = context.socket(zmq.REP) # rep = reply, the listener
socket.bind("tcp://*:5556")

print("Login authorization service is running on port 5556...")
while True:
    message = socket.recv_json()
    if message['context'] == "login":
        if message['username'] in database:
            if message['password'] == database[message['username']]['password']:
                socket.send_json({"status": True, "message": "Login successful" })
            else:
                socket.send_json({"status": False, "message": "Wrong password"})
        else:
            socket.send_json({"status": False, "message": "wrong username"})
    elif message['context'] == "register":
        username = message['username']
        password = message['password']
        birth_date = message['birth_date']
        database[username] = {"password": password, "birth_date": birth_date}
        socket.send_json({"status": True, "message": "successfully registered with username and password"})
    elif message['context'] == "forgot_password":

        username = message['username']
        answer = message['birth_date'] # using birthdate to verify the user
        new_password = message['new_password']
        if username in database:
            if database[username]['birth_date'] == answer:
                database[username]['password'] = new_password

                socket.send_json({"status": True, "message": "Password reset successful"})

            else:
                socket.send_json({"status": False, "message": "Security answer incorrect"})

        else:
            socket.send_json({"status": False, "message": "Username not found"})
    else:
        socket.send_json({"status": False, "message": "Not correct context or no context was given"})



