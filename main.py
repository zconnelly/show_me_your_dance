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
"""
import time
import usb

dev = usb.core.find(idVendor=0x6677, idProduct=0x8811)

# use the default configuration
dev.set_configuration()

# first endpoint
endpoint = dev[0][(0, 0)][0]

data = None
while True:
    time.sleep(1)
    try:
        data = dev.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize)
        print data
    except usb.core.USBError as e:
        print e
