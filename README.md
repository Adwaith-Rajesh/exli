# Exli

[![GitHub](https://img.shields.io/github/license/Adwaith-Rajesh/exli?style=for-the-badge)](LICENSE)
[![PyPI](https://img.shields.io/pypi/v/exli?style=for-the-badge)](https://pypi.org/project/exli/)

An alias manager and an infinitely extensible CLI.

## Installation

```commandline
pip3 install exli
```

### Exli as an Alias Manager.

#### Why ?

IDK.,

I don't like writing a ton of aliases in my `.bashrc` even though I've only like 5 of them. I just wanted a place for all my aliases that are non important (non-important in the sense that, you don't mind writing two more character in front of the real alias, and for small ones that you don't happen
to use that often)

And also its a lot of fun to write something like this, It's small, It's simple and easy to use.

#### How ?

In order to add new aliases you can run the following command in ur terminal

```commandline
exli add alias cmd

# OR

xi add alias cmd
```

##### Example

Let's say I want to add a small alias that tells me the current weather in my area.

```commandline
xi add weather curl wttr.in
```

And I can invoke the alias using the following

```commandline
xi weather
```

> You cannot name your alias, `add`, `help`, `ls`. or `rm` as these are reserved and are used by exli.

### Some other commands

- List all the available aliases

  ```commandline
  xi ls
  ```

- Remove aliases

  ```commandline
  xi rm alias1 alias2
  ```

- Get help
  ```commandline
   xi help
  ```

### Exli as an Extensible CLI

#### Why ?

You might have one day decided to write a simple CLI tool but you don't want to access it via the command line with it's own command name. (Maybe its a simple program file that you run ocaasianally in order do to a certain task or something)

#### How ?

As an example we can make simple CLI that greets someone.

> You can write the CLI in any language or in any framework.

```python
# ~/exli-extensions/greet.py

import sys

def main() -> int:
    print(f"Hello {' '.join(sys.argv[1:])}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

```

I also have a venv in the `~/exli-extensions` dir.

Now I can add this to exli like so.

```commandline
xi add greet ~/exli-extensions/env/bin/python3 ~/exli-extensions/greet.py
```

Now I can invoke the greet command like this.

```commandline
xi greet Adwaith Rajesh
```

```
Hello Adwaith Rajesh
```

So as you can see you can add as many CLI extensions as you want, you can make it as complex as you want.
