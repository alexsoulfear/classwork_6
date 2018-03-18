import random
import time

loop_limit = 10

while loop_limit > 0:
    print('Hello world!', loop_limit)
    loop_limit -= 1

loop_limit = 0
while loop_limit < 100:
    print('Hello Feb 46th!', loop_limit)
    time.sleep(.5)
    loop_limit += random.randint(0, 5)
