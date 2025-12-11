import time
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import adafruit_blinka_raspberry_pi5_piomatter as piomatter
import model




def do_the_thing(bool, num_run): #Main function for running both displays
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

    if bool == 1: #Display EPIC News
    #Prepare scrolling text------------------------------------------------
        title_text = "Attention!!"
        text = model.get_epic_news()  # the message to scroll
        if text == 2:
            title_text = "CS News"
            text = model.get_random_news()
    elif bool == 2: #Display CS News
        title_text = "CS News"
        text = model.get_random_news()
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
    for i in range(num_run):
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

    
def update_display():
    do_the_thing(1, 2)
    do_the_thing(2, 2)
        

        

