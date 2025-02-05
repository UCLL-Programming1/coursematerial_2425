# Shell

A [shell](https://en.wikipedia.org/wiki/Shell_(computing)) is a piece of software that allows us to communicate with the operating system.
For example, on Windows, the desktop, the taskbar and File Explorer all are part of Windows's shell.

However, there's also the command line interface.
This is a text-based way of interacting with your OS.
For example, instead of using File Explorer to view your files, you use the `ls` command.

![Command Line Interface](shell.png)

From now on, when we talk about the shell (or the terminal), we mean this command line interface.


## Launching the Shell

Visual Studio Code allows you to run the shell inside it:

* Open the Terminal menu.
* Select New Terminal.

Make sure to select the right shell.
You can control which shell is created using the little arrow next to the + button.

![Shell Selection](shell-selection.png)


## Python Shell

Python has a shell of its own.
It allows you to type in Python commands, which are then executed on the spot.

You can launch the Python shell from the "regular" shell using `py`, `python` or `python3`, depending on your OS.

```python
$ py
Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>

```



### IMPORTANT
The OS shell and the Python shell are two completely different beasts.
Do not confuse the two!

For example `ls` is an OS shell command that shows the contents of the current directory:

```bash
$ ls
file_one.txt    python_script.py
```

Typing that same command into a Python shell will result in an error, because Python doesn't recognize that command:

```python
>>> ls
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ls' is not defined
```

On the other `print` is a Python built-in function that works great in a Python shell:
```python
>>> print("Hello World!")
Hello World!
```

Typing it in an OS shell however will also result in an error:
```bash
$ print("Hello World!")
zsh: unknown file attribute: H
```
(The exact error can be slightly different depending on the system you're using)
