import os

# the cache dir for exli set by the user
USER_CACHE_DIR = os.environ.get("EXLI_CACHE_DIR", None)

CACHE_DIR = USER_CACHE_DIR or os.path.join(
    os.path.expanduser("~"), ".cache", "exli")

RESERVED_CMDS = [
    "help",
    "rm",
    "ls",
    "add"
]
