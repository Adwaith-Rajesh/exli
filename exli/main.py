import argparse
import os
import sys
from typing import Optional
from typing import Sequence

from ._cmd_utils import create_cache_dir_if_not_exist
from ._cmd_utils import get_cmd
from ._const import CACHE_DIR


create_cache_dir_if_not_exist(CACHE_DIR)


def main(argv: Optional[Sequence[str]] = None) -> int:

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(
        "cmd", type=str, help="The name of the command to be executed.")

    args, rest = parser.parse_known_args(argv)

    # the ls, add command is reserved
    if args.cmd == "ls":
        pass

    elif args.cmd == "add":
        pass

    elif args.cmd == "--help":
        pass

    else:
        cmd = get_cmd(args.cmd)

        if cmd:
            split_cmd = cmd.split(" ") + rest
            return os.execvp(split_cmd[0], split_cmd)

        else:
            print("The alias does not exist", file=sys.stderr)
            print("use 'exli ls' to list all the available aliases.")
            return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
