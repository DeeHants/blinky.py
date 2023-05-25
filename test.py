import blinkyLib

serial_port = 'COM5'
led_count = 30

# Connect to the strip
tape = blinkyLib.BlinkyTape(serial_port, led_count)

# Static colour
colour = blinkyLib.Color(128, 0, 255)
# colour = blinkyLib.Color.Black()
frame = blinkyLib.StaticFrame.CreateSolidFrame(colour)
tape.renderFrame(frame)

# Fade
frame = blinkyLib.StaticFrame.CreateFade(blinkyLib.Color.FromHex(0xff0000), blinkyLib.Color.FromHex(0x00ff00))
# frame.setRangeFade(0, int(led_count / 2), blinkyLib.Color.Red(), blinkyLib.Color.FromHex(0x32CD32))
# frame.setRangeFade(int(led_count / 2), led_count - 1, blinkyLib.Color.FromHex(0x32CD32), blinkyLib.Color.Blue())
tape.renderFrame(frame)
