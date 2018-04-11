import hid
import os
import random
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
    swift_videos = [
        "https://www.youtube.com/watch?v=tCXGJQYZ9JA",
        "https://www.youtube.com/watch?v=3tmd-ClpJxA",
        "https://www.youtube.com/watch?v=e-ORhEE9VVg",
        "https://www.youtube.com/watch?v=nfWlot6h_JM",
    ]
    cmd = 'open "%s"' % random.choice(swift_videos)
    os.system(cmd)


leader_pressed = False


def set_leader():
    global leader_pressed
    leader_pressed = True


dance_map = {
    'up': [set_leader],
    'up_left': [',c'],
    'down_left': [',t'],
    'start': ['q', False, 'using {command down, control down}'],
    'down_right': [open_swifty],
}

leader_map = {
    'right': ['q', False, 'using {command down, control down}'],
}


def send_keys(keys, enter=False, options=""):
    if callable(keys):
        keys()
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
    global leader_pressed
    while True:
        data = device.read(64)
        if data:
            button = button_lookup.get(tuple(data))
            if button in dance_map or button in leader_map:
                print(button)
                if not leader_pressed:
                    send_keys(*dance_map[button])
                elif button in leader_map:
                    send_keys(*leader_map[button])
                    leader_pressed = False
            else:
                print data
        else:
            time.sleep(0.05)


try:
    device = start_device()
    main(device)
except IOError as ex:
    print(ex)
    print("You probably don't have the hard coded device.")
