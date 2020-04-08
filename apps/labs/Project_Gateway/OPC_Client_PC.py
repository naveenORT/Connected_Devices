'''
Created on Apr 2, 2020
@author: Naveen Rajendran
'''
import time
from opcua import Client


class SubHandler(object):

    """
    Subscription Handler. To receive events from server for a subscription
    data_change and event methods are called directly from receiving thread.
    Do not do expensive, slow or network operation there. Create another 
    thread if you need to do such a thing
    """

    def datachange_notification(self, node, val, data):
        print("Python: New data change event", node, val)

    def event_notification(self, event):
        print("Python: New event", event)


opc_client = Client("opc.tcp://10.0.0.57:4048")
opc_client.connect()

temp_value = opc_client.get_node('ns=2; s="Cabin_Temperature"')
hum_value = opc_client.get_node('ns=2; s="Room_Humidity"')

while(1):
    time.sleep(5)
    handler = SubHandler()
    sub = opc_client.create_subscription(500, handler)
    handle = sub.subscribe_data_change(hum_value)

   # print(temp_value.get_value())
