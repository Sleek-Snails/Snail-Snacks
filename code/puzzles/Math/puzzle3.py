from random import randint
num1 = randint(0,10)
num2 = randint(0,10)
num3 = randint(0,10)
num4 = randint(1,2)
ans = num1-num2
wro = num1-num3
from rich import print
from rich.prompt import Prompt
from rich.console import RenderGroup
from rich.panel import Panel
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
from pynput import keyboard

def on_press(key):
    pass

def on_release(key):
    #Add your code to stop motor
    if key == keyboard.Key.esc:
        # Stop listener
        # Stop the Robot Code
        return False
    if 'char' in dir(key):   #check if char method exists,
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

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()