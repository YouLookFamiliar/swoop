# -*- coding: utf-8 -*-

import subprocess


def picamera_connected():
    """Checks if the Raspberry Pi Camera is connected.

    :rtype: bool
    """
    detected = 0

    try:
        vcgencmd = subprocess.check_output(['vcgencmd', 'get_camera'])
        detected = int(vcgencmd.strip()[-1])
    except subprocess.CalledProcessError:
        return False

    return bool(detected)
