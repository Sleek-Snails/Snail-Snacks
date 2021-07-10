from typing import Callable

from pynput import keyboard


class KeyHandler:
    """Class for handling keypresses"""

    def __init__(self, checkFunc: Callable[[], str]):
        # Collect events until released
        self.checkFunc = checkFunc
        self.listener = keyboard.Listener(on_press=self.on_press,
                                          on_release=self.on_release,
                                          suppress=True)

    def on_press(self, key: keyboard) -> None:
        """Event handler for keyboard on_press event"""
        pass

    def on_release(self, key: keyboard) -> bool:
        """Event handler for keyboard on_release event"""
        if 'char' in dir(key):
            if key.char == 'q':
                self.disable()
            else:
                return self.checkFunc(key.char)

    def enable(self) -> None:
        """Start keyboard listener"""
        with self.listener:
            self.listener.join()

    def disable(self) -> None:
        """Stop Keypress listener"""
        self.listener.stop()
