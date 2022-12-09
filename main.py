import sched, time
import requests

url = "http://getzcarsell.com"
s = sched.scheduler(time.time, time.sleep)

def ping(sc): 
    requests.get(url)
    print("Requst sent...")
    sc.enter(1500, 1, ping, (sc,))

s.enter(1500, 1, ping, (s,))
s.run() 
