from smbus import SMBus
addr = 8
bus = SMBus(1)
bus.write_byte(addr, 1)
input("press return to exit")
bus.write_byte(addr, 0)
