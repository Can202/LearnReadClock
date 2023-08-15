import platformdetect

WIDTH = 1280
HEIGHT = 720
if platformdetect.platform() == "android":
    DEFINEWIDTH = WIDTH
    DEFINEHEIGHT =  HEIGHT
else:
    DEFINEHEIGHT = 0
    DEFINEWIDTH = 0

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)