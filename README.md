# `py_fortune`

`py_fortune` is a program that hopes to be close enough to the original [`fortune` for Unix systems](https://en.wikipedia.org/wiki/Fortune_(Unix)).

It reads a random text file from the [`cookies/`](cookies/) directory and prints the file.

## Executing

You can use `py_fortune` by opening it through [Python](https://python.org/). *Latest version of Python used was [`3.11.11`](https://www.python.org/downloads/release/python-31111/).*

### Arguments

#### Read All Cookies : `-a`, `--all`

Reads any cookie from [`cookies`](cookies/), including those that are offensive or hidden.

#### Read Offensive Cookies : `-o`, `--offensive`

Allows reading cookies that are [offensive.](#offensive-cookies)

#### Choose Cookie : `-c`, `--cookie`

> [!IMPORTANT]
> Make sure to put the filetype in the option, like if the file is `hello_world.txt`, make sure to put `... -c hello_world.txt`, and not just `-c hello_world`.

This argument allows you to choose a cookie.

#### Verbose Mode : `-v`, `--verbose`

This argument prints out what the program does descriptively.

## Creating Cookies

### Normal Cookies

You can create cookies by creating a file in the [`cookies/`](cookies/) directory. It can have any name, as long as it doesn't start with `.` or [`o.`](#offensive-cookies)

### Offensive Cookies

You can create offensive cookies by creating a file in the [`cookies/`](cookies/) directory. It must start with `o.` in order to be identified as an offensive cookie.