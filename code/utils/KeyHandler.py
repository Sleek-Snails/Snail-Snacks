from typing import Callable

from pynput import keyboard


class KeyHandler:
    """Class for handling keypresses"""

    def __init__(self, checkFunc: Callable[[], str]):
        # Collect events until released
        self.checkFunc = checkFunc

    def on_press(self, key: keyboard) -> None:
        """Event handler for keyboard on_press event"""
        pass

    def on_release(self, key: keyboard) -> bool:
        """Event handler for keyboard on_release event"""
        if 'char' in dir(key):
            print(key.char)
            return self.checkFunc(key.char)

    def enable(self) -> None:
        """Start keyboard listener"""
        with keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            listener.join()

        # if 'char' in dir(key):  # check if char method exists,
        #     if num4 == 1:
        #         if key.char == 'a':
        #             return False

        #         if key.char == 'b':
        #             print("Wrong!")

        #     if num4 == 2:
        #         if key.char == 'a':
        #             print("Wrong!")

        #         if key.char == 'b':
        #             return False
