# x11util Package

x11util - Wrapper fucntions to make X11 low-level Xlib programming easier

# DESCRIPTION

This manual page documents **x11util** module, a Python module providing
several wrapper function for Xlib programming easier.

# EXAMPLE

```python
import time
from Xlib import X, display
from x11util import create_window, create_gcs, load_font, draw_str, flush

disp = display.Display()
font = load_font(disp)
screen = disp.screen()
window = create_window(disp, screen, width=320, height=240, x=100, y=200)
gcs = create_gcs(disp, screen, window, font)
draw_str(disp, screen, window, gcs, 'Hello, World!', 10, 20)
draw_str(disp, screen, window, gcs, 'Hello, World!', 11, 21, level=50)
flush(disp, screen)
time.sleep(10)
```

# FUNCTIONS

**x11util** module provides the following functions.

- create_window(disp, screen, width=640, height=480, x=0, y=0, override=1, mask=X.ExposureMask)

  Create a new window on screen SCREEN in display DISP with given WIDTH and
  HEIGHT, which is placed at the geometry of (X, Y) using Xlib's
  XCreateWindow.  override_redirect and event_mask can specified by OVERRIDE
  and MASK, respectively.

- load_font(disp, font=None)

  Load bitmap font FONT in display DISP, and return the loaded font object.
  If font loading failed, return None.

- create_gcs(disp, screen, window, font)

  Create GCs (Graphics Content) on screen SCREEN in display DISP for window
  WINDOW with font FONT.  GCs are returned as a dictionary, whose key is the
  color name (e.g., 'SteelBlue') and the value is a dictionary, whose items
  are (LEVEL, GC), where LEVEL is a brightness between 0 and 100 and GC is the
  GC for that brightness.

- clear(window)

  Erase the window WINDOW.

- draw_str(disp, screen, window, gcs, astr, col=0, row=0, color='PaleGreen', level=100, reverse=False)

  Render a string ASTR on window WINDOW on screen SCREEN in display DISP using
  graphics contents GC.  Text color and brightness can be specified by COLOR
  and LEVEL, respectively.  Reverse video is enabled if REVERSE is True.

- flush(disp, screen)

  Flush all pending X11 requests.

# INSTALLATION

```python
pip3 install x11util
```

# AVAILABILITY

The latest version of **perlcompat** module is available at PyPI
(https://pypi.org/project/x11util/) .

# SEE ALSO

- Xlib - C Language X Interface
- python3-xlib (https://pypi.org/project/python3-xlib/)

# AUTHOR

Hiroyuki Ohsaki <ohsaki[atmark]lsnl.jp>
