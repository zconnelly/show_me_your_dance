import hid
import os
import time

buttons = {
    'up': [4, 0, 128, 0],
    'right': [8, 0, 255, 128],
    'left': [1, 0, 0, 128],
    'down': [2, 0, 128, 255],
    'up_right': [128, 0, 128, 128],
    'down_right': [32, 0, 128, 128],
    'down_left': [16, 0, 128, 128],
    'up_left': [64, 0, 128, 128],
    'select': [0, 2, 128, 128],
    'start': [0, 1, 128, 128],
    'release': [0, 0, 128, 128],
}

button_lookup = {tuple(value): key for key, value in buttons.iteritems()}


def open_swifty():
    cmd = 'open "https://www.youtube.com/watch?v=tCXGJQYZ9JA"'
    os.system(cmd)


dance_map = {
    'up': ['m'],
    'down_right': [',t'],
    'start': [None, None, None, open_swifty],
}


def send_keys(keys, options="", enter=False, special=None):
    if special:
        special()
        return
    cmd = """
    osascript -e 'tell application "System Events" to keystroke "%s" %s'
    """ % (keys, options)
    enter_cmd = """
    osascript -e "tell application \"System Events\" to key code 36"
    """
    os.system(cmd)
    if enter:
        os.system(enter_cmd)


def start_device():
    print("Initializing Dance Mat")
    h = hid.device()
    h.open(0x6677, 0x8811)

    # enable non-blocking mode
    h.set_nonblocking(1)

    # write some data to the device
    h.write([0, 63, 35, 35] + [0] * 61)

    # wait
    time.sleep(0.10)
    return h


def main(device):
    print("Reading data in")
    while True:
        data = device.read(64)
        if data:
            button = button_lookup[tuple(data)]
            print(button)
            if button in dance_map:
                send_keys(*dance_map[button])
        else:
            time.sleep(0.05)


try:
    device = start_device()
    main(device)
except IOError as ex:
    print(ex)
    print("You probably don't have the hard coded device.")
