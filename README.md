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
