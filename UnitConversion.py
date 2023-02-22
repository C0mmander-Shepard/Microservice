
import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:7777")

while True:
    user_data = socket.recv_json()
    print("Request received")

    #convert lbs to kg
    user_data[0] = user_data[0] * 0.45359237

    user_data[1] = user_data[1] * 2.54

    print(user_data)

    time.sleep(1)
    print("Sending response...")

    socket.send_json(user_data)