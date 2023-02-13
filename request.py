import zmq

context = zmq.Context()

#  Socket to talk to server
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:7777")
print("Sending units to be converted...")

# Example data from user input
request = [150, 70]
socket.send_json(request)

#  Get the reply.
print("Awaiting response...")

result = socket.recv_json()

print("Response received")
print(result)