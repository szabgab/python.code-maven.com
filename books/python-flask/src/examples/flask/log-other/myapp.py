import logging

def myfunc():
    logger = logging.getLogger("myapp")

    logger.info("info in myapp")
    logger.warning("warn in myapp")


#if __name__ == "__main__":
#    myfunc()
