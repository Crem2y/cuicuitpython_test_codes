import time
import board
import digitalio

from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.standard.hid import HIDService

from adafruit_hid.mouse import Mouse

button = digitalio.DigitalInOut(board.D0)
button.switch_to_input(pull=digitalio.Pull.UP)

ble = BLERadio()
ble.name = "CP BLE Mouse"

hid = HIDService()
mouse = Mouse(hid.devices)

adv = ProvideServicesAdvertisement(hid)
adv.complete_name = "CP BLE Mouse"
adv.appearance = 962  # Mouse

was_pressed = False

print("BLE HID mouse ready")
print("start HID advertising")
ble.start_advertising(adv)
print("advertising:", ble.advertising)

while True:
    if not ble.connected:
        if not ble.advertising:
            ble.start_advertising(adv)

        was_pressed = False
        time.sleep(0.2)
        continue

    if ble.advertising:
        ble.stop_advertising()

    pressed = not button.value

    if pressed and not was_pressed:
        print("mouse click")
        mouse.move(x=80, y=0)
        time.sleep(0.2)
        mouse.move(x=-80, y=0)
        time.sleep(0.2)
        mouse.move(x=0, y=80)
        time.sleep(0.2)
        mouse.move(x=0, y=-80)
        time.sleep(0.2)
#        mouse.move(x=20, y=0)
        mouse.click(Mouse.LEFT_BUTTON)

    was_pressed = pressed
    time.sleep(0.02)