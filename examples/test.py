from rtkmcb import mcb
import time

mcb.speed(50)
time.sleep(0.5)
mcb.speed(-50)
time.sleep(0.5)
mcb.speed(10,-10)
time.sleep(0.5)
mcb.speed(-10,10)
time.sleep(0.5)
mcb.speed(100)
time.sleep(0.5)
mcb.speed(-100)
time.sleep(0.5)
mcb.speed(-100,100)
time.sleep(0.5)
mcb.speed(100,-100)
time.sleep(0.5)
