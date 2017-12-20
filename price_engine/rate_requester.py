import gdax
import time


'''



wsClient= gdax.WebsocketClient(products="BTC-USD")

wsClient.start()
print(wsClient.url, wsClient.products)
#wsClient.message_count < 500
time.sleep(5000)

#while (wsClient.message_count < 500):
 #   print ("\nmessage_count =", "{} \n".format(wsClient.message_count))
 #   time.sleep(1)
wsClient.close()
'''

import sys
import gdax
public_client = gdax.PublicClient()
count = 0

tbid=0
task=0
while (count<500):
    response = public_client.get_product_order_book("BTC-USD",level=2)
    bids = response['bids']
    asks = response ['asks']
    len = 1


    for i in range(len):
        bidq = float(bids[i][1])
        askq = float(asks[i][1])
        rbid = float(bids[i][0])
        rask = float(asks[i][0])
        if tbid!=rbid and task!=rask:
            print("----> bid ask change <-----")
            tbid = rbid
            task = rask
        elif tbid!=rbid:
            print("----> bid  change <-----")
            tbid = rbid
        elif task!=rask:
            print("----> ask  change <-----")
            task = rask

        if task-tbid > 0.5:
            print("SGNAL")

        print(bids[i][0] ,",", '%.4f'% bidq ,"|| ",'%.4f'% askq ,", ", asks[i][0])
    #print("========")
    time.sleep(1)

