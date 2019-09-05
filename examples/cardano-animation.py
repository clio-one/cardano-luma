#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017-18 Richard Hull and contributors
# See LICENSE.rst for details.
# PYTHON_ARGCOMPLETE_OK

"""
Displays an animated gif.
"""

import os.path
from demo_opts import get_device
from PIL import Image, ImageSequence
from luma.core.sprite_system import framerate_regulator


def main():
    regulator = framerate_regulator(fps=25)
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
        'images', 'cardano-loader_128x128.gif'))
    banana = Image.open(img_path)
    size = [min(*device.size)] * 2
    posn = ((device.width - size[0]) // 2, device.height - size[1])

    counter = 0
    while counter < 3:
		counter +=1
        for frame in ImageSequence.Iterator(banana):
            with regulator:
                background = Image.new("RGB", device.size, "black")
                background.paste(frame.resize(size, resample=Image.LANCZOS), posn)
                device.display(background.convert(device.mode))


if __name__ == "__main__":
    try:
        device = get_device()
        main()
    except KeyboardInterrupt:
        pass
