import time
import board
import digitalio

from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.standard.hid import HIDService

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

button = digitalio.DigitalInOut(board.D0)
button.switch_to_input(pull=digitalio.Pull.UP)

ble = BLERadio()
ble.name = "CP BLE Keyboard"

hid = HIDService()
kbd = Keyboard(hid.devices)

adv = ProvideServicesAdvertisement(hid)
adv.complete_name = "CP BLE Keyboard"
adv.appearance = 961  # Keyboard

was_pressed = False

print("BLE HID keyboard ready")
print("start HID advertising")
ble.start_advertising(adv)
print("advertising:", ble.advertising)

while True:
    if not ble.connected:
        if not ble.advertising:
            print("advertising")
            ble.start_advertising(adv)

        was_pressed = False
        time.sleep(0.2)
        continue

    if ble.advertising:
        ble.stop_advertising()

    pressed = not button.value  # pull-up: pressed == False input

    if pressed and not was_pressed:
        print("send A")
        kbd.send(Keycode.A)

    was_pressed = pressed
    time.sleep(0.02)