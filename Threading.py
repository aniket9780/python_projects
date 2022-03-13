from threading import *
from time import sleep


def new():
    
    for i in range(10):
        print("EXECUTING.....", current_thread().getName())
        sleep(1)
        
        
t1 = Thread(target=new)
t1.start()
t1.join()
print("Done....", current_thread().getName())

