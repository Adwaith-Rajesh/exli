import argparse
import os
import sys
from typing import Optional
from typing import Sequence

from ._cmd_utils import create_cache_dir_if_not_exist
from ._cmd_utils import dump_app_cache
from ._cmd_utils import get_cmd
from ._cmd_utils import load_app_cache
from ._const import CACHE_DIR
from ._const import RESERVED_CMDS


create_cache_dir_if_not_exist(CACHE_DIR)


def main(argv: Optional[Sequence[str]] = None) -> int:

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(
        "cmd", type=str, help="The name of the command to be executed.")

    args, rest = parser.parse_known_args(argv)

    # the ls, add, rm, and help commands are reserved
    if args.cmd == "ls":
        cmd_dicts = load_app_cache()
        print(", ".join(list(cmd_dicts)))
        return 0

    elif args.cmd == "add":
        if rest:
            if rest[0] == "--help":
                print("Usage: exli add <alias> <cmd>")
                return 0

        if len(rest) < 2:
            print(
                f"exli add requires two arguments found {len(rest)!r}", file=sys.stderr)
            return 1

        else:

            if rest[0] in RESERVED_CMDS:
                print(f"{rest[0]!r} is a reserved command.", file=sys.stderr)
                return 1

            curr_cmd = load_app_cache()
            curr_cmd[rest[0]] = ' '.join(rest[1:])
            dump_app_cache(curr_cmd)
            print(f"{' '.join(rest[1:])!r} aliased to {rest[0]!r}")
            return 0

    elif args.cmd == "rm":
        curr_cmd = load_app_cache()
        for c in rest:
            if c in curr_cmd:
                print(f"Removed alias {c!r}")
                del curr_cmd[c]

        dump_app_cache(curr_cmd)
        return 0

    elif args.cmd == "help":
        parser.print_help()
        return 0

    else:
        cmd = get_cmd(args.cmd)

        if cmd:
            split_cmd = cmd.split(" ") + rest
            # the alias cmd execution happened here
            return os.execvp(split_cmd[0], split_cmd)

        else:
            print("The alias does not exist", file=sys.stderr)
            print("use 'exli ls' to list all the available aliases.", file=sys.stderr)
            return 1


if __name__ == "__main__":
    raise SystemExit(main())
