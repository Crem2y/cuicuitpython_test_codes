import time
import board
import busio
import pwmio

uart = busio.UART(
    tx=board.D6,
    rx=board.D7,
    baudrate=921600,
    timeout=0.1,
    receiver_buffer_size=256,
)
led1 = pwmio.PWMOut(
    board.D0,
    frequency=1000,
    duty_cycle=0
)
led2 = pwmio.PWMOut(
    board.D1,
    frequency=1000,
    duty_cycle=0
)
led3 = pwmio.PWMOut(
    board.D2,
    frequency=1000,
    duty_cycle=0
)
led4 = pwmio.PWMOut(
    board.D3,
    frequency=1000,
    duty_cycle=0
)

# uart.write(b"UART line mode ready\r\n")

led1.duty_cycle = 65535
led2.duty_cycle = 65535
led3.duty_cycle = 65535
led4.duty_cycle = 65535

while True:
    line = uart.readline()

    if line is not None:
        print("LINE:", line)

        uart.write(b'\xaa\x04\x0c\x00\x10\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x18\x55U')
#        uart.write(b'\xaa\x03\x00\x03\x55U')

    time.sleep(0.001)