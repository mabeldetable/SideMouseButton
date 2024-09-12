from pynput.mouse import Listener, Button
from pynput.keyboard import Controller, Key

# Define the button number for mouse button x1
BUTTON_X2 = Button.x2

def on_click(x, y, button, pressed):
    if button == BUTTON_X2 and pressed:
        # Simulate CTRL+C key press
        keyboard = Controller()
        keyboard.press(Key.ctrl)
        keyboard.press('c')
        keyboard.release('c')
        keyboard.release(Key.ctrl)

with Listener(on_click=on_click) as listener:
    listener.join()
