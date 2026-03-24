from wrapper import wrap
import time

def myfunc():
    print("myfunc started")
    time.sleep(1)
    print("myfunc ended")


myfunc = wrap(myfunc)

myfunc()



