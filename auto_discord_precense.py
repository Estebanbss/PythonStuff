import time
from pypresence import Presence

client_id = '1065492597843427418'
RPC = Presence(client_id)
RPC.connect()

list = ["a ","b ","c ","d ","e ","f ","g ","h ","i ","j ","k ","l ","m ","n ","o ","p ","q ","r ","s ","t ","u ","v ","w ","x ","y ","z "]
now = 0

while True:
    print("Updating presence with state:", list[now])
    RPC.update(state=list[now], details="esto lo hice con codigo python 🙂", start=int(time.time()))
    time.sleep(15)
    now += 1
    if now == len(list):
        now = 0

RPC.close()

