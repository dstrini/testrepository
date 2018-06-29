import uplink
import time
import sys
import requests

print("Hello")

r = requests.get('http://www.hobbes.nmsu.edu')
print(r)
var = uplink.dumps
for _ in range(1, 10):
    time.sleep(0.4)
    print('.', end='')
    sys.stdout.flush()
    print()


def add_test():
    pass
