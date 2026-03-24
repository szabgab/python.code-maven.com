from wrapper import wrap
import time

@wrap
def myfunc():
    print("myfunc started")
    time.sleep(1)
    print("myfunc ended")

myfunc()

