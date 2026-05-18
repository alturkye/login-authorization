# Login Authorization Microservice

## Description
This microservice is an authentication service built using Python and ZeroMQ. 
It provides three main functionalities: user registration, login verification, and password reset. User data is stored in an in-memory dictionary, where each username maps to a record containing a password and birth date. 
The service communicates using JSON messages over a ZeroMQ REP socket, where each request includes a context field that determines the operation being performed.

## Communication Contract 

### How to REQUEST data
Requests should be made using a ZeroMQ REQ socket
* PORT: 5556
* FORMAT: JSON object 

* Example call * <br> 
import zmq <br> 
context = zmq.Context() <br> 
socket = context.socket(zmq.REQ) <br> 
socket.connect("tcp://localhost:5556") <br> 

socket.send_json({"username": "Owenbadz", "password": "123456", "context": "login"}) <br> 
socket.send_json({"username": "Owenbadz", "password": "123456", "birth_date": "08/31/2005", "context": "register"}) <br> 
socket.send_json({"username": "Owenbadz", "birth_date": "08/31/2005", "context": "forgot_password"}) <br> 

### How to RECEIVE data 
Once the microservice process the request, it will send a response back through
	the same ZeroMQ pipe 
The service will return a JSON object with a message and the status of the request 

* Example call * <br> 
response = socket.recv_json() <br> 

if response["status"] == True: <br> 
	print(response['message']) <br> 
else: <br> 
	print(f"Error: {response['message']}") <br> 
