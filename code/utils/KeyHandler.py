import threading
from typing import Callable

import blessed


class AsyncKeyHandler(threading.Thread):
    """
    Non-Blocking KeyPress Handler

    Callback should return True to stop KeyHandler
    """

    def __init__(self, callback: Callable):
        super(AsyncKeyHandler, self).__init__()
        self.callback = callback
        self.term = blessed.Terminal()
        self._stop_event = threading.Event()

    def run(self) -> bool:
        """Keypress Handler Logic (Required to be named Run by threading.Thread)"""
        while not self._stop_event.is_set():
            with self.term.cbreak():
                val = ''
                while val.lower() != 'q':
                    val = self.term.inkey(timeout=3)
                    if val.is_sequence:
                        if self.callback(str(val.name)):
                            self._stop_event.set()
                            return False
                    elif val:
                        if self.callback(str(val)):
                            self._stop_event.set()
                            return False

    def stop(self) -> None:  # , timeout):
        """Stop Keypress Handler"""
        self._stop_event.set()
        # self.join(timeout)


class BlockingKeyHandler:
    """
    Blocking KeyPress Handler

    Callback should return True to stop KeyHandler
    """

    def __init__(self, callback: Callable):
        self.callback = callback
        self.pause = False
        self.term = blessed.Terminal()

    def _process(self) -> bool:
        while not self.pause:
            with self.term.cbreak():
                val = ''
                while val.lower() != 'q':
                    val = self.term.inkey(timeout=3)
                    if val.is_sequence:
                        if self.callback(str(val.name)):
                            self.pause = True
                            return False
                    elif val:
                        if self.callback(str(val)):
                            self.pause = True
                            return False
                self.pause = True
                return False

    def start(self) -> bool:
        """Start KeyPress Handler"""
        self.pause = False
        return self._process()

    def stop(self) -> None:
        """Stop KeyPress Handler"""
        self.pause = True


if __name__ == "__main__":
    def testCallback(key: str) -> None:
        """Test Callback"""
        print(key)

    BlockingKeyHandler(testCallback).start()
