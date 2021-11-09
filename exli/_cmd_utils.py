import json
import os
from pathlib import Path
from typing import Dict
from typing import Union

from ._const import CACHE_DIR


def create_cache_dir_if_not_exist(path: str) -> None:
    Path(path).mkdir(parents=True, exist_ok=True)

    if len(os.listdir(path)) == 0:
        # the default json file does not exists
        with open(os.path.join(path, "default_cmd.json"), "w") as f:
            f.write("{}")


def verify_json_data(data: object) -> bool:
    """
    Checks whether the data if of the followgin schema:

    {
        "alias_key": "command"
    }

    both must be of type string
    """
    if isinstance(data, dict):
        if all(isinstance(i, str) for i in data) and all(isinstance(i, str) for i in data.values()):
            return True

    return False


def load_app_cache() -> Dict[str, str]:
    """Loads the existing json file stored in the cache dir"""

    with open(os.path.join(CACHE_DIR, "default_cmd.json")) as f:
        try:
            data = json.load(f)
            if verify_json_data(data):
                return data

            else:
                return {}

        except json.decoder.JSONDecodeError:
            return {}


def dump_app_cache(data: Dict[str, str]) -> None:
    """Dumps the given data in to the cache dir as a json file"""
    with open(os.path.join(CACHE_DIR, "default_cmd.json"), 'w') as f:
        if verify_json_data(data):
            json.dump(data, f)


def get_cmd(alias: str) -> Union[str, None]:
    cmds = load_app_cache()
    return cmds.get(alias)


def verify_json_file(filename: str) -> bool:
    """Verifies the externally given json file"""
    pass
