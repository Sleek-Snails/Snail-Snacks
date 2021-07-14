from typing import Callable

import keyboard


class OldKeyHandler:
    """Class for handling keypresses"""

    def __init__(self, checkFunc: Callable[[], str]):
        # Collect events until released
        self.checkFunc = checkFunc
        self.enabled = True
        self.listener = keyboard.Listener(on_press=self.on_press,
                                          on_release=self.on_release,
                                          suppress=True)

    def on_press(self, key: keyboard) -> None:
        """Event handler for keyboard on_press event"""
        print(f"key down: {key}")

    def on_release(self, key: keyboard) -> bool:
        """Event handler for keyboard on_release event"""
        if 'char' in dir(key):
            if key.char == 'q':
                self.disable()
                return False
            else:
                if self.enabled:
                    # self.suppress_event()
                    print('hm')
                    return self.checkFunc(key.char)
                else:
                    print("here")
                    return False

    def enable(self) -> None:
        """Start keyboard listener"""
        # self.listener.start()
        with self.listener:
            # while True:
            self.listener.join()
            # t.stop()
            # print("l")

    def disable(self) -> None:
        """Stop Keypress listener"""
        # self.listener.stop()
        self.enabled = False
        self.listener.stop()
        self.listener.wait()
        # print('hhh')

# from pynput import keyboard

# import time
# import keyboard

# class KeyHandler:
#     def __init__(self):
#         self.keyHook = keyboard.hook(callback=self.cb, suppress=True, on_remove=lambda: print("removed"))


#     def cb(self, key):
#         print(f"name: {key.name} | scan_code: {key.scan_code} | time: {key.time}")
#         if key.name == "m":
#             # keyboard._listener.listening = False
#             # keyboard.unhook(self.keyHook)
#             keyboard.unhook_all()
#             # keyboard._listener.remove_handler(self.keyHook)
#             input('test: ')

# KeyHandler()

# while True:
#     time.sleep(0.01)
#     # print('here')
