import time
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import adafruit_blinka_raspberry_pi5_piomatter as piomatter
import model, controller

# -----------------------------------------------------------
# Combined display settings
# -----------------------------------------------------------
PANEL_W = 32
PANEL_H = 32
NUM_PANELS = 3

WIDTH = PANEL_W * NUM_PANELS   # 64
HEIGHT = PANEL_H               # 32

geometry = piomatter.Geometry(
    width=WIDTH,
    height=HEIGHT,
    n_addr_lines=4,
    rotation=piomatter.Orientation.Normal
)

# ===========================================================
# One framebuffer for the entire display
# ===========================================================
framebuffer = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)

matrix = piomatter.PioMatter(
    colorspace=piomatter.Colorspace.RGB888Packed,
    pinout=piomatter.Pinout.Active3,
    framebuffer=framebuffer,
    geometry=geometry
)

# ===========================================================
# Prepare scrolling text
# ===========================================================
def update_display():
    text = model.get_random_news()  # the message to scroll
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)

    # Create a temporary canvas to measure text
    temp_canvas = Image.new("RGB", (1,1))
    temp_draw = ImageDraw.Draw(temp_canvas)
    bbox = temp_draw.textbbox((0,0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Create a canvas for the text, wide enough for scrolling
    text_canvas = Image.new("RGB", (text_width + WIDTH, HEIGHT), (0, 0, 0))
    text_draw = ImageDraw.Draw(text_canvas)
    text_draw.text((WIDTH, (HEIGHT - text_height)//2), text, font=font, fill=(255, 0, 255))

    # ===========================================================
    # Scroll loop
    # ===========================================================
    scroll_speed = 0.05  # seconds per pixel
    while True:
        for x in range(text_width + WIDTH):
            # Copy the portion of the text canvas to the framebuffer
            portion = text_canvas.crop((x, 0, x + WIDTH, HEIGHT))
            framebuffer[:] = np.asarray(portion)
            matrix.show()
            time.sleep(scroll_speed)
