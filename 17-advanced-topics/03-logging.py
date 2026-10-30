# --------------------------------------------------
# -- Advanced Lessons => Add logging To Your Code --
# --------------------------------------------------
# - Print Out To Console Or File
# - Print Logs Of What Happens
#-------------------------------
# - DEBUG
# - INFO
# - WARNING
# - ERROR
# - CRITICAL
# ----------
# name => Logging Module Give It To The Default Logger
# ----------------------------------------------------
# Basic Config
# - level => Level of Severity
# - filename => File Name And Extention
# - mode => Mode Of The File a => Append
# - format => Format For The Log Message
# -------------------------
# getLogger => Return a Logger With The Specified Name

import logging

# print(dir(logging))

logging.basicConfig(filename= "my_app.log", filemode = "w", format= )

logging.critical("This Is Critical Message")