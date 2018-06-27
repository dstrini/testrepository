import uplink
import time
import sys
import requests

print("Hello")

r = requests.get('http://www.python.org')
print(r)
var = uplink.dumps
for _ in range(1,10):
    time.sleep(10)
    print('.', end='')
    sys.stdout.flush()