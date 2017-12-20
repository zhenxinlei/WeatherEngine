import gdax
import threading
import queue
import time
from datetime import datetime, timezone
import os.path
import csv

def main():

    levels = 1
    levelsName =['timestamp']

    for i in range(int(levels)):
        lvl=i+1
        levelsName.append('bp'+str(lvl))
        levelsName.append('bs'+str(lvl))
        levelsName.append('bo'+str(lvl))
        levelsName.append('ap'+str(lvl))
        levelsName.append('as'+str(lvl))
        levelsName.append('ao'+str(lvl))

    print(levelsName)

    date= datetime.now(timezone.utc).strftime("%Y_%m_%d")
    file = "../data/BTC-USD_"+date+".csv"
    isFileExisted = os.path.exists(file)

    priceWriter = None

    if isFileExisted == False:
        with open(file,'w') as csv_file:
            priceWriter = csv.DictWriter(csv_file,
                                     fieldnames=levelsName)
            priceWriter.writeheader()
    else:
        with open(file,'a') as csv_file:
            priceWriter = csv.DictWriter(csv_file,
                                     fieldnames=levelsName)
            priceWriter.writeheader()
    '''

    with open(file,'a') as csv_file:
        priceWriter = csv.DictWriter(csv_file,fieldnames=levelsName)
        priceWriter.writeheader()

    '''

    recorder = PriceRecorder()
    thread = threading.Thread(target=recorder.run)
    thread.start()

    csvInCache =[]
    while True:
        try:
            price = recorder.getPrice()
            lvlDict ={'timestamp': price['timestamp']}
            print(price)
            for i in range (levels):
                lvl = i +1

                lvlDict['bp'+str(lvl)]= price['bids'][lvl][0]
                lvlDict['bs'+str(lvl)]= price['bids'][lvl][1]
                lvlDict['bo'+str(lvl)]= price['bids'][lvl][2]

                lvlDict['ap'+str(lvl)]= price['asks'][lvl][0]
                lvlDict['as'+str(lvl)]= price['asks'][lvl][1]
                lvlDict['ao'+str(lvl)]= price['asks'][lvl][2]

            if len(csvInCache) >5:
                with open(file,'a') as csv_file:
                    priceWriter = csv.DictWriter(csv_file,
                                     fieldnames=levelsName)
                    priceWriter.writerows(row for row in csvInCache)
                    csv_file.close()
                csvInCache=[]
            else:
                csvInCache.append(lvlDict)

        except:
            print("error")

        time.sleep(1)



class PriceRecorder():
    #self.price_queue = queue.Queue()
    def __init__(self):
        self.price_queue = queue.Queue()

    def run(self):
        public_client = gdax.PublicClient()

        while True:

            response = public_client.get_product_order_book("BTC-USD",level=2)
            ts=time.time()
            response['timestamp']=ts
            if 'message' in response:
                if response['message']=='Rate limit exceeded':
                    print('limit exce')
                    continue
            self.price_queue.put(response)
            time.sleep(1)



    def getPrice(self):
        return self.price_queue.get()

main()