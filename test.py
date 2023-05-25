import blinkyLib

serial_port = 'COM5'
led_count = 30

# Connect to the strip
tape = blinkyLib.BlinkyTape(serial_port, led_count)

# Static colour
colour = blinkyLib.Color(128, 0, 255)
# colour = blinkyLib.Color.Black()
frame = blinkyLib.StaticFrame.create_solid_frame(colour)
tape.render_frame(frame)

# Fade
frame = blinkyLib.StaticFrame.create_fade_frame(blinkyLib.Color.FromHex(0xff0000), blinkyLib.Color.FromHex(0x00ff00))
# frame.set_range_fade(0, int(led_count / 2), blinkyLib.Color.Red(), blinkyLib.Color.FromHex(0x32CD32))
# frame.set_range_fade(int(led_count / 2), led_count - 1, blinkyLib.Color.FromHex(0x32CD32), blinkyLib.Color.Blue())
tape.render_frame(frame)
