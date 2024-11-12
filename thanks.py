import board
import displayio
from adafruit_st7789 import ST7789

displayio.release_displays()

# Establish SPI interface
spi = board.SPI()
tft_cs = board.D2  # this is the CS pin you chose on the board
tft_dc = board.D3 # this is the DC pin you chose on the board
disp_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs)
display = ST7789(disp_bus, rotation=270, width=240, height=135, rowstart=40, colstart=53)

my_group = displayio.Group()
display.root_group = my_group


my_bitmap = displayio.Bitmap(240, 135, 1) 
my_palette = displayio.Palette(1) 
my_palette[0] = 0xFFFFFF 
my_sprite = displayio.TileGrid(my_bitmap, x=0, y=0, pixel_shader=my_palette)




from adafruit_display_shapes.rect import Rect
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.roundrect import RoundRect
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.polygon import Polygon





triangle = Triangle(45, 95, 50, 100, 55, 95, fill=0xeeee1b, outline=0xeeee1b)
my_group.append(my_sprite)
my_group.append(triangle)

rect = Rect(165, 20, 25, 60, fill=None, outline=0xad8e56, stroke=1)
my_group.append(rect)

rect = Rect(173, 70, 5, 10, fill=None, outline=0xeeee1b, stroke=2)
my_group.append(rect)

line = Line(140, 80, 220, 80, color=0xa06f18)
my_group.append(line)

circle = Circle(50, 100, 20, fill=None, outline=0xa06f18, stroke=2)
my_group.append(circle)

triangle2 = Triangle(40, 85, 40, 60, 45, 70, fill=None, outline=0xe94406)
my_group.append(triangle2)
triangle2 = Triangle(50, 85, 50, 60, 55, 70, fill=None, outline=0xe94406)
my_group.append(triangle2)
triangle2 = Triangle(60, 85, 60, 60, 65, 70, fill=None, outline=0xe94406)
my_group.append(triangle2)



while True:
    pass
