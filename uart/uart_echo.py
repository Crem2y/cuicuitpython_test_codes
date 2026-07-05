import time
import board
import busio

uart = busio.UART(
    tx=board.D6,
    rx=board.D7,
    baudrate=921600,
    timeout=0.1,
    receiver_buffer_size=256,
)

uart.write(b"UART line mode ready\r\n")

while True:
    line = uart.readline()

    if line is not None:
        print("LINE:", line)

        uart.write(b"echo: ")
        uart.write(line)
        uart.write(b"\n")

    time.sleep(0.001)