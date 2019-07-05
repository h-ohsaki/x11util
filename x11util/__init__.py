#!/usr/bin/env python3
#
# Wrapper fucntions to make X11 low-level Xlib programming easier.
# Copyright (c) 2018-2019, Hiroyuki Ohsaki.
# All rights reserved.
#
# $Id: xutil.py,v 1.8 2019/02/27 14:16:58 ohsaki Exp $
#

import time

from Xlib import X, display

FONT_NAME = '-schumacher-clean-bold-r-normal--8-80-75-75-c-80-iso646.1991-irv'
FONT_WIDTH = 8
FONT_HEIGHT = 8

COLORS = [
    'SteelBlue1',
    'PaleGreen',
    'LightGoldenrod',
    'chocolate1',
    'black',
    'LightCyan',
    'aquamarine1',
    'aquamarine2',
    'aquamarine3',
    'aquamarine4',
    'DarkSlateGray',
    'orange',
    'OrangeRed',
]

def create_window(disp,
                  screen,
                  width=640,
                  height=480,
                  x=0,
                  y=0,
                  override=1,
                  mask=X.ExposureMask):
    """Create a new window on screen SCREEN in display DISP with given WIDTH
    and HEIGHT, which is placed at the geometry of (X, Y) using Xlib's
    XCreateWindow.  override_redirect and event_mask can specified by OVERRIDE
    and MASK, respectively."""
    window = screen.root.create_window(
        x,
        y,
        width,
        height,
        0,
        screen.root_depth,
        X.InputOutput,
        X.CopyFromParent,
        background_pixel=screen.black_pixel,
        override_redirect=override,
        event_mask=mask,
        colormap=X.CopyFromParent,
    )
    window.change_attributes(backing_store=X.Always)
    window.map()
    return window

def load_font(disp, font=None):
    """Load bitmap font FONT in display DISP, and return the loaded font
    object.  If font loading failed, return None."""
    if font is not None:
        global FONT_NAME
        FONT_NAME = font
        spec = font.split('-')
        # record the font width and height for later use
        try:
            if spec[7]:
                global FONT_WIDTH
                FONT_WIDTH = int(spec[7])
            if spec[12]:
                global FONT_HEIGHT
                FONT_HEIGHT = int(spec[12]) // 10
        except:
            pass
    font = disp.open_font(FONT_NAME)
    return font

def create_gcs(disp, screen, window, font):
    """Create GCs (Graphics Content) on screen SCREEN in display DISP for
    window WINDOW with font FONT.  GCs are returned as a dictionary, whose key
    is the color name (e.g., 'SteelBlue') and the value is a dictionary, whose
    items are (LEVEL, GC), where LEVEL is a brightness between 0 and 100 and
    GC is the GC for that brightness."""
    gcs = {}
    for color in COLORS:
        colormap = screen.default_colormap
        pixel = colormap.alloc_named_color(color).pixel
        red = (pixel >> 16) & 0xff
        green = (pixel >> 8) & 0xff
        blue = (pixel >> 0) & 0xff
        gcs[color] = {}
        for level in range(100 + 1):
            r = int(red * level / 100)
            g = int(green * level / 100)
            b = int(blue * level / 100)
            pixel = (r << 16) | (g << 8) | b
            gcs[color][level] = window.create_gc(font=font, foreground=pixel)
    return gcs

def clear(window):
    """Erase the window WINDOW."""
    geom = window.get_geometry()
    window.clear_area(0, 0, geom.width, geom.height)

def draw_str(disp,
             screen,
             window,
             gcs,
             astr,
             col=0,
             row=0,
             color='PaleGreen',
             level=100,
             reverse=False):
    """Render a string ASTR on window WINDOW on screen SCREEN in display DISP
    using graphics contents GC.  Text color and brightness can be specified by
    COLOR and LEVEL, respectively.  Reverse video is enabled if REVERSE is
    True."""
    fgcolor, bgcolor = color, 'black'
    if reverse:
        fgcolor, bgcolor = bgcolor, fgcolor
    x = col * FONT_WIDTH
    y = row * FONT_HEIGHT
    # FIXME: this code could be written simpler?
    chars = [chr(c).encode() for c in list(astr.encode())]
    window.poly_text(gcs[fgcolor][level], x, y + FONT_HEIGHT - 1, chars)

def flush(disp, screen):
    # NOTE: the following line is necessary due to unknown reason
    screen.default_colormap.alloc_named_color('white')

def main():
    disp = display.Display()
    font = load_font(disp)
    screen = disp.screen()
    window = create_window(disp, screen, width=320, height=240, x=100, y=200)
    gcs = create_gcs(disp, screen, window, font)
    draw_str(disp, screen, window, gcs, 'Hello, World!', 10, 20)
    draw_str(disp, screen, window, gcs, 'Hello, World!', 11, 21, level=50)
    flush(disp, screen)
    time.sleep(10)

if __name__ == "__main__":
    main()
