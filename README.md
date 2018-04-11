"""
Show Me Your Dance
=======

### Find the mat!

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

### List USB Devices

```bash
# list usb devices
ioreg -p IOUSB -w0
```

### The Dance Mat Info

```text
# the mat
Decimal VendorID=26231 & ProductID=34833
Hexadecimal VendorID=0x6677 & ProductID=0x8811
```

### The Dance Mat Data

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

### Sending Keys

```bash
osascript -e 'tell application "System Events" to keystroke "m"'
```

### More on Applescript / Sending Keys

https://eastmanreference.com/complete-list-of-applescript-key-codes/
"""
