# Logging_Config.py
import logging
from .constants import LOG_FILE, DEBUG_MODE



DEBUG_MODE = True
level = logging.DEBUG if DEBUG_MODE else logging.INFO

logger = logging.getLogger()                                        # "getLogger()" Telling & Setting Rules. Empty means root logger, Default Name of whole Application.
logger.setLevel(level)                                              # "setLevel" Setting Worning Level Rules.

# ---------- File Handler ----------
#file_handler = logging.FileHandler(filename, mode, encoding, delay) 
#filename (required): The name (and path) of the file where the logs will be written. If the file doesn't exist, Python will automatically create it.
#mode (optional): File opening mode. The default is 'a' (append).
#encoding (optional): Used to open the file. The default is None, means the system default encoding is used.
#delay (optional): If set to True, the file is not opened until the first log record is emitted. Useful if the file path not available.
file_handler = logging.FileHandler(LOG_FILE, mode="a")            # "a" = Append, "w" = wipe file every time
file_handler.setLevel(level)

# ---------- Console Handler ----------
console_handler = logging.StreamHandler()
console_handler.setLevel(level)

# ---------- Formatter ----------
formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"                    # "TIME | LEVEL | TEXT"
)

file_handler.setFormatter(formatter)                               # setFormatter(): Used to define how the log record's attributes (message, time, log level, etc.) should be arranged.
console_handler.setFormatter(formatter)                            # formatter: It holds the format of the final logged message. 

# ---------- Attach Handlers ----------

if not logger.handlers:
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

#print("✅ Logging configured")   # DEBUG CONFIRMATION
