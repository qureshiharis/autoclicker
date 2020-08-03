import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode


delay = 107.343
button = Button.left
start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')

dashboard = 1


class ClickMouse(threading.Thread):


    def __init__(self, delay, button):

        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

        print('The current pointer position is {0}'.format(mouse.position))


    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):

        global dashboard

        while self.program_running:
            while self.running:

                # Move to position
                if dashboard == 0:
                    mouse.position = (761, 214)
                    dashboard = 1
                    print("at analytics")

                # Move to position
                elif dashboard == 1:
                    mouse.position = (303, 214)
                    dashboard = 2
                    print("at dashboard")

                # Move at position
                elif dashboard == 2:
                    mouse.position = (559,214)
                    dashboard = 3
                    print ("at orders")

                # Move at position
                elif dashboard == 3:
                    mouse.position = (1732,214)
                    dashboard = 4
                    print ("clicked icon")

                elif dashboard == 4:
                    mouse.position = (1479, 291)
                    dashboard = 5
                    print ("at profile")

                elif dashboard == 5:
                    mouse.position = (796, 821)
                    dashboard = 6
                    print ("trying capcha")

                elif dashboard == 6:
                    mouse.position = (1451, 821)
                    dashboard = 1
                    print ("reloading")

                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)


mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
