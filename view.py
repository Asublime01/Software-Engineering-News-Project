import time
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import adafruit_blinka_raspberry_pi5_piomatter as piomatter
import model




def update_display():
    # -----------------------------------------------------------
    # Combined display settings
    # -----------------------------------------------------------
    PANEL_W = 32
    PANEL_H = 32
    NUM_PANELS = 3

    WIDTH = PANEL_W * NUM_PANELS   # 64
    HEIGHT = PANEL_H               # 32
    
    TITLE_HEIGHT = 12
    SCROLL_HEIGHT = HEIGHT - TITLE_HEIGHT

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

#Prepare scrolling text------------------------------------------------
    title_text = "EPIC News"
    text = model.get_random_news()  # the message to scroll
    font_TITLE = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 12)
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 12)


    # Create a temporary canvas to measure text
    temp_canvas = Image.new("RGB", (1,1))
    temp_draw = ImageDraw.Draw(temp_canvas)
    bbox = temp_draw.textbbox((0,0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Create a canvas for the text, wide enough for scrolling
    scroll_canvas = Image.new("RGB", (text_width + WIDTH, SCROLL_HEIGHT), (0, 0, 0))
    scroll_draw = ImageDraw.Draw(scroll_canvas)
    
    scroll_y = (SCROLL_HEIGHT - text_height) // 2
    scroll_draw.text((WIDTH, scroll_y), text, font=font, fill=(255, 255, 255))

    # ===========================================================
    # Scroll loop
    # ===========================================================
    scroll_speed = 0.025  # seconds per pixel
    while True:
        for x in range(text_width + WIDTH):
            # Copy the portion of the text canvas to the framebuffer
            master = Image.new("RGB", (WIDTH, HEIGHT), (0,0,0))
            draw = ImageDraw.Draw(master)
            
            #Draw title at the top
            draw.text((2,0), title_text, font=font_TITLE, fill=(0xFFFF8C00))
            
            
            #Crop scrolling information and paste below title
            crop = scroll_canvas.crop((x,0,x+WIDTH, SCROLL_HEIGHT))
            master.paste(crop, (0,TITLE_HEIGHT))
            
            draw.rectangle((0,TITLE_HEIGHT + 2, WIDTH, TITLE_HEIGHT + 2), fill=(0xFF4F9153))
            
            framebuffer[:] = np.asarray(master)
            matrix.show()
            time.sleep(scroll_speed)
