# -*- coding: utf-8 -*-

import re
import subprocess


def picamera_status():
    """Returns support and detection status for the Raspberry Pi Camera.

    :return: (supported, detected)
    :rtype: (bool, bool)
    """
    supported, detected = False, False
    vcgencmd_regex = r'supported=(0|1) detected=(0|1)'

    try:
        vcgencmd = subprocess.check_output(['vcgencmd', 'get_camera'])
        result = re.match(vcgencmd_regex, vcgencmd).groups()

        supported = bool(int(result[0]))
        detected = bool(int(result[1]))
    except (subprocess.CalledProcessError, OSError):
        return False, False

    return supported, detected
