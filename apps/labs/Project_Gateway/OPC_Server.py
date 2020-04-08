
import random
from opcua import Server
import time
server = Server()

server.set_endpoint("opc.tcp://10.0.0.57:4048")

server.register_namespace("Room1")

object = server.get_objects_node()

cabin_parameters = object.add_object('ns = 2; s ="SS1"', "Electrical_Cabin")
Temperature = cabin_parameters.add_variable('ns=2; s="Cabin_Temperature"', "Temperature", 0)
Humidity = cabin_parameters.add_variable('ns=2; s="Room_Humidity"', "Humidity", 0)
MagneticFlux = cabin_parameters.add_variable('ns=2; s="Magnetic_Flux"', "Magnetic Flux", 0)

Temperature.set_writable()
Humidity.set_writable()

pit_parameters = object.add_object('ns = 3; s ="SS2"', "Electrical_Pit")
pit_parameters.add_variable('ns=3; s="Salt_Level"', "SaltLevel", 0)
pit_parameters.add_variable('ns=3; s="Rod_Resistence"', "Resistance", 0)

try:
    print("Start Server")
    server.start()
    print("Server Online")
    
finally:
    print("ok")
