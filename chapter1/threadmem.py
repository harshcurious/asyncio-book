import os
from time import sleep
from threading import Thread

# Couldn't create 10000 threads!!!
threads = [ Thread(target=lambda: sleep(60)) for i in range(0, 5000)]
[t.start() for t in threads]
print(f'PID = {os.getpid()}')
[t.join() for t in threads]
