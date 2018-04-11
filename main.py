"""
DDR Vim
=======

Find the mat!

```python
#!/usr/bin/python
import sys
import usb.core
# find USB devices
dev = usb.core.find(find_all=True)
# loop through devices, printing vendor and product ids in decimal and hex
for cfg in dev:
  sys.stdout.write(
    'Decimal VendorID=' + str(cfg.idVendor) +
    ' & ProductID=' + str(cfg.idProduct) + '\n')
  sys.stdout.write(
    'Hexadecimal VendorID=' + hex(cfg.idVendor) +
    ' & ProductID=' + hex(cfg.idProduct) + '\n\n')
```

```bash
# list usb devices
ioreg -p IOUSB -w0
```

```text
# the mat
Decimal VendorID=26231 & ProductID=34833
Hexadecimal VendorID=0x6677 & ProductID=0x8811
```

```
# codes
up
[4, 0, 128, 0]
[0, 0, 128, 128]
right
[8, 0, 255, 128]
[0, 0, 128, 128]
left
[1, 0, 0, 128]
[0, 0, 128, 128]
down
[2, 0, 128, 255]
[0, 0, 128, 128]
up right
[128, 0, 128, 128]
[0, 0, 128, 128]
[128, 0, 128, 128]
[0, 0, 128, 128]
down right
[32, 0, 128, 128]
[0, 0, 128, 128]
down left
[16, 0, 128, 128]
[0, 0, 128, 128]
[4, 0, 128, 0]
[0, 0, 128, 128]
[16, 0, 128, 128]
[0, 0, 128, 128]
up left
[64, 0, 128, 128]
[0, 0, 128, 128]
select
[0, 2, 128, 128]
[0, 0, 128, 128]
start[0, 1, 128, 128]
[0, 0, 128, 128]
```
"""
from __future__ import print_function

import hid
import time

# try opening a device, then perform write and read

try:
    print("Opening the device")

    h = hid.device()
    h.open(0x6677, 0x8811)  # TREZOR VendorID/ProductID

    print("Manufacturer: %s" % h.get_manufacturer_string())
    print("Product: %s" % h.get_product_string())
    print("Serial No: %s" % h.get_serial_number_string())

    # enable non-blocking mode
    h.set_nonblocking(1)

    # write some data to the device
    print("Write the data")
    h.write([0, 63, 35, 35] + [0] * 61)

    # wait
    time.sleep(0.10)

    # read back the answer
    print("Read the data")
    while True:
        d = h.read(64)
        if d:
            print(d)
        else:
            time.sleep(0.05)

    print("Closing the device")
    h.close()

except IOError as ex:
    print(ex)
    print("You probably don't have the hard coded device. Update the hid.device line")
    print("in this script with one from the enumeration list output above and try again.")

print("Done")
