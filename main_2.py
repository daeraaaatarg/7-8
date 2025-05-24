# логування (smth like try-except)
# DEBUG, INFO, Warning, NameError, Critical
import logging
# default - from warning - so to set from DEBUG:
# filename and filemod - to see it in some file
logging.basicConfig(level=logging.DEBUG, filename="logs.log", filemode="w")
logging.debug("debug")               # nothing default
logging.info("info")                 # nothing default
logging.warning("warner")
logging.error("error")
logging.critical("critical")

print("===================================================")

# тести
#if 2+2 == 4:
#    print("ok")
#assert 2+2 == 5, "wrong"

# to file - "test_2"
def add(a, b)
    return a+b