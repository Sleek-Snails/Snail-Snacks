import time

from pynput import keyboard
from rich.live import Live
from rich.text import Text

# from rich.color import Color #noqa: F401
# from rich.style import Style #noqa: F401

text = Text("Hello World!")
with Live(text, auto_refresh=False) as live:
    def on_press(key: keyboard) -> None:
        """Event handler for keyboard on_press event"""
        try:
            # print('alphanumeric key {0} pressed'.format(
            #     key.char))
            t = Text(f"Key pressed down: {key.char}")
            live.update(t, refresh=True)
        except AttributeError:
            t = Text(f"Key pressed down: {key}")
            live.update(t, refresh=True)
            # print('special key {0} pressed'.format(
            #     key))

    def on_release(key: keyboard) -> bool:
        """Event handler for keyboard on_release event"""
        # print('{0} released'.format(
        #     key))
        t = Text(f"Key pressed up: {key.char}")
        live.update(t, refresh=True)
        if key == keyboard.Key.esc:
            # Stop listener
            return False
            quit()

    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release,
        suppress=True)
    listener.start()

    while True:
        time.sleep(1)
