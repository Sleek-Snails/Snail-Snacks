# import time

# # Running Math puzzles is now as easy as just import puzzle1-3 (soon to removet these files)
import puzzles.MathPuzzle  # noqa: F401

# import puzzles.Math.puzzle2
# import puzzles.Math.puzzle3
# from puzzles.MultipleChoicePuzzle import MultipleChoicePuzzle
# # from puzzles.Puzzle import Puzzle
# from pynput import keyboard
# from rich.live import Live
# from rich.text import Text

# from rich.color import Color #noqa: F401
# from rich.style import Style #noqa: F401


# text = Text("Hello World!")
# print(text)
# with Live(text, auto_refresh=False) as live:
# def on_press(key: keyboard) -> None:
#     """Event handler for keyboard on_press event"""
#     try:
#         # print('alphanumeric key {0} pressed'.format(
#         #     key.char))
#         t = Text(f"Key pressed down: {key.char}")
#         live.update(t, refresh=True)
#     except AttributeError:
#         t = Text(f"Key pressed down: {key}")
#         live.update(t, refresh=True)
#         # print('special key {0} pressed'.format(
#         #     key))

# def on_release(key: keyboard) -> bool:
#     """Event handler for keyboard on_release event"""
#     # print('{0} released'.format(
#     #     key))
#     t = Text(f"Key pressed up: {key.char}")
#     live.update(t, refresh=True)
#     if key == keyboard.Key.esc:
#         # Stop listener
#         quit()
#         return False

# listener = keyboard.Listener(
#     on_press=on_press,
#     on_release=on_release,
#     suppress=True)
# listener.start()


# while True:
#   time.sleep(1)
