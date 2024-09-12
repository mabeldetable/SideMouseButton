from pynput.mouse import Listener, Button
from pynput.keyboard import Controller, Key

# Define the button number for mouse button x1
BUTTON_X1 = Button.x1

def on_click(x, y, button, pressed):
    if button == BUTTON_X1 and pressed:
        # Simulate CTRL+V key press
        keyboard = Controller()
        keyboard.press(Key.ctrl)
        keyboard.press('v')
        keyboard.release('v')
        keyboard.release(Key.ctrl)

with Listener(on_click=on_click) as listener:
    listener.join()
