# Unit Conversion Microservice
 Converts Enlish to SI units for weight and height

# REQUESTING DATA:

Data requests need to made using ZeroMQ as the pipeline. This needs to be installed on the local machine making the data request. A current copy of the microservice py file needs to be contained on the local machine as well. Users will make a call to this service using the format below. The request needs to use TCP 7777 as that is what the server will be monitoring. Users also need to provide weight and height, in English units, in a list example [150, 70] to the service. This needs to be sent as json in order for the microservice to interpret the data properly.

context = zmq.Context()

#Socket to talk to server

socket = context.socket(zmq.REQ)

socket.connect("tcp://localhost:7777")

print("Sending units to be converted...")


#Example data from user input:  [weight, height[]]

request = [150, 70]

socket.send_json(request)


# RECEIVING DATA:

The results for the microservice request will also be sent back to the user using ZeroMQ. This will come in a json format so the user will need to anticipate that as the response type. The user can expect the results in a list just as input in this format [weight, height]. The results will be converted into metric units. Note the format used to receive data below.

#Get the reply.

print("Awaiting response...")

result = socket.recv_json()


![image](https://user-images.githubusercontent.com/38335751/218407822-dde9737f-6000-4b90-b0eb-d9f54852f2c3.png)
