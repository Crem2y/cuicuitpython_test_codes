import time

from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

ble = BLERadio()
ble.name = "CP-UART"

uart = UARTService()

adv = ProvideServicesAdvertisement(uart)
adv.complete_name = "CP-UART"

print("BLE UART ready")
ble.start_advertising(adv)

while True:
    if not ble.connected:
        if not ble.advertising:
            print("advertising")
            ble.start_advertising(adv)

        time.sleep(0.2)
        continue

    if ble.advertising:
        ble.stop_advertising()

    print("connected")

    while ble.connected:
        if uart.in_waiting:
            data = uart.readline()

            if data is not None:
                try:
                    text = data.decode("utf-8").strip()
                except UnicodeError:
                    text = repr(data)

                print("rx:", text)

                uart.write(b"echo: ")
                uart.write(data)

        time.sleep(0.01)

    print("disconnected")

    try:
        ble.stop_advertising()
    except Exception:
        pass

    time.sleep(0.5)