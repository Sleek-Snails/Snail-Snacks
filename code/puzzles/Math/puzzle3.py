from random import randint

from pynput import keyboard
from rich import print
from rich.console import RenderGroup
from rich.panel import Panel

# from rich.prompt import Prompt


num1 = randint(0, 10)
num2 = randint(0, 10)
num3 = randint(0, 10)
num4 = randint(1, 2)
ans = num1-num2
wro = num1-num3

if num4 == 1:
    panel_group = RenderGroup(
        Panel(f"What is {num1} - {num2}?"),
        Panel(f"A - {ans}", style="on blue"),
        Panel(f"B - {wro}", style="on red")
    )

if num4 == 2:
    panel_group = RenderGroup(
        Panel(f"What is {num1} - {num2}?"),
        Panel(f"A - {wro}", style="on blue"),
        Panel(f"B - {ans}", style="on red")

    )

print(Panel(panel_group))


def on_press(key: keyboard) -> None:
    """Event handler for keyboard on_press event"""
    pass


def on_release(key: keyboard) -> bool:
    """Event handler for keyboard on_release event"""
    if 'char' in dir(key):  # check if char method exists,
        if num4 == 1:
            if key.char == 'a':
                return False

            if key.char == 'b':
                print("Wrong!")

        if num4 == 2:
            if key.char == 'a':
                print("Wrong!")

            if key.char == 'b':
                return False


# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# # ...or, in a non-blocking fashion:
# listener = keyboard.Listener(
#     on_press=on_press,
#     on_release=on_release)
# listener.start()
